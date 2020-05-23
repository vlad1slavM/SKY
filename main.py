#!/usr/bin/env python3
import fire
from AuthMail.auth import Auth
from StateOfDirectory.currentState import State


state = State('C:\\Users\\dlach\\Documents\\GitHub\\SKY\\forTest')
auth = Auth('testforpython12', '^cf487z4j#R*pdR')


class Mail:

    def auth_mail(self):
        return auth.login_bot()

    def sync(self):
        return state.sync()

    def diff(self):
        return state.diff()

    def check(self):
        return state.check_local_coincidence()


if __name__ == '__main__':
    fire.Fire(Mail)
#sync('C:\\Users\\dlach\\Documents\\GitHub\\SKY\\forTest')

#check_local_coincidence('C:\\Users\\dlach\\Documents\\GitHub\\SKY\\forTest')

#postFiles('testforpython12', '^cf487z4j#R*pdR')

#state.sync()

#state.diff()
