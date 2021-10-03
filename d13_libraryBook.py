from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aisin-aw23@127.0.0.1:3306/library36'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'kljalwer'


db = SQLAlchemy(app)
CSRFProtect(app)

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    books = db.relationship('Book', backref='authors')

    def __repr__(self):
        return 'Author: id->{}, name->{}'.format(self.id, self.name)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))

    def __repr__(self):
        return 'Book: id->{}, name->{}, author_id->{}'.format(self.id, self.name, self.author_id)

db.drop_all()
db.create_all()

author1 = Author(name='金庸')
author2 = Author(name='罗贯中')
db.session.add_all([author1, author2])
db.session.commit()

book1 = Book(name='天龙八部', author_id=author1.id)
book2 = Book(name='神雕侠侣', author_id=author1.id)
book3 = Book(name='三国演义', author_id=author2.id)
db.session.add_all([book1,book2,book3])
db.session.commit()

@app.route('/')
def hello_world():
    authors = Author.query.all()
    return render_template('13_library.html', authors=authors)

@app.route('/add_book',methods=['POST'])
def add_book():
    author_name = request.form.get('author')
    book_name = request.form.get('book')
    if not all([author_name,book_name]):
        flash('作者或者书名不能为空')
        return redirect('/')

    author = Author.query.filter(Author.name==author_name).first()
    if author:
        book = Book.query.filter(Book.name==book_name, Book.author_id==author.id).first()
        if book:
            flash('书名已经存在！')
            return redirect('/')
        else:
            book_tmp = Book(name=book_name, author_id=author.id)
            db.session.add(book_tmp)
            db.session.commit()
    else:
        author_tmp = Author(name=author_name)
        db.session.add(author_tmp)
        db.session.commit()

        book_tmp = Book(name=book_name, author_id=author_tmp.id)
        db.session.add(book_tmp)
        db.session.commit()

    return redirect('/')

@app.route('/delete_book/<int:id>')
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

@app.route('/delete_author/<int:id>')
def delete_author(id):
    author = Author.query.get(id)
    for book in author.books:
        db.session.delete(book)
        # db.session.commit()
    db.session.delete(author)
    db.session.commit()
    return redirect(('/'))


if __name__ == '__main__':
    app.run(debug=True)