'''https://cloud.mail.ru/home/test1.txt'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    '--n',
    type=int,
    help='provide an integer '
)
my_namespace = parser.parse_args()

print(my_namespace.n ** 2)

