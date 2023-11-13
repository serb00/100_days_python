import random
import pandas
import datetime as dt
# import smtplib


def get_random_letter():
    with open("letter_templates/" + random.choice(letters), mode="r") as file:
        return file.read()


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
# birthday_today_list = df[(df["month"] == today_month) & (df["day"] == today_day)]
# optimized way for bigger datasets
birthday_today_list = df.query(f'month == {today_month} & day == {today_day}')
list_of_recipients = [(data_row["name"], data_row["email"]) for (index, data_row) in birthday_today_list.iterrows()]

# alternative way thought by the course, trouble with several people having birthday in a same day
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}
# today_tuple = (today_month, today_day)
# if today_tuple in birthdays_dict:
#     print(birthdays_dict[today_tuple])

for (to_name, to_mail) in list_of_recipients:
    message = get_random_letter()
    send_birthday_mail(to_name, to_mail, message)
