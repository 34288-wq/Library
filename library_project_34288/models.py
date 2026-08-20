from dataclasses import dataclass

@dataclass
class Book:
    book_id: str
    title: str
    author: str
    category: str
    status: str = "available"

@dataclass
class Member:
    member_id: str
    name: str
    classroom: str
    phone: str = ""