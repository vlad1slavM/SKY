import unittest
from AuthMail.auth import loginbot


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


if __name__ == '__main__':
    unittest.main()