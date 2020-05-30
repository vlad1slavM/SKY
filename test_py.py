import unittest
from AuthMail.auth import login_bot
from StateOfDirectory.currentState import State, md5
import json
direction = r'C:\Users\dlach\Documents\GitHub\SKY\forTest1'
state = State(direction)
state_2 = State(r'C:\Users\dlach\Documents\GitHub\SKY\forTest2')


class TestGetFiles(unittest.TestCase):
    def test_auth(self):
        answer = ['Mail.ru рекомендует',
                  'Берег.jpg',
                  'Горное озеро.jpg',
                  'Долина реки.jpg',
                  'На отдыхе.jpg',
                  'Полет.mp4',
                  'Чистая вода.jpg']
        self.assertEqual(login_bot('testforpython13@mail.ru', 'R&ft3OKEprs1'),
                         answer)

    def test_sync(self):
        answer = "{'1.txt': '356a192b7913b04c54574d18c28d46e6395428ab'," \
                 " '2.txt': 'da4b9237bacccdf19c0760cab7aec4a8359010b0'," \
                 " '3.txt': '77de68daecd823babbb58edb1c8e14d7106e83bb'," \
                 " '4.txt': '1b6453892473a467d07372d45eb05abc2031647a'}"
        state.sync()
        with open(direction + '\\currentState.json', 'r') as read_file:
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
        self.assertEqual(md5(direction, '1.txt'), answer)


if __name__ == '__main__':
    unittest.main()

