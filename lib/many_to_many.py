class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []  # List to store contracts associated with the author

    def add_contract(self, contract):
        """Adds a contract to the author's list of contracts"""
        self._contracts.append(contract)

    def contracts(self):
        """Returns a list of contracts associated with the author"""
        return self._contracts

    def books(self):
        """Returns a list of books the author has contracts for"""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates a contract for the author and the given book"""
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        """Returns the sum of all royalties from the author's contracts"""
        return sum(contract.royalties for contract in self._contracts)

    pass


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  # List to store contracts associated with the book

    def add_contract(self, contract):
        """Adds a contract to the book's list of contracts"""
        self._contracts.append(contract)

    def contracts(self):
        """Returns a list of contracts associated with the book"""
        return self._contracts

    def authors(self):
        """Returns a list of authors that have contracts for this book"""
        return [contract.author for contract in self._contracts]


    pass


class Contract:
    all = []  # This is the list storing all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        self.author.add_contract(self)
        self.book.add_contract(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts filtered by date."""
        return [contract for contract in cls.all if contract.date == date]
    pass


