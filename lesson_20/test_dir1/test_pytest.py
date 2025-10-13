import requests
import pytest
import time
import allure


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

@pytest.fixture(scope='session')
def hello():
    print('\nHello')
    yield None
    print('\nBye')

# @pytest.mark.skip('No precondition') # Для пропуска теста
@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.smoke
def test_get_one_post(new_post_id, hello):
    print('Test 1')
    with allure.step(f'Run get request for post with id {new_post_id}'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    # assert response['id'] == 100 == new_post_id
    with allure.step(f'Check that post id is {new_post_id}'):
        assert response == {11}

@allure.feature('Posts')
@allure.story('Get posts')
@pytest.mark.smoke
def test_get_all_posts():
    print('Test 2')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

@allure.feature('Posts')
@allure.story('Manipulate posts')
@pytest.mark.regression
def test_add_post():
    print('Test 3')
    with allure.step('Prepare test data'):
        body = {
            "title": "qqqq",
            "body": "wwww",
            "userID": 1
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to create a post'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
    with allure.step('Check response code is 201'):
        assert response.status_code == 201
    with allure.step('Check id of create post is 101'):
        assert response.json()['id'] == 101

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.regression
def test_one():
    # time.sleep(3)
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
@pytest.mark.parametrize('logins', ['', '  ', '!@#$%^&*()'])
def test_two(logins):
    print(logins)
    # time.sleep(3)
    assert 1 == 1

@allure.feature('Example')
@allure.story('Equals')
def test_three():
    # time.sleep(3)
    assert 1 == 1