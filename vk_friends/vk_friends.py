import requests
import sys


def get_token():
    if len(sys.argv) < 4:
        with open('.vk_token.txt') as file:
            return file.read()
    else:
        return sys.argv[3]


TOKEN = get_token()
user_id_1 = sys.argv[1]
user_id_2 = sys.argv[2]

request_link = 'https://api.vk.com/method/friends.get?'
method = ''

user_link = 'https://vk.com/id'


def get_friends(id):
    params = {
        'access_token': TOKEN.rstrip(),
        'user_id': id
    }
    res = requests.get(request_link, params)
    return res.json()['response']


def compare_friends(user1, user2):
    friends1 = get_friends(user1)
    friends2 = get_friends(user2)
    common_friends = [friend for friend in friends1 if friend in friends2]
    return common_friends


def add_url(id):
    return {
        'id': id,
        'url': user_link + str(id)
    }


common_friends = compare_friends(user_id_1, user_id_2)
common_friends_with_urls = list(map(add_url, common_friends))

for friend in common_friends_with_urls:
    print(friend)
