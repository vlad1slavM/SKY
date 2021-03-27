#!/usr/bin/env python3
import requests
import re
import os


class DropBoxCloud:
    pass


class MailRuCloud:
    def __init__(self, login, password, web_directory, directory):
        self.login = login
        self.password = password
        self.web_directory = web_directory
        self.directory = directory
        self.reg_name = re.compile(r'"name": "(.+)"')
        self.reg_name_dir = re.compile(r'"name": "(.+)",\s+.+\s+.+\s+"kind": "file",\s+.+\s+"home": "(.+)"')
        self.reg_dir = re.compile(r'"name": "(.+)",\s+.+\s+.+\s+"kind": "folder"')

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
        if z.headers['Connection'] == 'keep-alive':
            text = z.text
            result = re.findall(self.reg_name, text)
            return result, s
        else:
            print(f'Incorrect password or login')

    def get_files_name(self):
        s = MailRuCloud.get_list_and_session(self)[1]
        d = s.get(f'https://cloud.mail.ru/home/{self.web_directory}/')
        text = d.text
        file_dir = re.findall(self.reg_name_dir, text)
        file_dir = file_dir[:int(len(file_dir) / 2)]
        files = []
        for el in file_dir:
            files.append(el[0])
        return files

    def get_files(self, s,  web_directory):
        d = s.get(f'https://cloud.mail.ru/home/{web_directory}/')
        text = d.text
        file_dir = re.findall(self.reg_name_dir, text)
        file_dir = file_dir[:int(len(file_dir) / 2)]
        return file_dir, text

    def download(self):
        s = MailRuCloud.get_list_and_session(self)[1]
        file_dir = MailRuCloud.get_files(self, s, self.web_directory)[0]
        text = MailRuCloud.get_files(self, s, self.web_directory)[1]
        is_alone_file = False
        if self.web_directory == '/':
            directories = set(re.findall(self.reg_dir, text))
            for dir in directories:
                files = MailRuCloud.get_files(self, s, dir)[0]
                for file in files:
                    file_dir.append(file)

        else:
            path = self.web_directory.split('/')
            if len(path) == 2:
                for file in file_dir:
                    if file[0] == path[1]:
                        file_dir = file
                        is_alone_file = True
                        break
        if is_alone_file:
            MailRuCloud.real_download(self, s, file_dir[1], file_dir[0])
            print(f'{file_dir[0]} was download :)')
        else:
            for file in file_dir:
                MailRuCloud.real_download(self, s, file[1], file[0])
                print(f'{file[0]} was download :)')

    def real_download(self, s, web_directory, file_name):
        url = f'https://cloclo21.cloud.mail.ru/attach{web_directory}/' \
              f'?x-email={self.login}'
        request = s.get(url)
        sizing_kilobytes = 1024 * 64
        with open(os.path.join(self.directory, file_name), 'wb') as file:
            for chunk in request.iter_content(chunk_size=sizing_kilobytes):
                if chunk:
                    file.write(chunk)
                    file.flush()
        request.close()


if __name__ == '__main__':
    mail = MailRuCloud('testforpython12', '^cf487z4j#R*pdR', "/",
                       "/home/vladislav/Documents/!GitHub/SKY/down_for_test")
    mail.download()
