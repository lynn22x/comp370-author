import json
import urllib.parse

import requests
import argparse

import os

BASE_URL = "https://openlibrary.org/search/authors.json/"

AUTHOR_STORAGE_LOC = os.path.join(os.getcwd(), "authors")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_name")

    args = parser.parse_args()

    url_name = urllib.parse.quote(args.author_name).lower()

    response = requests.get(BASE_URL + f"?q={url_name}")
    json_response = response.json()

    with open(os.path.join(AUTHOR_STORAGE_LOC, args.author_name + ".json"), 'w', encoding='utf-8') as f:
        json.dump(json_response, f, indent=4)


if __name__ == "__main__":
    main()