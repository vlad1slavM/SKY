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


class State:

    def __init__(self, directory):
        self.directory = directory

    def sync(self):
        list_of_files = get_files(self.directory)
        files = []
        dict_files = {"files": []}
        current_state_file = os.path.join(self.directory, 'currentState.json')
        with open(current_state_file, "w",
                  encoding="utf-8") as log:
            for el in list_of_files:
                if el != 'currentState.json':
                    files.append(el)
            dict_files["files"] = files
            json.dump(dict_files, log)

    def diff(self):
        list_of_files = get_files(self.directory)
        files = []

        for i in range(len(list_of_files)):
            if list_of_files[i] != 'currentState.json':
                files.append(list_of_files[i])
        with open(os.path.join(self.directory, 'currentState.json'), "r",
                  encoding="utf-8") as log:
            files_from_json = json.load(log)
        dict_different = {'DELETE': set(files_from_json) - set(files),
                          'NEW': set(files) - set(files_from_json)}
        return dict_different

