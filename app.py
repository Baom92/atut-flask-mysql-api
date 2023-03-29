from config import app, app_port
from flask import jsonify, request
from services.services import BookService, AuthorService
from dto.dto import BookData, AuthorData


@app.route('/books', methods=['POST'])
def create_book():
    book_data = BookData(**request.json)
    book = BookService.create(book_data)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict()), 201


@app.route('/books', methods=['GET'])
def get_all_books():
    books = BookService.get_all()
    return jsonify([book.to_dict() for book in books])


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id: int):
    book = BookService.get(book_id)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id: int):
    book_data = BookData(**request.json)
    book = BookService.update(book_id, book_data)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book.to_dict())


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int):
    if BookService.delete(book_id):
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404


@app.route('/authors', methods=['POST'])
def create_author():
    print(request.json)
    author_data = AuthorData(**request.json)
    author = AuthorService.create(author_data)
    return jsonify(author.to_dict()), 201


@app.route('/authors', methods=['GET'])
def get_all_authors():
    authors = AuthorService.get_all()
    return jsonify([author.to_dict() for author in authors])


@app.route('/authors/<int:author_id>', methods=['GET'])
def get_author_by_id(author_id: int):
    author = AuthorService.get(author_id)
    if author is None:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify(author.to_dict())


@app.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    author_data = AuthorData(**request.json)
    author = AuthorService.update(author_id, author_data)
    if author is None:
        return jsonify({'error': 'Author not found'}), 404
    return jsonify(author.to_dict())


@app.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    if AuthorService.delete_author(author_id):
        return jsonify({'message': 'Author deleted'})
    else:
        return jsonify({'error': 'Author not found'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app_port, debug=True)
