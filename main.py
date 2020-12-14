#!/usr/bin/env python3
from AuthMail.auth import CloudMail
from StateOfDirectory.currentState import State
import argparse
import getpass

parser = argparse.ArgumentParser()

parser.add_argument(
    '-d',
    '--direction',
    type=str,
    help='Введите -d директория, с которой вы будете работать '
)

parser.add_argument('-a',
                    '--action',
                    type=str,
                    help='Выберите функцию которую хотите вызвать'
                    )

parser.add_argument('-f',
                    '--file',
                    type=str,
                    help='Введите название файла, который хотите скачать'
                    )

parser.add_argument('-w',
                    '--web',
                    type=str,
                    help='Выберите директорию, которую хотите скачать из облака'
                    )

my_namespace = parser.parse_args()
state = State(my_namespace.direction)


def auth_mail():
    login = str(input("User Name : "))
    password = getpass.getpass()
    mail = CloudMail(login, password, "", "")
    return mail.get_files_name()


def sync():
    return state.sync()


def diff():
    state.diff()


def load():
    login = str(input("User Name : "))
    password = getpass.getpass()
    mail = CloudMail(login, password, my_namespace.web, my_namespace.direction)
    return mail.download()


if my_namespace.action == 'files':
    auth_mail()
elif my_namespace.action == 'sync':
    sync()
elif my_namespace.action == 'diff':
    diff()
elif my_namespace.action == 'download':
    load()
