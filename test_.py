import unittest
from AuthMail.auth import MailRuCloud
from StateOfDirectory.currentState import State
import json
import os


class TestGetFiles(unittest.TestCase):
    directory = str(os.getcwd()) + r'/Tests/forTest1'
    state = State(directory)
    state_2 = State(str(os.getcwd()) + r'/Tests/forTest2')
    mail = MailRuCloud('testforpython13@mail.ru', 'R&ft3OKEprs1', "", "")

    def test_auth(self):
        answer = {'home/': {'Берег.jpg',
                            'Горное озеро.jpg',
                            'Долина реки.jpg',
                            'На отдыхе.jpg',
                            'Полет.mp4',
                            'Чистая вода.jpg'}}
        self.assertEqual(TestGetFiles.mail.get_files_name(), answer)

    def test_sync(self):
        same = False
        answer = ["1.txt", "2.txt", "3.txt", "4.txt"]
        length = len(answer)
        TestGetFiles.state.sync()
        with open(os.path.join(TestGetFiles.directory, "currentState.json"),
                  'r') \
                as read_file:
            dict_answer = json.load(read_file)
        different = set(dict_answer["files"]) - set(answer)
        if length == len(dict_answer["files"]) and str(different) == "set()":
            same = True
        self.assertTrue(same)


if __name__ == '__main__':
    unittest.main()
