import re

def check_password ():

    password = input ("Enter your password: ")

    score = 0

    if len(password) >=8:
        score +=1
    if re.search (r'[A-Z]', password):
        score +=1
    if re.search (r'\d', password):
        score +=1
    if re.search (r'[@_!#$%^&*?]', password):
        score +=1

    print ("final password score:", score, "/4")

    if score == 4:
        print ("strong")
    elif score == 3:
        print ("moderate")
    else:
        print ("weak")
    

check_password()