import sys
from utils.zodiac import SendMail

try:
    zodiac_sign = input('Enter a zodiac sign: ')
    recipient_email = input("Enter recipient email address: ")
    if zodiac_sign and recipient_email:
        SendMail(zodiac_sign, recipient_email)
    else:
        sys.exit("Please fill in the required fields.")
except KeyboardInterrupt:
    print("\nExiting program....\n")
