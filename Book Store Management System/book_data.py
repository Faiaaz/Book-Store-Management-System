import json
import os

FILE_NAME = "books.json"


def load_books():
    """Load books from a JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_books(books):
    """Save books to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)
