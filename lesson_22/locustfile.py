from locust import task, HttpUser
import requests

class MemeUser(HttpUser):
    url = None
    payload = None
    @task
    def get_auth_token(self):
        self.url = '/common/auth' # хост в locust - http://172.16.3.87:7070/api
        self.payload = {'login': 0, 'password': 321}
        response = self.client.get(self.url, json=self.payload)
        return response.text

    @task
    def get_list_profiles(self):
        url = '/profiles' # хост в locust - http://172.16.3.87:7070/api
        token = self.get_auth_token()
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        return response