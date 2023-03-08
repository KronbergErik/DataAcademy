import requests


if __name__ == '__main__':
    r = requests.get("http://127.0.0.1:5000/users")

    users = r.json()

    for user in users['users']:
        print("User id:",user['id'], "User name:", user['name'])