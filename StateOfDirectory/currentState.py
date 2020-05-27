#!/usr/bin/env python3

import hashlib
import os
from AuthMail.auth import login_bot
import json
import fire


def md5(directory, filename):
    hash_md5 = hashlib.sha1()
    os.chdir(directory)
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class State:

    def __init__(self, directory):
        self.directory = directory

    def sync(self):
        list_of_files = os.listdir(self.directory)
        dict_of_files = {}
        if 'currentState.json' not in list_of_files:
            open(os.path.join(self.directory, 'currentState.json'), "w",
                 encoding="utf-8")
            log = str(self.directory) + '\\currentState.json'
            for el in list_of_files:
                dict_of_files[el] = md5(self.directory, el)
            with open(log, 'w') as write_file:
                json.dump(dict_of_files, write_file)
        else:
            log = str(self.directory) + '\\currentState.json'
            for el in list_of_files:
                if el == 'currentState.json':
                    continue
                dict_of_files[el] = md5(self.directory, el)
            with open(log, 'w') as write_file:
                json.dump(dict_of_files, write_file)

    def diff(self):
        was_change = []
        log = str(self.directory) + '\\currentState.json'
        with open(log, 'r') as read_file:
            dict = json.load(read_file)
        files = os.listdir(self.directory)
        for el in files:
            if el == 'currentState.json':
                continue
            else:
                if dict[el] != md5(self.directory, el):
                    was_change.append(el)
        return was_change

    '''def check_local_coincidence(self):
        auth = Auth('testforpython12', '^cf487z4j#R*pdR')
        list_of_files = []
        for el in os.listdir(self.directory):
            if el == 'currentState.txt':
                continue
            else:
                list_of_files.append(el)
        list_of_files_on_mail = list(auth.login_bot())
        coincidence = set(list_of_files) ^ set(list_of_files_on_mail)
        if str(coincidence) == 'set()':
            print('Nothing change')
        else:
            print(coincidence)'''


