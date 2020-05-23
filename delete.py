'''https://cloud.mail.ru/home/test1.txt'''
import json


file = 'C:\\Users\\dlach\\Documents\\GitHub\\SKY\\forTest\\currentState.json'
dict = {'test1.txt': 'b444ac06613fc8d63795be9ad0beaf55011936ac', 'test2.txt': '109f4b3c50d7b0df729d299bc6f8e9ef9066971f', 'test3.txt': 'e81803683a032fb1084163fee1efb28b032a64f6', 'test4.txt': 'da39a3ee5e6b4b0d3255bfef95601890afd80709'}

with open(file, "w") as write_file:
    data = json.dump(dict, write_file)

with open(file, 'r') as read_file:
    date = json.load(read_file)
print(date['test1.txt'])