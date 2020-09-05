import requests
import json
import re
from StateOfDirectory.currentState import md5
reqular_cookie = re.compile(r'<Cookie sdcs=(.+) for .cloud.mail.ru/>')
reqular_cookieMpop = re.compile(r'<Cookie Mpop=(.+):testforpython12@mail.ru: for .mail.ru/>')
reqular_token = re.compile(r'"csrf": "(.+)"')
'''
<Cookie sdcs=BOHSf1CLM54A2oti for .cloud.mail.ru/>
<Cookie sdcs=reqpFIJR4Qh9AcNj for .cloud.mail.ru/>
<Cookie Mpop=1591109991:5d505f77595d520f1905000017031f051c054f6c5150445e05190401041d455c434357564b48484459585b0607105956505d1e444d:testforpython12@mail.ru: for .mail.ru/>
'''


def login_bot(login, password):
    s = requests.Session()
    files = []

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
    s.get('https://auth.mail.ru/cgi-bin/auth')
    text = s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
    token = re.findall(reqular_token, text.text)
    url = r'https://cloclo3.cloud.mail.ru/attach/test.txt?x-email=testforpython12%40mail.ru'
    cookie = s.cookies
    c = s.headers
    print(c)
    cookie1 = re.findall(reqular_cookie, str(cookie))
    url1 = 'https://cloud.mail.ru/api/v2/file/add'
    hash = md5(r'C:\Users\dlach\Documents\GitHub\SKY', 'ToDo.txt')
    data = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-CSRF-Token': token[0],
        'Connection': 'keep-alive',
        'Content-Length': '224',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'VID=1YiMVO2tdEHx00000Q0qD4Hx:::3f0c7cd-0-0-3a83a10:CAASEDW4qfBwHubGVOfMcsvETCIaYJjMyFL4aBlK2AtkSIiglfbF2KHjoU6_gM_PSK6ZFiPzcO3ImhV3-1Z6l97k6ubEzgaR9TfPaOMpBeKnYGQVvbQFxNqbaCiuckcX9E0VDdTAm7ibBuD5MKe53Rm9DrHl8A; _ga=GA1.2.1102720450.1586584001; mrcu=1EBA5E9159C233D1EB12C5DE97C1; p=oJMAAIv/RQAA; tmr_reqNum=220; tmr_lvid=cc1c8e23f0788d150505fdbf0d1f1782; tmr_lvidTS=1586584004864; s=octavius=1|fver=0|ww=1534|wh=722; i=AQBqXtZeBgATAAgcCRwBAR8BAeoCAVsIAdMJAfEJAYQKAUMLAXseArsBCAQBAgABvQcIBAGZFQEpCQhJGNoCAagDASIEAXkEAYAEAYUEAYkEAYwEAZEEARAFAbYFATEHAawHAbgHAboHAeQHAeoHAe0HAbMIAcgLAckLAcwLAc4LAY0NAUgMBQIBAIkNBQIB/w==; b=7kcAAJDj7XEALwAAgBDOLJkM+DjOoRBWIwsI5TWygAAA; c=Dm/WXgAAAOK/6QERAAQACAcAAAIA; searchuid=9823344891586356522; Mpop=1591111437:7c5a7e01405f00071905000017031f051c054f6c5150445e05190401041d455c434357564b48484459585b0607105956505d1e444d:testforpython12@mail.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAEGzAcA; o=testforpython12@mail.ru:233:Ig==.s|:233:AA==.s; sdcs=NuiLzcyOS8b1EDfC; _ym_uid=1590075035500165857; _ym_d=1590075035; _fbp=fb.1.1590075035813.108013153; OTVET-8088=1; _gid=GA1.2.1155570725.1590927994; tmr_detect=0%7C1591111441304; amplitude_id_bcbcf0f0c3bc8d4102bb913afbc350c0mail.ru=eyJkZXZpY2VJZCI6IjQ1MTQzN2ZlLWJhMGItNDAzOS05ZDY4LTBmZmJiZTNlMDc4NFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MTAxNDgzOTg3MCwibGFzdEV2ZW50VGltZSI6MTU5MTAxNDgzOTg3MCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; act=bc42dc813023415ba6ddc351bd0c6649; _gat_gtag_UA_43037165_12=1',
        'Host': 'cloud.mail.ru',
        'Origin': 'https://cloud.mail.ru',
        'Referer': 'https://cloud.mail.ru/home/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        'X-Requested-With': 'XMLHttpRequest'}
    print(hash)
    print(str(hash).upper())
    head = {
        'hash': '37F3F0A7012F54A68EE8D639C58AA49F92B4FCD4',
        'size': 1104,
        'api': '2',
        'home': '/ToDo+(1).txt',
        'conflict': 'strict',
        'build': 'cloudweb-10860-70-13-4.202005280922',
        'x-page-id': 'Y9kk1GyzI9',
        'email': 'testforpython12@mail.ru',
        'x-email': 'testforpython12@mail.ru'}
    '''text1 = s.post(url1, headers=data, data=head)
    print(cookie)
    print(text1.text)
    print(text1.headers)'''


login_bot('testforpython12', '^cf487z4j#R*pdR')
s = '37F3F0A7012F54A68EE8D639C58AA49F92B4FCD4'
print(s.lower())