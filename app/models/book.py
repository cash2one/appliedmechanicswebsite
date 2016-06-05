from .. import db
from . import CRUDMixin
import flask.ext.whooshalchemy

class Book(db.Model, CRUDMixin):
    __searchable__ = ['id', 'bookname', 'author', 'subject', 'isbn', 'numberavailable']  # these fields will be indexed by whoosh
    id = db.Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(100))
    author = db.Column(db.String(100))
    subject = db.Column(db.String(50))
    isbn = db.Column(db.String(20))
    numberavailable = db.Column(db.Integer)
