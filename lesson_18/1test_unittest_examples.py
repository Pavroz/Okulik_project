import unittest
import requests
import sys



class TestPostApi(unittest.TestCase):

    def setUp(self):
        body = {"title": "qqqq", "body": "wwww", "userID": 1}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')

    @unittest.skip('skip')
    def test_get_one_post(self):
        print('Test 1')
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'] == 100, self.post_id)


class TestIndependent(unittest.TestCase):

    @unittest.skipIf(sys.platform == 'win32', 'Windows')
    def test_get_all_posts(self):
        print('Test 2')
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
        print('Test 3')
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)
