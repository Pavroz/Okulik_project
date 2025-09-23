import random
import sys

print(sys.platform)

print(random.random())
print(int(random.random() * 100))
print(random.randint(0 ,100))
print(random.randrange(0,100, 2))

users = ['user1', 'user2', 'user3']
print(random.choice(users))