from book_data import load_books


def view_books():
    """Display all books in the store."""
    books = load_books()
    if not books:
        print("No books available.")
        return
    print("\nBooks in Store:")
    for book in books:
        print(
            f"ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
