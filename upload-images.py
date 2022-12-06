import os
from os import scandir

from storage3 import create_client as storage_client
from supabase import create_client, Client

url = "<SUPABSE_URL>"
key = "<SUPABSE_SERVICE_ROLE>"
headers = {"apiKey": key, "Authorization": f"Bearer {key}"}

options = {"contentType": "image/png"}

# pass in is_async=True to create an async client
storage_client = storage_client(url + "/storage/v1", headers, is_async=False)
supabase: Client = create_client(url, key)

UUIDs = [f.path for f in scandir('images/output') if f.is_dir()]

for UUID in UUIDs:
    files = [f.path for f in scandir(UUID) if f.is_file()]
    supabase_paths = []
    for file in files:
        supabase_path = os.path.relpath(file, 'images/')

        print("Uploading: " + file)
        storage_client.get_bucket('images').upload(supabase_path, file, options)
        supabase_paths.append(supabase_path)

        # Move file so it doesn't get uploaded twice
        path = os.path.split(file)[0]
        if not os.path.isdir("images/uploaded/" + path):
            os.makedirs("images/uploaded/" + path)
        os.rename(file, "images/uploaded/" + file)
