import random
import string

def generate_random_numbers(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def get_book_data():
    return {
        "title": "Book_" + generate_random_numbers(10),
        "type": "Satire",
        "creation_date": "2021-01-02"
    }
