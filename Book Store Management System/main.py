
from add_book import add_book
from view_books import view_books
from search_books import search_books
from remove_book import remove_book
from utils import display_menu
def main():
    """Main menu for the CLI application."""
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
