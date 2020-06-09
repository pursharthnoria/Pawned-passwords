import requests
import hashlib

def get_hash(passwd):
    hashed_pass = hashlib.sha1(passwd.encode('utf-8')).hexdigest().upper()
    return hashed_pass

def use_api(password):
    hashed = get_hash(password)
    hash_back = hashed[5:]
    hash_first5 = hashed[:5]
    api = 'https://api.pwnedpasswords.com/range/' + hash_first5
    res = requests.get(api).text
    res = res.split('\r\n')
    flag = 0
    for hash in res:
        if hash[:35] == hash_back:
            result = hash_first5 + hash 
            flag = 1
            break
    if flag == 1:
        result = result.split(':')
        print('This password has been used {} times. You should probably change your password'.format(result[1]))
    else:
        print('This password has not been breached yet. You are safe.')

while(True):
    password = input("Enter a password: ")
    if password == 'end' or password == 'END' or password == 'stop' or password == 'STOP' or password == 'exit' or password == 'EXIT':
        break
    else:
        use_api(password)