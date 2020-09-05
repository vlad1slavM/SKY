import requests

s = requests.Session()
s.get('https://mcskill.ru/')

data = {'username': 'mclogs',
        'password': 'sp9dcLK_GEzJ4uF'}
headers = {'authority': 'mcskill.ru',
                'method': 'POST',
                'path': '/',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'max-age=0',
                # contecn lenght
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarypVXGAxgWvaIMpWVg',
                'origin': 'https://mcskill.ru',
                'referer': 'https://mcskill.ru/',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

data1 = {'username': 'mclogs',
            'password': 'sp9dcLK_GEzJ4uF',
            'submit': '',
            'login': 'submit'}
kk = s.post('https://mcskill.ru/?page=start', data=data1, headers=headers)
kk.encoding = 'latin-1'
print(kk.text)
