def extract_themes(dictionary: dict):
    all_themes = []
    for item in dictionary["docs"]:
        subjects_in_book = item.get("top_subjects")
        if subjects_in_book:
            all_themes.extend(subjects_in_book)

    return all_themes