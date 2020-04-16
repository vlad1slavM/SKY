import requests
import re


reqular = re.compile(r'"name": ".+"')

def loginbot(login, password):
    s = requests.Session()
    s.get('https://cloud.mail.ru/')

    data = {'Login': login,
            'Domain': 'mail.ru',
            'Password': password,
            'saveauth': '1',
            'new_auth_form': '1',
            'FromAccount': 'opener=account&vk=1&ok=1&twoSteps=1',
            'act_token': '',
            'page': 'https://cloud.mail.ru/?authid=k8v75gff.6m&dwhsplit=s6763.a1s3319.n1s&from=login&from-page=promo&from-promo=blue-2018',
            'lang': 'ru_RU'}

    r = s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
    text = r.text

    return re.findall(reqular, text)