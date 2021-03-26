#!/usr/bin/env python3
import requests
import re
import os


class Cloud:
    def get_list_and_session(self):
        pass

    def get_files_name(self):
        pass

    def download(self):
        pass


class MailRuCloud(Cloud):
    def __init__(self, login, password, web_directory, directory):
        self.login = login
        self.password = password
        self.web_directory = web_directory
        self.directory = directory
        self.reg_name = re.compile(r'"name": "(.+)"')

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
        result = re.findall(self.reg_name, text)
        return result, s

    @staticmethod
    def clear_trash():
        pass

    def get_files_name(self):
        files = []
        folders = []
        result = MailRuCloud.get_list_and_session(self)[0]
        for i in range(len(result)):
            if result[i] == "default":
                break
            elif "." in result[i]:
                files.append(result[i])
            elif result[i] == "/":
                continue
            else:
                folders.append(result[i])
        s = MailRuCloud.get_list_and_session(self)[1]
        files = set(files)
        directory = {"home/": set(files)}
        for k in range(len(folders)):
            new_files = []
            f = s.get(f'https://cloud.mail.ru/home/{folders[k]}')
            text = f.text
            files_from_folder = re.findall(self.reg_name, text)
            for element in files_from_folder:
                if element == 'default':
                    break
                elif element == '/' or element in new_files \
                        or element in folders:
                    continue
                else:
                    new_files.append(element)
            directory[folders[k]] = new_files
        return directory

    @staticmethod
    def remove_trash(text, files, web_directory, login, s, directory, reg):
        files_from_folder = re.findall(reg, text)
        for element in files_from_folder:
            if element == 'default':
                break
            elif element == '/' or element in files or \
                    element == web_directory or '.' not in element:
                continue
            else:
                """Тут скачиваем файлы."""
                files.append(element)
                url = f'https://cloclo21.cloud.mail.ru/attach/{web_directory}/' \
                      f'{element}?x-email={login}'
                request = s.get(url)
                with open(os.path.join(directory, element),
                          'wb') as file:
                    for chunk in request.iter_content(chunk_size=1024 * 36):
                        if chunk:
                            file.write(chunk)
                            file.flush()
                request.close()

    def download_file(self):
        s = MailRuCloud.get_list_and_session(self)[1]
        url = f'https://cloclo21.cloud.mail.ru/attach/{self.web_directory}/' \
              f'?x-email={self.login}'
        request = s.get(url)
        file_reg = re.compile(r'/(.+)')
        sizing_kilobytes = 1024 * 64
        with open(os.path.join(self.directory, re.findall(file_reg,
                                                          self.web_directory)[0]),
                  'wb') as file:
            for chunk in request.iter_content(chunk_size=sizing_kilobytes):
                if chunk:
                    file.write(chunk)
                    file.flush()
        request.close()

    def download(self):
        if self.web_directory == '/':
            MailRuCloud.download_all_files(self)
        files = []
        s = MailRuCloud.get_list_and_session(self)[1]
        d = s.get(f'https://cloud.mail.ru/home/{self.web_directory}/')
        text = d.text
        MailRuCloud.remove_trash(text, files, self.web_directory,
                                 self.login, s, self.directory, self.reg_name)

    def download_all_files(self):
        files = []
        files_dict = MailRuCloud.get_files_name(self)
        s = MailRuCloud.get_list_and_session(self)[1]
        for i in files_dict.keys():
            if i == 'home/':
                d = s.get(f'https://cloud.mail.ru/home/')
                text = d.text
                MailRuCloud.remove_trash(text, files, '', self.login,
                                         s, self.directory, self.reg_name)
                files = []
            else:
                d = s.get(f'https://cloud.mail.ru/home/{i}')
                text = d.text
                MailRuCloud.remove_trash(text, files, i, self.login,
                                         s, self.directory, self.reg_name)

    def new_download(self):
        reg = re.compile(r'"name": "(.+)",\s+.+\s+.+\s+"kind": "file",\s+.+\s+"home": "(.+)"')
        s = MailRuCloud.get_list_and_session(self)[1]
        d = s.get(f'https://cloud.mail.ru/home/{self.web_directory}/')
        text = d.text
        file_dir = re.findall(reg, text)
        if self.web_directory == '/':
            path = '/'
            pass
        else:
            path = self.web_directory.split('/')
            # directory
            if len(path) == 1:
                pass
            #file
            if len(path) == 2:
                file = path[1]

        print(path)
        print(file_dir)



mail = MailRuCloud('testforpython12', '^cf487z4j#R*pdR', "/",
                   "/home/vladislav/Documents/!GitHub/SKY/down_for_test")
mail.new_download()
