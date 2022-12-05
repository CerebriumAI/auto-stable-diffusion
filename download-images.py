import os

from storage3 import create_client as create_storage_client
from supabase import create_client, Client

url = "<SUPABSE_URL>"
key = "<SUPABSE_ANON_KEY>"
headers = {"apiKey": key, "Authorization": f"Bearer {key}"}

# pass in is_async=True to create an async client
storage_client = create_storage_client(url + "/storage/v1", headers, is_async=False)
supabase: Client = create_client(url, key)

UUIDs = storage_client.get_bucket('images').list('unprocessed')

if not os.path.isdir("images/unprocessed"):
    os.makedirs("images/unprocessed")

for UUID in UUIDs:

    if UUID['name'] == '.emptyFolderPlaceholder':
        continue

    if not os.path.isdir("images/unprocessed/" + UUID['name']):
        os.makedirs("images/unprocessed/" + UUID['name'])

    files = storage_client.get_bucket('images').list('unprocessed/' + UUID['name'])

    supabase_paths = []

    for file in files:
        print(file)

        if file['name'] == '.emptyFolderPlaceholder':
            continue

        from_path = 'unprocessed/' + UUID['name'] + '/' + file['name']
        to_path = 'processed/' + UUID['name'] + '/' + file['name']

        supabase_paths.append(from_path)
        c = storage_client.get_bucket('images').download(from_path)
        storage_client.get_bucket('images').move(from_path, to_path)
        f = open("images/unprocessed/" + UUID['name'] + '/' + file['name'], "wb")
        f.write(c)
        f.close()

    supabase.from_("profiles").update({"unprocessed": []}).eq("id", UUID['name']).execute()
    supabase.from_("profiles").update({"processed": supabase_paths}).eq("id", UUID['name']).execute()
