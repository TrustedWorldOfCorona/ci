"""
Test for discovering TWOC FAIR Data Point instances.
"""

import requests
import sys

INDEX = "https://twoc-index.fair-dtls.surf-hosted.nl"
ENTRIES_ENDPOINT = INDEX + "/index/entries/all"
EXPECTED_ENTRIES = 3

numEntries = 0

for entry in requests.get(ENTRIES_ENDPOINT).json():
    try:
        clientUrl = entry["clientUrl"]
        print(f"Requesting client url {clientUrl}")
        requests.get(clientUrl)
        print("Resolved client url")
        numEntries += 1
    except:
        continue

print(f"Found {numEntries} entries")

if numEntries < EXPECTED_ENTRIES:
    print(f"Expected {EXPECTED_ENTRIES} entries")
    sys.exit(1)
