#!/usr/bin/env python3
import requests
import re
import os

reqular = re.compile(r'"name": "(.+)"')
reqular_token = re.compile(r'"csrf": "(.+)"')
reqular_hash = re.compile(r'"hash": "(.+)"')


def login_bot(login, password):
    files = []
    files_meta = {}
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
    z = s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
    text = z.text
    result = re.findall(reqular, text)
    hash = re.findall(reqular_hash, text)
    token = re.findall(reqular_token,
                       text)  # Token found right but for now i don`t need it
    for i in range(len(result)):
        if "." in result[i]:
            files.append(result[i])
    for i in range(len(files)):
        files_meta[files[i]] = str(hash[i]).lower()
    return files_meta

#Нужен логин пароль, а так же полная дериктория куда скачать, и имя файла :
#download('testforpython12', '^cf487z4j#R*pdR', r'C:\Users\dlach\Documents\GitHub\SKY', 'test1.txt')


def download(login, password, directory, filename):
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
    url = r'https://cloclo25.cloud.mail.ru/attach/' + filename \
          + r'?x-email=testforpython12%40mail.ru'
    text = s.get(url)
    os.chdir(directory)
    print(os.chdir(directory))
    open(os.path.join(directory, filename), "w",
         encoding="utf-8")
    with open(filename, 'wb') as f:
        for chunk in text.iter_content(chunk_size=1024 * 36):
            if chunk:
                f.write(chunk)
                f.flush()
    text.close()



