import re
import hashlib

user_password = ''
def password(user_password):
    while True:
        user_password = input("enter your password :")
        if (len(user_password)<8):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
        elif not re.search("[a-z]", user_password):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
            continue
        elif not re.search("[A-Z]", user_password):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
            continue
        elif not re.search("[0-9]", user_password):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
            continue
        elif not re.search("[!@#$%^&*]" , user_password):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
            continue
        elif re.search("\s" , user_password):
            flag = False
            print("the password must contain at least 8 characters, one uppercase, one lowercase, one number and one special character ")
            continue
        else:
            flag = True
            print('Your password is: '+user_password)
            print('Your hashed password is: '+hash_pass(user_password))
            print("Valid Password")
            break

def hash_pass(user_password):
    return hashlib.sha256(user_password.encode()).hexdigest()


password(user_password)