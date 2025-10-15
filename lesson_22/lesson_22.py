# Нагрузочное тестирование

import requests
from datetime import datetime

start = datetime.now()
url = f='http://172.16.3.87:7070/api/common/auth'
payload = {'login': 0, 'password': 321}
response = requests.post(url, json=payload)
# print(response)
end = datetime.now()
print(end - start)