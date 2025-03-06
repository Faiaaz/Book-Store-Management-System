from book_data import load_books


def search_books():
    """Search for books by title, author, or genre."""
    books = load_books()
    if not books:
        print("No books available to search.")
        return

    keyword = input("Enter title, author, or genre to search: ").lower()
    results = [book for book in books if
               keyword in book['title'].lower() or keyword in book['author'].lower() or keyword in book[
                   'genre'].lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            print(
                f"ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Price: {book['price']}, Quantity: {book['quantity']}")
    else:
        print("No matching books found.")