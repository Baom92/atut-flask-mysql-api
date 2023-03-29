from config import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='author', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "books": self.books
        }


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(1000))
    note = db.Column(db.Float())
    price = db.Column(db.Float(), nullable=False)
    publication_date = db.Column(db.Date(), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "summary": self.summary,
            "note": self.note,
            "price": self.price,
            "publication_date": self.publication_date,
            "category": self.category,
            "author_id": self.author_id
        }
