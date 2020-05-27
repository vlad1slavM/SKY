#!/usr/bin/env python3
import fire
from AuthMail.auth import Auth
from StateOfDirectory.currentState import State
import argparse

state = State('C:\\Users\\dlach\\Documents\\GitHub\\SKY\\forTest')
'''auth = Auth('testforpython12', '^cf487z4j#R*pdR')'''

parser = argparse.ArgumentParser()
parser.add_argument(
    '-lp',
    '--login_password',
    type=str,
    nargs=2,
    help='login_password'
)

parser.add_argument(
    '-d',
    '--direction',
    type=str,
    help='direction '
)

my_namespace = parser.parse_args()

auth = Auth(str(my_namespace.login_password[0]),
            str(my_namespace.login_password[1]))


def auth_mail():
    return auth.login_bot()


def sync():
    return state.sync()


def diff():
    return state.diff()


def check():
    return state.check_local_coincidence()


print(auth_mail())

