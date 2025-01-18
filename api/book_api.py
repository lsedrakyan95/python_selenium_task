import requests

class BookAPI:

    def __init__(self):
        self.BASE_URL = "http://127.0.0.1:5000/v1/books"

    def get_latest_books(self, limit=1):
        """GET request to fetch the latest books with an optional limit."""
        endpoint = f"{self.BASE_URL}/latest"
        params = {"limit": limit}
        response = requests.get(endpoint, params=params)
        return response

    def get_book_info(self, book_id):
        """GET request to fetch information about a specific book by ID."""
        endpoint = f"{self.BASE_URL}/info"
        params = {"id": book_id}
        response = requests.get(endpoint, params=params)
        return response

    def post_book_manipulation(self, book_data):
        """POST request to manipulate book data."""
        endpoint = f"{self.BASE_URL}/manipulation"
        headers = {"Content-Type": "application/json"}
        response = requests.post(endpoint, json=book_data, headers=headers)
        return response