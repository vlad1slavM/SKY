from AuthMail.auth import loginbot
from StateOfDirectory.currentState import sync, diff

print(loginbot('vladislav_3982', 'Markgavno1'))
sync()
print(diff())
