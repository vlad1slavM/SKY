#!/usr/bin/env python3
import requests
import re
import fire
reqular = re.compile(r'"name": "(.+)"')
reqular_token = re.compile(r'"csrf": "(.+)"')


class Auth:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def login_bot(self):
        s = requests.Session()
        files = []
        s.get('https://cloud.mail.ru/')
        data = {'Login': self.login,
                'Domain': 'mail.ru',
                'Password': self.password,
                'saveauth': '1',
                'new_auth_form': '1',
                'FromAccount': 'opener=account&vk=1&ok=1&twoSteps=1',
                'act_token': '',
                'page': 'https://cloud.mail.ru/?authid=k8v75gff.'
                        '6m&dwhsplit=s6763.a1s3319.n1s&from='
                        'login&from-page=promo&from-promo=blue-2018',
                'lang': 'ru_RU'}

        r = s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
        text = r.text
        print(text)
        result = re.findall(reqular, text)
        k = 0
        token = re.findall(reqular_token, text)
        #print(token)
        for i in range(len(result)):
            if k == 2:
                files.append(result[i])
            if result[i] == '/':
                k += 1
        return files


if __name__ == '__main__':
    fire.Fire(Auth)
