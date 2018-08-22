import requests
import sys

limit_cap = 1000
default_user_id = '5030613'


def get_user_id():
    if len(sys.argv) < 2:
        return default_user_id
    else:
        return sys.argv[1]


def get_token():
    if len(sys.argv) < 3:
        with open('.vk_token.txt') as file:
            return file.read()
    else:
        return sys.argv[2]


user_id = get_user_id()
TOKEN = get_token()

user_link = 'https://vk.com/id'
request_friends = 'https://api.vk.com/method/friends.get?'
request_groups = 'https://api.vk.com/method/groups.get?'
request_group_info = 'https://api.vk.com/method/groups.getById?'
request_group_members = 'https://api.vk.com/method/groups.getMembers?'


def remove_stdout_line():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)


def get_friends(id):
    params = {
        'version': '5.74',
        'access_token': TOKEN.rstrip(),
        'user_id': id
    }
    res = requests.get(request_friends, params)
    payload = res.json()
    if 'error' in payload:
        return []
    return payload['response']


def get_groups(id):
    params = {
        'version': '5.61',
        'access_token': TOKEN.rstrip(),
        'user_id': id
    }
    res = requests.get(request_groups, params)
    payload = res.json()
    if 'error' in payload:
        return []
    return payload['response']


def get_friends_groups(id):
    friends = get_friends(user_id)
    friends_groups = set()
    print('Start processing friends')
    for i, friend in enumerate(friends):
        # Stop loop it limit reached
        if i > limit_cap:
            break
        # Log progress
        line = 'Processing friend: ' + str(i) + ' of ' + str(len(friends)) + '. Unique groups gathered: ' + str(len(friends_groups))
        remove_stdout_line()
        print(line)
        groups = get_groups(friend)
        for group in groups:
            friends_groups.add(group)
    return friends_groups


def get_group_members_count(id):
    params = {
        'version': '5.74',
        'access_token': TOKEN.rstrip(),
        'group_id': id,
    }
    res = requests.get(request_group_members, params)
    payload = res.json()
    if 'error' in payload:
        return []
    return payload['response']['count']


def create_group_info(id):
    params = {
        'version': '5.61',
        'access_token': TOKEN.rstrip(),
        'group_id': id,
        'fields': 'name',
    }
    res = requests.get(request_group_info, params)
    payload = res.json()
    if 'error' in payload:
        return False
    return {
        'name': payload['response'][0]['name'],
        'gid': id,
        'members_count': get_group_members_count(id),
    }


def find_unique_user_groups(id):
    user_groups = get_groups(id)
    print('User\'s groups found: ', len(user_groups))

    friends_groups = get_friends_groups(id)
    print('Friend\'s groups found: ', len(friends_groups))

    set(user_groups).difference_update(friends_groups)
    print('Unique user\'s groups found: ', len(user_groups))

    result = []
    print('Start processing friends')
    for i, group in enumerate(user_groups):
        # Log progress
        line = 'Processing group data: ' + str(i) + ' of ' + str(len(user_groups))
        remove_stdout_line()
        print(line)
        group_to_add = create_group_info(group)
        if group_to_add is False:
            continue
        result.append(group_to_add)

    print(result)


find_unique_user_groups(user_id)
