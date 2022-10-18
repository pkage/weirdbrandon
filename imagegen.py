#! /usr/bin/env python3

from autodraw.image import StableDiffusion
from promptgen import RunConfig, load_tags
from tqdm import tqdm

import sys

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} NUMBER')
    sys.exit(1)

PREFIX = 'out/'
BATCH_COUNT = int(sys.argv[1])

class SDBatchGenerator:
    sd = None
    tags = None
    output = ''

    def __init__(self, output):
        self.tags   = load_tags()
        self.sd     = StableDiffusion()
        self.output = output

    def generate(self):
        rc = RunConfig(self.tags)

        img = self.sd.stable_diffusion(
            rc.get_prompt(),
            seed=rc.get_seed(),
            unsafe=True
        )

        img.save(rc.get_image_name(prefix='out/'))
    
        with open(rc.get_metadata_name(prefix='out/'), 'w') as metaout:
            metaout.write(rc.get_json())

if __name__ == '__main__':
    sdbg = SDBatchGenerator(PREFIX)
    
    for i in tqdm(range(BATCH_COUNT)):
        sdbg.generate()
