import os


def saveToken(access_token):
    with open('token.ini', 'w', encoding='utf-8') as f:
        f.write(access_token)


def getToken():
    with open('token.ini', 'r', encoding='utf-8') as f:
        token = f.readline()
    return token


def tokenExist():
    return os.path.exists("token.ini")
