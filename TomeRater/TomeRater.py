class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.mail = new_email
        print("user {}'s email has been update to {}".format(
            self.name, new_email))

    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(
            self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for score in self.books.values():
            total += score
        return total / len(self.books)


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("book {}'s isbn has been updated to {}".format(
            self.title, new_isbn))

    def add_rating(self, rating):
        if (0 <= rating and rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        total = 0
        for rate in self.ratings:
            total += rate
        return total / len(self.ratings)

    def __repr__(self):
        return "{}".format(self.title)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_lebel(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level,
                                              self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        try:
            curr_user = self.users[email]
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
            curr_user.read_book(book, rating)
        except KeyError:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email, 0)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        top_rate = None
        top_freq = 0
        for book, freq in self.books.items():
            if freq > top_freq:
                top_freq = freq
                top_rate = book
        return top_rate

    def highest_rated_book(self):
        highest_book = None
        highest_rating = 0
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_book = book
        return highest_book

    def most_positive_user(self):
        highest_user = None
        highest_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_rating = user.get_average_rating()
                highest_user = user
        return highest_user
