import argparse
import json

def extract_themes(dictionary: dict):
    all_themes = []
    for item in dictionary["docs"]:
        subjects_in_book = item.get("top_subjects")
        if subjects_in_book:
            all_themes.extend(subjects_in_book)

    return all_themes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("author_json_path")
    parser.add_argument("output_path")

    args = parser.parse_args()

    with open(args.author_json_path, "r") as json_data:
        data = json.load(json_data)

    all_themes = extract_themes(data)

    with open(args.output_path, "w") as json_file:
        json.dump({"themes": all_themes}, json_file)

if __name__ == "__main__":
    main()
