#! /usr/bin/env python3

from dotenv import load_dotenv
load_dotenv()

import json

from upload import StorageAPI


OUTPUT = 'out/'

storage  = StorageAPI('wb')
listing = storage.get_listing('wb/out/')

get_id = lambda x: x.split('/')[-1].split('.')[0]

ids = set([get_id(x) for x in listing])
ids = list(ids)

json.dump(
    {'ids': ids},
    open('all_ids.json', 'w')
)

storage.upload('all_ids.json')
