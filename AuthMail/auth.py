#!/usr/bin/env python3
import requests
import re
import os


class Regulars:
    name = re.compile(r'"name": "(.+)"')
    token = re.compile(r'"csrf": "(.+)"')
    hash = re.compile(r'"hash": "(.+)"')


class CloudMail:
    def __init__(self, login, password, web_directory, directory):
        self.login = login
        self.password = password
        self.web_directory = web_directory
        self.directory = directory

    def get_list_and_session(self):
        s = requests.Session()
        s.get(f'https://cloud.mail.ru/')
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
        z = s.post('https://auth.mail.ru/cgi-bin/auth', data=data)
        text = z.text
        with open(os.path.join('text.txt'), 'w', encoding='UTF-8') as file:
            file.write(text)
        result = re.findall(Regulars.name, text)
        return result, s

    def get_files_name(self):
        files = []
        folders = []
        result = CloudMail.get_list_and_session(self)[0]
        for i in range(len(result)):
            if result[i] == "default":
                break
            elif "." in result[i]:
                files.append(result[i])
            elif result[i] == "/":
                continue
            else:
                folders.append(result[i])
        s = CloudMail.get_list_and_session(self)[1]
        files = set(files)
        directory = {"home/": set(files)}
        for k in range(len(folders)):
            new_files = []
            f = s.get(f'https://cloud.mail.ru/home/{folders[k]}')
            text = f.text
            files_from_folder = re.findall(Regulars.name, text)
            for j in range(len(files_from_folder)):
                if files_from_folder[j] == 'default':
                    break
                elif files_from_folder[j] == '/':
                    continue
                elif files_from_folder[j] in new_files:
                    continue
                elif files_from_folder[j] in folders:
                    continue
                else:
                    new_files.append(files_from_folder[j])
            directory[folders[k]] = new_files
        return directory

    @staticmethod
    def remove_trash(text, files, web_directory, login, s, directory):
        files_from_folder = re.findall(Regulars.name, text)
        for i in range(len(files_from_folder)):
            if files_from_folder[i] == 'default':
                break
            elif files_from_folder[i] == '/':
                continue
            elif files_from_folder[i] in files:
                continue
            elif files_from_folder[i] == web_directory:
                continue
            elif '.' not in files_from_folder[i]:
                continue
            else:
                """Тут скачиваем файлы."""
                files.append(files_from_folder[i])
                url = f'https://cloclo25.cloud.mail.ru/attach/{web_directory}/' \
                      f'{files_from_folder[i]}?x-email={login}'
                request = s.get(url)
                with open(os.path.join(directory, files_from_folder[i]),  'wb') as file:
                    for chunk in request.iter_content(chunk_size=1024 * 36):
                        if chunk:
                            file.write(chunk)
                            file.flush()
                request.close()

    def download(self):
        if self.web_directory == '/':
            CloudMail.download_all_files(self)
        files = []
        s = CloudMail.get_list_and_session(self)[1]
        d = s.get(f'https://cloud.mail.ru/home/{self.web_directory}')
        text = d.text
        CloudMail.remove_trash(text, files, self.web_directory,
                               self.login, s, self.directory)

    def download_all_files(self):
        files = []
        files_dict = CloudMail.get_files_name(self)
        s = CloudMail.get_list_and_session(self)[1]
        for i in files_dict.keys():
            if i == 'home/':
                d = s.get(f'https://cloud.mail.ru/home/')
                text = d.text
                CloudMail.remove_trash(text, files, '', self.login,
                                       s, self.directory)
                files = []
            else:
                d = s.get(f'https://cloud.mail.ru/home/{i}')
                text = d.text
                CloudMail.remove_trash(text, files, i, self.login,
                                       s, self.directory)


