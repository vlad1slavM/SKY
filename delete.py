import requests

url = r'https://cloud.mail.ru/api/v2/file/add'
s = requests.post(url)
print(s.text)

file = 'F95058792223816D32DCF2799A18EE74A72F2D23'
print(file.lower())