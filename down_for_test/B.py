import hashlib
#mes = str(input())

tests = ['12344441234444123', 'kekaaakekbbbkek', 'nikakvynenauchites', 'Lol', 'kekek']


def vilg(message):
    left_index = 1
    right_index = len(message) - 1
    ans = ''

    while right_index > left_index:
        left_hash = hashlib.md5(message[:left_index].encode()).hexdigest()
        right_hash = hashlib.md5(message[right_index:].encode()).hexdigest()
        if left_hash == right_hash:
            substring = message[:left_index]
            len_of_sub = len(substring)
            last_left_index = left_index
            last_right_index = right_index
            for i in range(last_left_index, last_right_index):
                new_sub = message[i:len_of_sub + i]
                hash_sub = hashlib.md5(new_sub.encode()).hexdigest()
                hash_ans = hashlib.md5(substring.encode()).hexdigest()
                if hash_sub == hash_ans:
                    ans = new_sub
                    break
                if len_of_sub + i == last_right_index:
                    break
            left_index += 1
            right_index -= 1

        else:
            left_index += 1
            right_index -= 1

    if len(ans) != 0:
        print(ans)
    else:
        print('Just a legend')


for el in tests:
    vilg(el)
