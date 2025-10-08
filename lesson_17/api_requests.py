import requests



def all_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts') # Для примера
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    print(response[0])
    assert len(response) == 100, 'Not all posts returned'
    print('All posts returned')


def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    print(response)
    # assert response['id'] == post_id


def post_a_post():
    body = {
        "title": "qqqq",
        "body": "wwww",
        "userID": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'Id is incorrect'

def new_post():
    body = {
        "title": "qqqq",
        "body": "wwww",
        "userID": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    return response.json()['id']

def clear(post_id):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


def put_a_put():
    post_id = new_post()
    body = {
        "title": "QQQQQQQQQQQQQQQQQQQQQ",
        "body": "WWWWWWWWWWWWWWWWW",
        "userID": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['title'] == 'qwqwqwqwww'
    clear(post_id)


def patch_a_patch():
    post_id = new_post()

    body = {
        "body": "GGGGGGGGGGGGGGG",
        "userID": 7
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    ).json()
    clear(post_id)


def delete_a_delete():
    post_id = new_post()
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    print(response.json())
    print(response.status_code)

new_post()
# all_posts()
one_post()
# post_a_post()
# put_a_put()
# patch_a_patch()
# delete_a_delete()