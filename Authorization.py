import base64
import requests


class Authorization:
    def authorization_esmtr(self):
        params = {'username': 'auvin', 'password': '111'}
        auth = requests.get('https://esmtr24.sdi-solution.ru/ws/token', params=params).json()
        return 'Bearer ' + auth['token']

    def authorization_adapter(self):
        username = 1
        password = 1
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return encoded_credentials