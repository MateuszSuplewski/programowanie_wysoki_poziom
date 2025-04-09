from typing import Dict, Optional


class Library:
    def __init__(self, books: Dict[int, str]) -> None:
        self.books = books

    def find_book(self, isbn: int) -> Optional[str]:
        return self.books.get(isbn)


library = Library({9784181067050: "The Magic Tree", 9783883830332: "My Best Friend The Lion"})

print(library.find_book(9784181067050))
print(library.find_book(9783883830332))
print(library.find_book(9780751440491))
