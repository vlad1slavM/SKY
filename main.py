#!/usr/bin/env python3
from AuthMail.auth import login_bot, download
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

my_namespace = parser.parse_args()
state = State(my_namespace.direction)


def auth_mail():
    login = str(input("User Name : "))
    password = getpass.getpass()
    return login_bot(login, password)


def sync():
    return state.sync()


def diff():
    state.diff()


def load():
    login = str(input("User Name : "))
    password = getpass.getpass()
    return download(login, password, my_namespace.direction,
                    my_namespace.file)


if my_namespace.action == 'auth':
    auth_mail()
elif my_namespace.action == 'sync':
    sync()
elif my_namespace.action == 'diff':
    diff()
elif my_namespace.action == 'download':
    load()
