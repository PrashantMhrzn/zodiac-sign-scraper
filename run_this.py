from utils.zodiac import SendMail
import schedule
import time


def job():
    SendMail('gemini', 'sulavmaharjan63@gmail.com')
    print('Email sent')


job()
schedule.every().day.at("07:00").do(job)


while True:
    schedule.run_pending()
    time.sleep(2)
