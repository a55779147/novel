# -*- coding: utf-8 -*-
"""
    novel.models
    ------------

    novel website models
    :copyright: (c) 2018-07-20 by buglan
"""

from datetime import datetime

from extensions import db


class User(db.Model):
    """User"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(55))
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, username, passowrd):
        self.username = username
        self.password = passowrd
        self.creat_time = datetime.now()
        self.update_time = datetime.now()

    def __repr__(self):
        return f'<User {self.username}>'

    def __str__(self):
        return f'<User {self.username}>'


class BookRack(db.Model):
    """BookRack"""
    __tablename__ = 'bookrack'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    books = db.relationship('Book', backref='bookrack', lazy='dynamci')

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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    creat_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Book {self.name}>'

    def __str__(self):
        return f'<Book {self.name}>'
