import requests


def test_edit():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    
    assert response.status_code == 404
