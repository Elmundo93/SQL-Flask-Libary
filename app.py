from flask import Flask, render_template, request, redirect, url_for, flash
from data_models import db, Author, Book
import os

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'library.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "supersecretkey"

# Ensure the 'data' directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize the database
db.init_app(app)

# Create all tables (run this once; you can comment it out later)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # Retrieve sorting and search query parameters
    sort_by = request.args.get('sort', 'title')
    search_query = request.args.get('q', '')

    query = Book.query.join(Author)

    if search_query:
        # Case-insensitive search on book titles and author names
        query = query.filter(
            Book.title.ilike(f"%{search_query}%") |
            Author.name.ilike(f"%{search_query}%")
        )

    # Apply sorting based on query parameter
    if sort_by == 'title':
        books = query.order_by(Book.title).all()
    elif sort_by == 'author':
        books = query.order_by(Author.name).all()
    else:
        books = query.all()

    return render_template('home.html', books=books, sort_by=sort_by, search_query=search_query)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form.get('name')
        birth_date = request.form.get('birth_date')
        date_of_death = request.form.get('date_of_death')
        if name:
            author = Author(name=name, birth_date=birth_date, date_of_death=date_of_death)
            db.session.add(author)
            db.session.commit()
            flash('Author added successfully!', 'success')
            return redirect(url_for('add_author'))
        else:
            flash('Author name is required', 'error')
    return render_template('add_author.html')


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    authors = Author.query.all()
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        publication_year = request.form.get('publication_year')
        author_id = request.form.get('author_id')
        if title and author_id:
            book = Book(isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)
            db.session.add(book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('add_book'))
        else:
            flash('Book title and author are required', 'error')
    return render_template('add_book.html', authors=authors)


@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    author = book.author
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'success')

    if not author.books:
        db.session.delete(author)
        db.session.commit()
        flash('Author deleted as no books remain', 'success')

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)