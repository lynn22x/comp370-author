import argparse
import json

import os
AUTHOR_STORAGE_LOC = os.path.join(os.getcwd(), "authors")
THEMES_STORAGE_LOC = os.path.join(os.getcwd(), "themes")


def extract_themes(dictionary: dict):
    all_themes = []
    for item in dictionary["docs"]:
        subjects_in_book = item.get("top_subjects")
        if subjects_in_book:
            all_themes.extend(subjects_in_book)

    return all_themes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_name")

    args = parser.parse_args()

    with open(os.path.join(AUTHOR_STORAGE_LOC, args.author_name + ".json"), "r") as json_data:
        data = json.load(json_data)

    all_themes = extract_themes(data)

    with open(os.path.join(THEMES_STORAGE_LOC, args.author_name + ".json"), "w") as json_file:
        json.dump({"themes": all_themes}, json_file)

if __name__ == "__main__":
    main()
