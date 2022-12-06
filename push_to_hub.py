import random
import sys

from huggingface_hub import HfApi
from huggingface_hub import create_repo

UUID = sys.argv[1]
OUTPUT_DIR = sys.argv[2]
HF_TOKEN = sys.argv[3]
concept_name = UUID or f"session-{random.randrange(1, 10000)}"

api = HfApi()
username = api.whoami(token=HF_TOKEN)["name"]

repo_id = f"{username}/{concept_name}"


def bar(prg):
    br = "[1;33mUploading to HuggingFace : " '[0m|' + '█' * prg + ' ' * (25 - prg) + '| ' + str(prg * 4) + "%"
    return br


print("Loading...")

print(bar(1))

create_repo(repo_id, private=True, token=HF_TOKEN)

api.create_commit(repo_id=repo_id, operations=[], commit_message=f"Upload the concept {concept_name} embeds and token", token=HF_TOKEN)

api.upload_folder(folder_path=OUTPUT_DIR + "/600/feature_extractor", path_in_repo="feature_extractor", repo_id=repo_id, token=HF_TOKEN)

print(bar(8))

api.upload_folder(folder_path=OUTPUT_DIR + "/600/scheduler", path_in_repo="scheduler", repo_id=repo_id, token=HF_TOKEN)

print(bar(9))

api.upload_folder(folder_path=OUTPUT_DIR + "/600/text_encoder", path_in_repo="text_encoder", repo_id=repo_id, token=HF_TOKEN)

print(bar(12))

api.upload_folder(folder_path=OUTPUT_DIR + "/600/tokenizer", path_in_repo="tokenizer", repo_id=repo_id, token=HF_TOKEN)

print(bar(13))

api.upload_folder(folder_path=OUTPUT_DIR + "/600/unet", path_in_repo="unet", repo_id=repo_id, token=HF_TOKEN)

print(bar(21))

api.upload_folder(folder_path=OUTPUT_DIR + "/600/vae", path_in_repo="vae", repo_id=repo_id, token=HF_TOKEN)

print(bar(23))

api.upload_file(path_or_fileobj=OUTPUT_DIR + "/600/model_index.json", path_in_repo="model_index.json", repo_id=repo_id, token=HF_TOKEN)

print(bar(24))

print(f"Your concept was saved successfully. https://huggingface.co/{repo_id}")
