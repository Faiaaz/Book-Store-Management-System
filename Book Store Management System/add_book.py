from book_data import load_books, save_books


def get_book_input():
    """Get book details from user input."""
    isbn = input("Enter ISBN/Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    return {"isbn": isbn, "title": title, "author": author, "genre": genre, "price": price, "quantity": quantity}


def add_book():
    """Add a new book to the store."""
    books = load_books()
    new_book = get_book_input()
    if any(book['isbn'] == new_book['isbn'] for book in books):
        print("Book with this ISBN already exists!")
        return
    books.append(new_book)
    save_books(books)
    print("Book added successfully!")
