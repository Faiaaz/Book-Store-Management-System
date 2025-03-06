from book_data import load_books, save_books

def remove_book():
    """Remove a book by ISBN."""
    books = load_books()
    isbn = input("Enter ISBN to remove: ")
    books = [book for book in books if book['isbn'] != isbn]
    save_books(books)
    print("Book removed successfully!")