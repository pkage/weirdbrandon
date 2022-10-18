#! /usr/bin/env python3

import json
import os
import random

def load_tags():
    return json.load(open('tags.json', 'r'))


def random_modifiers(tags):
    all_categories = list(tags.keys())
    sample_size = random.randint(2, min(len(all_categories), 5))

    categories = random.sample(all_categories, sample_size)


    out = []
    for cat in categories:
        out.append(random.choice(tags[cat]))

    return out


def make_id():
    alphabet = 'bcdfghjklmnpqrstvwxyz0123456789'
    
    return ''.join([random.choice(alphabet) for _ in range(8)])


class RunConfig:
    modifiers = []
    seed = 0
    image_id = ''

    def __init__(self, tags):
        self.seed = random.randint(0,65536)
        self.modifiers = random_modifiers(tags)
        self.image_id = make_id()

    def get_json(self):
        obj = {
            'seed':      self.seed,
            'modifiers': self.modifiers,
            'image_id':  self.image_id
        }

        return json.dumps(obj)

    def get_prompt(self):
        return ', '.join([
            'joe biden',
            *self.modifiers
        ])


    def get_seed(self):
        return self.seed


    def __prefix_wrap(self, filename, prefix=None):
        if prefix is None:
            return filename

        return os.path.join(prefix, filename)


    def get_image_name(self, prefix=None):
        filename = f'{self.image_id}.png'

        return self.__prefix_wrap(filename, prefix=prefix)


    def get_metadata_name(self, prefix=None):
        filename = f'{self.image_id}.json'

        return self.__prefix_wrap(filename, prefix=prefix)



if __name__ == '__main__':
    tags = load_tags()

    rc = RunConfig(tags)

    print(rc.to_json())
    print(rc.get_prompt())
    print(rc.get_image_name('out/'))
    print(rc.get_metadata_name('out/'))
