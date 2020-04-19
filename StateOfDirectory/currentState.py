#!/usr/bin/env python3
import hashlib
import os


def sync(directory):
    list_of_files = os.listdir(directory)
    dictOfFiles = {}
    if 'currentState.txt' not in list_of_files:
        open(os.path.join(directory, 'currentState.txt'), "w", encoding="utf-8")
        log = open(directory + '\\currentState.txt', 'w', encoding='utf-8')
        for el in list_of_files:
            dictOfFiles[el] = hashlib.md5(el.encode('utf-8')).hexdigest()
        log.write(str(dictOfFiles))
        log.close()
    else:
        log = open(directory + '\\currentState.txt', 'w', encoding='utf-8')
        for el in list_of_files:
            dictOfFiles[el] = hashlib.md5(el.encode('utf-8')).hexdigest()
        log.write(str(dictOfFiles))
        log.close()
    log = open(directory + '\\currentState.txt', 'r', encoding='utf-8')
    return log.read()


def diff(directory):
    log = []
    list_of_files = os.listdir(directory)
    file = open(directory + '\\currentState.txt', 'r',  encoding='utf-8')
    for row in file:
        new_row = row[:-1]
        log.append(new_row)
    result = set(list_of_files) ^ set(log)
    return result
