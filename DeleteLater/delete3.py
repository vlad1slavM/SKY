import re
import requests
from StateOfDirectory.currentState import md5



reqular_cookie = re.compile(r'<Cookie sdcs=(.+) for .cloud.mail.ru/>')
reqular_cookieMpop = re.compile(r'<Cookie Mpop=(.+):testforpython12@mail.ru: for .mail.ru/>')
reqular_token = re.compile(r'"csrf": "(.+)"')





def login_bot(login, password):
    s = requests.Session()
    files = []

    data1 = {'Login': login,
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
    text = s.post('https://auth.mail.ru/cgi-bin/auth', data=data1)
    token = re.findall(reqular_token, text.text)
    url = r'https://cloclo2.cloud.mail.ru/attach/test4.txt?x-email=testforpython12%40mail.ru'
    cookie = s.cookies
    c = s.headers
    print(c)
    cookie1 = re.findall(reqular_cookie, str(cookie))
    url1 = 'https://cloud.mail.ru/api/v2/file/add'
    #hash = md5(r'C:\Users\dlach\Documents\GitHub\SKY', 'ToDo.txt')
    data = {
        'Host': 'cloclo2.cloud.mail.ru',
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64;x64;rv: 76.0) Gecko / 20100101Firefox / 76.0',
        'Accept': 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, * / *;q = 0.8',
        'Accept - Language': 'ru - RU, ru;q = 0.8, en - US;q = 0.5, en; q = 0.3',
        'Accept - Encoding': 'gzip, deflate, br',
        'Connection': 'keep - alive',
        'Upgrade - Insecure - Requests ': '1',
        'Cookie': 'VID=1YiMVO2tdEHx00000Q0qD4Hx:::3f5ff59-0-0-3a83a10'
                  ':CAASEDBoFc1ts8BK5702GkMXKz0aYE9AkN7w_YtR0LM3oSbLb4iZpLRCFZNZFJAslblgjyqt1M2762J6OUTx-Cm-Igr0boYICg49VO4jBzFV4DPMGW8pK1r5LtF4fbXl6QlHNY04QCrvpkVHkyH0VGMqJ8TldA; _ga=GA1.2.1102720450.1586584001; mrcu=1EBA5E9159C233D1EB12C5DE97C1; p=oJMAAIv/RQAA; tmr_reqNum=281; tmr_lvid=cc1c8e23f0788d150505fdbf0d1f1782; tmr_lvidTS=1586584004864; s=octavius=1|fver=0|ww=1534|wh=722|dpr=1.25|rt=1; i=AQCVptteBgATAAgcCRwBAR8BAeoCAVsIAdMJAfEJAYQKAUMLAXseArsBCAQBAgABvQcIBAGZFQEpCQhJGNoCAagDASIEAXkEAYAEAYUEAYkEAYwEAZEEARAFAbYFATEHAawHAbgHAboHAeQHAeoHAe0HAbMIAcgLAckLAcwLAc4LAY0NAUgMBQIBAIkNBQIB+w==; b=8kcAAIDj7XEAKwAAQKDHcQ5DeI0sEMhqZIEA; c=mqbbXgAAAOK/6QERAAQACAcAAAIA; searchuid=9823344891586356522; Mpop=1591453337:7a5f495869456d471905000017031f051c054f6c5150445e05190401041d455c434357564b48484459585b0607105956505d1e444d:testforpython12@mail.ru:; t=obLD1AAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAACAAAEGzAcA; o=testforpython12@mail.ru:233:Ig==.s|:233:AA==.s; sdcs=Wv6Fh7aqDjlr3RJm; _ym_uid=1590075035500165857; _ym_d=1590075035; _fbp=fb.1.1590075035813.108013153; OTVET-8088=1; amplitude_id_bcbcf0f0c3bc8d4102bb913afbc350c0mail.ru=eyJkZXZpY2VJZCI6IjQ1MTQzN2ZlLWJhMGItNDAzOS05ZDY4LTBmZmJiZTNlMDc4NFIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5MTAxNDgzOTg3MCwibGFzdEV2ZW50VGltZSI6MTU5MTAxNDgzOTg3MCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; _gid=GA1.2.1357549169.1591453331; _gat=1; _gat_gtag_UA_43037165_12=1; act=8b8febdcd6b247668e4783ce69ea2d01',
        }
    print(hash)
    print(str(hash).upper())
    head = {
        'x-email': 'testforpython12@mail.ru'}
    text1 = s.get(url, headers=data, data=head)
    print(text1.text)
    print(text1.headers)


login_bot('testforpython12', '^cf487z4j#R*pdR')