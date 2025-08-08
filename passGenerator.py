import string
import secrets

rndmLetters = string.ascii_letters
rndmUpper = string.ascii_uppercase
rndmLower = string.ascii_lowercase
allChar = rndmUpper + rndmLower + rndmLetters
def passWordGenerator():

    while True:
        print("Enter length of password you want to Generate : ")
        
        try:
            length = int(input("-> "))
            break
        except ValueError:
            print('input number of length only, no other characters.')

    while True:
        print("How many passwords do you want to generate?")
        
        try:
            lengthInput = int(input("-> "))
            break
        except ValueError:
            print('input number of length only, no other characters.')
    count = 0

    while lengthInput != count:
        passWord = ''
        for i in range(length):
            passWord += secrets.choice(allChar)
        print(passWord)
        count += 1
        if lengthInput == count:
            break

def another():
    while True:
        yep = input('do you want more? (y/n) -> ').lower()
        
        if 'y' in yep or 'yes' in yep:
            passWordGenerator()
        elif 'n' in yep or 'no' in yep:
            print('thankyou for using my app 🥰')
            input('press any key to exit...')
            break
        else:
            print("invalid answer, try 'y' or 'n' to continue")
passWordGenerator()
another()