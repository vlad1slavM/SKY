#!/usr/bin/env python3
import hashlib
import os
import json


def get_files(directory):
    dir_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            dir_files.append(filename)
    return dir_files


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
        list_of_files = get_files(self.directory)
        files = []
        with open(os.path.join(self.directory, 'currentState.json'), "w",
                  encoding="utf-8") as log:
            for el in list_of_files:
                files.append(el)
            json.dump(files, log)

    def diff(self):
        list_of_files = get_files(self.directory)
        files = []
        dict_different = {'DELETE': [], 'NEW': []}
        for i in range(len(list_of_files)):
            if list_of_files[i] == 'currentState.json':
                continue
            else:
                files.append(list_of_files[i])
        with open(os.path.join(self.directory, 'currentState.json'), "r",
                  encoding="utf-8") as log:
            files_from_json = json.load(log)
        was_delete = set(files_from_json) - set(files)
        new_files = set(files) - set(files_from_json)
        dict_different['DELETE'] = was_delete
        dict_different['NEW'] = new_files
        print(dict_different)

