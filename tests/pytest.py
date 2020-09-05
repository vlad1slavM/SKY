import unittest
from AuthMail.auth import login_bot
from StateOfDirectory.currentState import State, md5
import json
import os
import hashlib

directory = os.path.abspath(r'../forTest1')
state = State(directory)
state_2 = State(os.path.abspath(r'../forTest2'))


def sha1(filename):
    hash_md5 = hashlib.sha1()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class TestGetFiles(unittest.TestCase):
    def test_auth(self):
        answer = {
            'Берег.jpg': '9101ab34f2348576ee9225aecf4dc17674d1eb17',
            'Горное озеро.jpg': 'fc2bfebbf99e1b9518bed1e3b0fdbcf934276a4a',
            'Долина реки.jpg': 'f6efa34bffd20a300f440b9c88245da048deee89',
            'На отдыхе.jpg': '1d1ec8cbb4a1128148108d5932ec76c42256f543',
            'Полет.mp4': 'c2ad142bdf1e4f9fd50e06026bca578198bfc36e',
            'Чистая вода.jpg': '8b57d61b651f8af2696e756cb310f320dc7838b9'}
        self.assertEqual(login_bot('testforpython13@mail.ru',
                                   'R&ft3OKEprs1'), answer)

    def test_sync(self):
        answer = "{'1.txt': '356a192b7913b04c54574d18c28d46e6395428ab'," \
                 " '2.txt': 'da4b9237bacccdf19c0760cab7aec4a8359010b0'," \
                 " '3.txt': '77de68daecd823babbb58edb1c8e14d7106e83bb'," \
                 " '4.txt': '1b6453892473a467d07372d45eb05abc2031647a'}"
        state.sync()
        with open(r'currentState.json', 'r') as read_file:
            dict = json.load(read_file)
        self.assertEqual(str(dict), answer)

    def test_diff_when_nothing_change(self):
        answer = []
        self.assertEqual(state.diff(), answer)

    def test_diff_when_something_was_change(self):
        answer = ['1.txt']
        self.assertEqual(state_2.diff(), answer)

    def test_md5(self):
        answer = "356a192b7913b04c54574d18c28d46e6395428ab"
        self.assertEqual(md5(directory, '1.txt'), answer)


if __name__ == '__main__':
    unittest.main()
