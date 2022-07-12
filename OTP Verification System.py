import os
import math
import random
import yagmail

# Password of length 8 will be selected from below string

string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
OTP = ""

length = len(string)

# OTP will be generated from below loop

for i in range(8):
    OTP += string[math.floor(random.random() * length)]

msg = "Hello, your one time password is " + OTP

# above message contains the unique one time password

user = 'ritikkumar.2005.hero@gmail.com'
app_password = 'nhrdnsdczpkhgyod'

to = input("Enter your Email id : ")

subject = 'OTP for verification'

content = [msg]

# OTP will be sent to the person through email

with yagmail.SMTP(user, app_password) as yag:

    yag.send(to, subject, content)
    print('Sent email successfully')

# Enter your OTP below

a = input("Enter Your OTP >>: ")

# This system will generate OTP till we enter incorrect OTP for consecutive three times

for i in range(3):
    if a == OTP:

        # If entered OTP is correct then it will print Verified

        print("Verified")
        break
    else:
        if (i == 2):
            print("Oops !! Incorrect OTP . You have entered three times wrong OTP . Now new OTP can only be generated after 24 hours. \n")
        if(i < 2):
            print("Oops !! Incorrect OTP . \nPlease enter the new OTP generated.")
            OTP = ""

            # Below code will generate new OTP

            for i in range(8):
                OTP += string[math.floor(random.random() * length)]

            msg = "Hello, your one time password is " + OTP
            content = [msg]

            # New OTP will be sent to the person

            yag.send(to, subject, content)

            print('Sent email successfully')

            # Enter your new OTP below

            a = input("Please enter new OTP >>: ")
