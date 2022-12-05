import os
import random
import sys

import torch
from diffusers import StableDiffusionPipeline

UUID = sys.argv[1]
CLASS_TYPE = sys.argv[2]
NUM_TRAIN_STEPS = sys.argv[3]

model_id = f"./weights/{UUID}/{NUM_TRAIN_STEPS}"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

prompts = [
    f"{UUID} {CLASS_TYPE} as a a fantasy style portrait painting oil painting unreal 5 daz. rpg portrait, extremely detailed artgerm greg rutkowski greg hildebrandt tim hildebrandt",
    f"portrait of {UUID} {CLASS_TYPE} by greg rutkowski, impeccable military composure, wearing tactical gear of the galactic alliance, star wars expanded universe, highly detailed portrait, digital painting, artstation, concept art, smooth, sharp foccus ilustration, artstation hq ",
    f"portrait of {UUID} {CLASS_TYPE} by Greg Rutkowski, old jedi Master Luke Skywalker from Star Wars Expanded Universe, he is about 60 years old, wearing black robes, highly detailed portrait, digital painting, artstation, concept art, smooth, sharp foccus ilustration, Artstation HQ",
    f"ultra realistic illustration, {UUID} {CLASS_TYPE}, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha",
    f"a portrait of {UUID} {CLASS_TYPE} as obi - wan kenobi, fantasy, sharp focus, intricate, elegant, digital painting, artstation, matte, highly detailed, concept art, illustration, ambient lighting, art by ilya kuvshinov, artgerm, alphonse mucha, and greg rutkowski "
]

run_number = random.randrange(1, 10000)
prompt_index = 1
for prompt in prompts:
    images = pipe(prompt, num_inference_steps=50, guidance_scale=7.5, num_images_per_prompt=4).images

    print(f"Number of images: {len(images)}")

    image_index = 1
    for image in images:

        if not os.path.isdir(f"images/output/{UUID}"):
            os.makedirs(f"images/output/{UUID}")

        image.save(f"images/output/{UUID}/{run_number}-{prompt_index}-{image_index}.png")
        image_index = image_index + 1

    prompt_index = prompt_index + 1
