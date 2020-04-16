import os
list_of_files = os.listdir(f'D:\\test')

def writelogs():
    log = open('currentState.log', 'w')
    for el in list_of_files:
        log.write(el + '\n')

    log.close()

print('You want save current state YES/NO')

messadge = input()
if messadge == 'YES':
    writelogs()
else:
    print('OKEY')
