import random
import pandas
import datetime as dt
# import smtplib


def send_birthday_mail(name, mail, text):
    from_mail = "test@gmai.com"
    from_pass = "mypass"
    from_smtp = "smtp.gmail.com"

    to_mail = mail
    message = f"Subject:Happy birthday, {name}!\n\n{text.replace('[NAME]', name)}"

    print(message)

    # with smtplib.SMTP(from_smtp) as connection:
    #     connection.starttls()
    #     connection.login(user=from_mail, password=from_pass)
    #     connection.sendmail(
    #         from_addr=from_mail,
    #         to_addrs=to_mail,
    #         msg=message
    #     )


now = dt.datetime.now()
today_day = now.day
today_month = now.month

letters = [
    "letter_1.txt",
    "letter_2.txt",
    "letter_3.txt"
]

df = pandas.read_csv("birthdays.csv")
birthday_today_list = df[df["month"] == today_month][df["day"] == today_day].values

list_of_recipients = [(x[0], x[1]) for x in birthday_today_list]


def get_random_letter():
    with open("letter_templates/"+random.choice(letters), mode="r") as file:
        return file.read()


for (to_name, to_mail) in list_of_recipients:
    message = get_random_letter()
    send_birthday_mail(to_name, to_mail, message)
