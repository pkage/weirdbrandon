#! /usr/bin/env python3

from autodraw.image import StableDiffusion
from promptgen import RunConfig, load_tags

PREFIX = 'out/'

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
            seed=rc.get_seed()
        )

        img.save(rc.get_image_name(prefix='out/'))
    
        with open(rc.get_metadata_name(prefix='out/'), 'w') as metaout:
            metaout.write(rc.get_json())

if __name__ == '__main__':
    sdbg = SDBatchGenerator(PREFIX)
    
    BATCH_COUNT = 3
    for i in range(BATCH_COUNT):
        print(f'generating {i+1} of {BATCH_COUNT}')
        sdbg.generate()
