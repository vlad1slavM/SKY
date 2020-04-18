import os

list_of_files = os.listdir(f'D:\\test')


def sync():
    log = open('D:\\test\\currentState.txt', 'w', encoding='utf-8')
    for el in list_of_files:
        log.write(str(el) + '\n')
    log.close()


def diff():
    log = []
    file = open('D:\\test\\currentState.txt', 'r',  encoding='utf-8')
    for row in file:
        new_row = row[:-1]
        log.append(new_row)
    result = set(list_of_files) ^ set(log)
    return result
