from utils.zodiac import SendMail
import sys
import enquiries

SIGNS = ['aquarius', 'aries', 'cancer', 'capricon',
         'gemini', 'leo', 'libra', 'pisces',
         'sagittarius', 'scorpio', 'taurus', 'virgo']

try:
    zodiac_sign = enquiries.choose('Choose a zodiac sign: ', SIGNS)
    recipient_email = input("Enter recipient email address: ")
    if zodiac_sign and recipient_email:
        print("Zodiac Sign:", zodiac_sign)
        print("Recipient Email:", recipient_email)
        SendMail(zodiac_sign, recipient_email)
    else:
        sys.exit("Please fill in the required fields.")
except KeyboardInterrupt:
    print("\nExiting program....\n")
