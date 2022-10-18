#! /usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

import os
import magic
import boto3
import math
import argparse
from termcolor import colored
from tqdm import tqdm

class StorageAPI:
    def __init__(self, prefix):
        self.s3 = boto3.client(
            's3',
            region_name=os.environ['S3_REGION'],
            endpoint_url=os.environ['S3_ENDPOINT'],
            aws_access_key_id=os.environ['S3_ACCESS_KEY'],
            aws_secret_access_key=os.environ['S3_ACCESS_SECRET'],
        )
        
        self.prefix = prefix


    def __get_key(self, key):
        return f'{self.prefix}/{key}'


    def __head(self, key):
        try: 
            return self.s3.head_object(
                Bucket=os.environ['S3_BUCKET'],
                Key=key
            )
        except:
            return None

    def get_listing(self, prefix):
        keys = []

        paginator = self.s3.get_paginator('list_objects')
        for result in paginator.paginate(
                Bucket=os.environ['S3_BUCKET'],
                Delimiter='/',
                Prefix=prefix
            ):
            for obj in result.get('Contents'):
                keys.append(obj.get('Key'))

        return keys

    def exists(self, filename):
        key = self.__get_key(filename)
        head = self.__head(key)

        if head is None:
            return False

        size = os.path.getsize(filename)
        remote_size = int(head['ContentLength'])

        if size != remote_size:
            return False

        return True

    def upload(self, filename):
        key = self.__get_key(filename)

        response = self.s3.upload_file(
            filename,
            os.environ['S3_BUCKET'],
            key,
            ExtraArgs={
                # infer mime type
                'ContentType': magic.from_file(filename, mime=True),
                'ACL': 'public-read'
            }
        )

    
class LocalFileTree:
    def __init__(self, storage):
        self.storage = storage

    def __get_human_size(self, filename):
        size = os.path.getsize(filename)

        if size / (1024*1024) > 1:
            return f'{math.ceil(size/(1024*1024))} MB'

        return f'{math.ceil(size/1024)} KB'

    def build_tree(self, directory):

        base = os.path.basename(directory)
        # mega hacky
        os.chdir(
            os.path.abspath(
                os.path.join(
                    directory,
                    '..'
                )
            )
        )
        walk = list(os.walk(base))


        for folder,_,files in walk:
            for file in tqdm(files):
                if file[0] == '.':
                    continue
                filename = os.path.join(folder,file)

                if self.storage.exists(filename):
                    print(f'{colored("IGNORE", "yellow")}: {filename} ({self.__get_human_size(filename)})')
                else:
                    print(f'{colored("UPLOAD", "green")}: {filename} ({self.__get_human_size(filename)})')
                    self.storage.upload(filename)

                print(filename)


def _main():
    parser = argparse.ArgumentParser(description='Upload a folder to S3')
    parser.add_argument('folder', help='folder to upload', type=str)
    parser.add_argument('--prefix', help='S3 prefix', type=str, required=True)
    args = parser.parse_args()

    print(f'Uploading {args.folder} to {args.prefix}...')

    storage = StorageAPI(args.prefix)

    lft = LocalFileTree(storage)
    lft.build_tree(args.folder)

if __name__ == '__main__':
    _main()
