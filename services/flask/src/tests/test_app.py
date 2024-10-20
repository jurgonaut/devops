import requests


URL = "http://localhost:5000/"


class TestAll():
    def test_get_books(self):
        response = requests.get(URL)
        assert response.status_code == 200

    def test_create_book(self):
        data = {"title": "test-tile", "author": "test-author", "pages_num": 100, "review": "test-review"}
        response = requests.post(f"{URL}/create/", data=data)
        assert response.status_code == 200

    def test_delete(self):
        data = {"title": "test-tile", "author": "test-author"}
        response = requests.post(f"{URL}/delete/", data=data)
        assert response.status_code == 200
