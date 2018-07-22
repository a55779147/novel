# -*- coding: utf-8 -*-
"""
    novel.models
    ------------

    novel website models
    :copyright: (c) 2018-07-20 by buglan
"""

from datetime import datetime

from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """User"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(55))
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    bookracks = db.relationship('BookRack', backref='user', lazy='dynamic')

    def __init__(self, username, passowrd):
        self.username = username
        self.password = passowrd
        self.creat_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return f'<User {self.username}>'

    def __str__(self):
        return f'<User {self.username}>'

    @property
    def password(self):
        raise AttributeError('password is not readable attributer')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class BookRack(db.Model):
    """BookRack"""
    __tablename__ = 'bookrack'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    books = db.relationship('Book', backref='bookrack', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name):
        self.name = name
        self.creat_time = db.Column(db.DateTime)
        self.update_time = db.Column(db.DateTime)

    def __repr__(self):
        return f'<BookRack {self.name}>'

    def __str(self):
        return f'<BookRack {self.name}>'


class Book(db.Model):
    """Book"""
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    bookrack_id = db.Column(db.Integer, db.ForeignKey('bookrack.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Book {self.name}>'

    def __str__(self):
        return f'<Book {self.name}>'
