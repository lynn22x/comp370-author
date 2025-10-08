import urllib.parse

import requests
import argparse

BASE_URL = "https://openlibrary.org/search/authors.json/"
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_name")

    args = parser.parse_args()

    url_name = urllib.parse.quote(args.author_name).lower()

    response = requests.get(BASE_URL + f"?q={url_name}")

    print(response.json())
    return response.json()

if __name__ == "__main__":
    main()