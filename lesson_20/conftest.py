from multiprocessing.spawn import import_main_path

import requests
import pytest

@pytest.fixture()
def new_post_id():
    body = {"title": "qqqq",' '"body": "wwww", "userID": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('\ndeleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture()
def num():
    return 1