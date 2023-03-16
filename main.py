import hashlib
import json

def open_json(destination):
    with open(f'{destination}.json') as f:
        data=json.load(f)
    return data

def dump_json(destination,data):
    with open(f'{destination}.json', 'w') as f:
        json.dump(data, f, indent=4)

register=open_json('user_password')
check = False
def check_password(password,input_name):
    global check
    lowercase = False
    uppercase = False
    number = False
    special_character = False
    character = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",  "[", "]", "|", ":", ";", "-", "", "+", "=", "{", "}", "<", ">", ",", ".", "?"]
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if len(password) > 8:
        for char in password:
            if char.lower():
                lowercase = True
            if char.upper():
                uppercase = True
            if char.isdigit():
                number = True
            if char in character:
                special_character = True
        if password_hash in [register[i] for i in register]:
            return 'Another password pwease :3, this one already in database UwU'
        if number and uppercase and lowercase and special_character:
            register[input_name]= password_hash
            check = True
            return f'Your password is {password}\nYour password hashed is {password_hash}'
    return "the password must contain at least 8 characters, one uppercase, one lowercase, one upercase, one number and one special character"

def password():
    while check == False:
        userinput = input("please enter your password :")
        input_name=input("please enter your name : ")
        print(check_password(userinput,input_name))
        dump_json('user_password',register)

password()