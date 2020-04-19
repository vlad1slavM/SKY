import unittest
from AuthMail.auth import loginbot
from StateOfDirectory.currentState import sync


class TestGetFiles(unittest.TestCase):
    def test_auth(self):
        answer = ['Mail.ru рекомендует',
                  'testik',
                  'Берег.jpg',
                  'Горное озеро.jpg',
                  'Долина реки.jpg',
                  'На отдыхе.jpg',
                  'Полет.mp4',
                  'Чистая вода.jpg']
        self.assertEqual(loginbot('testforpython12', '^cf487z4j#R*pdR'),
                         answer)

    def test_sync(self):
        answer = {'adasdad.txt': 'dda1bb9cc0e76a1fdf005b1380619240',
                  'asd.txt': 'd9ef8c633400198e5e6c6480e18cfd1d',
                  'currentState.txt': '03d2f517b7d7f768e54edfd21934480e',
                  'dffffff.txt': 'f7b616ef776ff01adabf558837a72453'}
        self.assertEqual(sync('forTest'), str(answer))


if __name__ == '__main__':
    unittest.main()