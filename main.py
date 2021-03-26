#!/usr/bin/env python3
from AuthMail.auth import MailRuCloud
from StateOfDirectory.currentState import State
import argparse
import getpass


def parser_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d',
        '--direction',
        type=str,
        help='Введите -d директория, в которую вы хотите скачать файлы '
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
                             ' из облака'
                        )

    parser.add_argument('-c',
                        '--cloudFile',
                        type=str,
                        help='Выберите директорию в облаке, которую хотите'
                             ' скачать'
                        )
    return parser


my_namespace = parser_args().parse_args()
state = State(my_namespace.direction)


if __name__ == "__main__":
    login = str(input("User Name : "))
    if my_namespace.action == 'files':
        password = getpass.getpass()
        mail = MailRuCloud(login, password, "", "")
        print(mail.get_files_name())

    elif my_namespace.action == 'sync':
        print(state.sync())

    elif my_namespace.action == 'diff':
        state.diff()

    elif my_namespace.action == 'download':
        password = getpass.getpass()
        mail = MailRuCloud(login, password, my_namespace.cloudFile,
                           my_namespace.direction)
        mail.download()
