import json
import urllib.parse

import requests
import argparse

BASE_URL = "https://openlibrary.org/search/authors.json/"
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_name")
    parser.add_argument("file_path")

    args = parser.parse_args()

    url_name = urllib.parse.quote(args.author_name).lower()

    response = requests.get(BASE_URL + f"?q={url_name}")
    json_response = response.json()

    with open(args.file_path, 'w', encoding='utf-8') as f:
        json.dump(json_response, f, indent=4)


if __name__ == "__main__":
    main()