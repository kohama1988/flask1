from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aisin-aw23@127.0.0.1:3306/library36'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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


if __name__ == '__main__':
    app.run(debug=True)