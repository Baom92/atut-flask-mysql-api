# -*- coding: utf-8 -*-

from datetime import date
from dataclasses import dataclass


@dataclass
class AuthorData:
    firstname: str
    lastname: str


@dataclass
class BookData:
    title: str
    summary: str
    note: float
    price: float
    publication_date: date
    category: str
    author_id: int
    #author: AuthorData
