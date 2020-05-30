#!/usr/bin/env python3
from AuthMail.auth import login_bot
from StateOfDirectory.currentState import State
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '-lp',
    '--login_password',
    type=str,
    nargs=2,
    help='Введите -lp Логин и Пароль'
)

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

my_namespace = parser.parse_args()
state = State(my_namespace.direction)


def auth_mail():
    print(login_bot(my_namespace.login_password[0],
                    my_namespace.login_password[1]))


def sync():
    return state.sync()


def diff():
    print(state.diff())


if my_namespace.action == 'auth':
    auth_mail()
elif my_namespace.action == 'sync':
    sync()
elif my_namespace.action == 'diff':
    diff()
