class Author:
    """Author with a name and related contracts/books via Contract intermediary."""

    all = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    # name property with validation
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise Exception("name must be a string")
        self._name = value

    # relationship helpers
    def contracts(self):
        """Return all Contract instances for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return unique Book instances for this author via contracts."""
        seen = set()
        result = []
        for c in self.contracts():
            if id(c.book) not in seen:
                seen.add(id(c.book))
                result.append(c.book)
        return result

    def sign_contract(self, book, date, royalties):
        """Create and return a Contract for this author and given book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self) -> int:
        """Sum of royalties across all this author's contracts."""
        return sum(c.royalties for c in self.contracts())


class Book:
    """Book with a title and related contracts/authors via Contract intermediary."""

    all = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    # title property with validation
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str):
            raise Exception("title must be a string")
        self._title = value

    # relationship helpers
    def contracts(self):
        """Return all Contract instances for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return unique Author instances for this book via contracts."""
        seen = set()
        result = []
        for c in self.contracts():
            if id(c.author) not in seen:
                seen.add(id(c.author))
                result.append(c.author)
        return result


class Contract:
    """Contract linking an Author and a Book with date and royalties."""

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author property with validation
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    # book property with validation
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be a Book instance")
        self._book = value

    # date property with validation
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    # royalties property with validation
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an int")
        self._royalties = value

    # class methods
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts that match the given date (preserve creation order)."""
        return [c for c in cls.all if c.date == date]