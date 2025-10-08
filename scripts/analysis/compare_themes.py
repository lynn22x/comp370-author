import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("theme_file_1")
    parser.add_argument("theme_file_2")

    args = parser.parse_args()
