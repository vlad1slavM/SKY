#!/usr/bin/env python3
import requests
import re
import json
import os
from StateOfDirectory.currentState import md5
reqular = re.compile(r'"name": "(.+)"')
reqular_token = re.compile(r'"csrf": "(.+)"')
reqular_hash = re.compile(r'"hash": "(.+)"')


def login_bot(login, password):
    s = requests.Session()
    files = []
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
    k = 0
    token = re.findall(reqular_token, text)
    for i in range(len(result)):
        if k == 2:
            files.append(result[i])
        if result[i] == '/':
            k += 1
    files_meta = {}
    for i in range(len(files)):
        files_meta[files[i]] = str(hash[i]).lower()
    return files_meta, token


def download(file):
    '''https://cloclo3.cloud.mail.ru/attach/test.txt?x-email=testforpython12%40mail.ru'''

    link_for_download = r'https://cloclo3.cloud.mail.ru/attach/' + str(file)\
                        + r'?x-email=testforpython12%40mail.ru'

    r = requests.get(url=link_for_download, stream=True)

    with open('1.txt', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 36):
            if chunk:
                f.write(chunk)
                f.flush()
    r.close()


def upload(login, password):
    s = requests.Session()
    r = requests.Session()
    token = login_bot(login, password)[1]
    print(token)
    file = r'C:\Users\dlach\Documents\GitHub\SKY\about.txt'
    hash = md5(r'C:\Users\dlach\Documents\GitHub\SKY', 'about.txt')
    size = os.path.getsize(file)
    s.get('https://cloud.mail.ru/')
    r.get('https://cloud.mail.ru/')
    headers = {
            'hash': str(hash).upper(),
            'size': str(size),
            'api': '2',
            'home': '/about.txt',
            'conflict': 'strict',
            'build': 'cloudweb-10860-70-13-4.202005280922',
            'x-page-id': '',
            'email': str(login),
            'x-email': str(login)}

    data = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'X-CSRF-Token': token[0],
            'Connection': 'keep-alive',
            'Content-Length': '224',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'VID=1YiMVO2tdEHx00000Q0qD4Hx:::3e91a7e-0-0-3a83a10:CAASENwpynP3SixM4f70LUtK0K0aYMETdp33ceZAe2AWz4JxBGn_9tbVlQvzUThxbYolhQMoDM27LSG8eREC9SNRlswYjuyMrqT3_ul4dDnlGGPLCnUq5izkIZ49Jee1JNrGlnNGjRjDH7g0NSAmHYjey_KN8g; _ga=GA1.2.1102720450.1586584001; mrcu=1EBA5E9159C233D1EB12C5DE97C1; p=oJMAAIv/RQAA; tmr_reqNum=96; tmr_lvid=cc1c8e23f0788d150505fdbf0d1f1782; tmr_lvidTS=1586584004864; s=octavius=1|fver=0|ww=1920|wh=944|rt=1|dpr=1.25; i=AQB4otNeBAC7AQgEAQIAAb0HCAQBmRUBSAwFAgEAiQ0FAgHy; b=7EcBAJDj7XEA/qPvhhgAAEAYZ5ZMBn0c51AYq5EFhPMaWUAA; c=qrjTXgEAkHsTAAAUAAQACQAAIMIBnLGmDwAA; searchuid=9823344891586356522; Mpop=1590608318:70797462064055651905000017031f051c054f6c5150445e05190401041d455c434357564b48484459585b0607105956505d1e444d:testforpython12@mail.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAEGzAcA; o=testforpython12@mail.ru:229:Ag==.s; sdcs=aJkMNUPG5c1q3WVr; _ym_uid=1590075035500165857; _ym_d=1590075035; _fbp=fb.1.1590075035813.108013153; OTVET-8088=1; _gid=GA1.2.1155570725.1590927994; tmr_detect=0%7C1590933678298; _gat_gtag_UA_43037165_12=1',
            'Host': 'cloud.mail.ru',
            'Origin': 'https://cloud.mail.ru',
            'Referer': 'https://cloud.mail.ru/home/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'X-Requested-With': 'XMLHttpRequest'}


    '''s.post('https://cloud.mail.ru/api/v1/folder/add', headers=headers,
           data=data)'''
    text1 = s.get('https://cloud.mail.ru/api/v2/file/add', data=data)
    text = r.post('https://cloud.mail.ru/api/v2/file/add', data=data)
    '''text1 = s.post('https://cloud.mail.ru/api/v2/file/add', headers=data,
                   data=headers)'''
    print(text1.headers)


upload('testforpython12', '^cf487z4j#R*pdR')
