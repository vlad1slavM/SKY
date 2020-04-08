import requests

def loginbot(login, password):
    s = requests.Session()

    s.get(f'https: // yandex.ru')

    data = {'csrf_token': 'dbb90c302db0dbce37c706ea87f3581077c8bb4a:1586357248483',
            'login': login,
            'process_uuid': '4c961af1-6cb2-4ca0-9cdf-e6225badbe2d',
            'retpath': 'https://disk.yandex.ru?source=landing2_signin_ru',
            'origin': 'disk_landing2_signin_ru',
            'service': 'cloud'
            }
