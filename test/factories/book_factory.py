from app import db
from app.models import Book

from faker import Factory
import factory
from factory.alchemy import SQLAlchemyModelFactory

fake = Factory.create()


class BookFactory(SQLAlchemyModelFactory):
    FACTORY_FOR = Book
    FACTORY_SESSION = db.session

    bookname = factory.LazyAttribute(lambda a: fake.word())
    author = factory.LazyAttribute(lambda a: fake.word())
    subject = factory.LazyAttribute(lambda a: fake.word())
    isbn = factory.LazyAttribute(lambda a: fake.word())
    numberavailable = factory.LazyAttribute(lambda a: fake.random_int())
