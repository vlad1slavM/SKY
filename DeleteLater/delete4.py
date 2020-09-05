import requests
import re
import json
import os
reqular = re.compile(r'"name": "(.+)"')
reqular_token = re.compile(r'"csrf": "(.+)"')
reqular_hash = re.compile(r'"hash": "(.+)"')

directory = os.path.abspath(r'forTest')
file = str(directory) + '\\123.txt'
print(directory + '\n' + file)


def login_bot(login, password):
    s = requests.Session()
    s.get('https://cloud.mail.ru/')
    data = {'Login': login,
            'Domain': 'mail.ru',
            'Password': password,
            'saveauth': '1',
            'new_auth_form': '1',
            'FromAccount': 'opener=account&vk=1&ok=1&twoSteps=1',
            'act_token': '',
            'page': 'https://cloud.mail.ru/?authid=k8v75gff.'
                    '6m&dwhsplit=s6763.a1s3319.n1s&from='
                    'login&from-page=promo&from-promo=blue-2018',
            'lang': 'ru_RU'}
    s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
    text = s.get('https://cloclo25.cloud.mail.ru/attach/test3.txt?x-email=testforpython12%40mail.ru')
    os.chdir(directory)
    open(os.path.join(directory, '123.txt'), "w",
         encoding="utf-8")
    with open(file, 'wb') as f:
        for chunk in text.iter_content(chunk_size=1024 * 36):
            if chunk:
                f.write(chunk)
                f.flush()
    text.close()
# Получаю содержимое


login_bot('testforpython12', '^cf487z4j#R*pdR')