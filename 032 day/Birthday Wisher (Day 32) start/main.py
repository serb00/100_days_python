# import smtplib
#
# from_mail = "test@gmai.com"
# from_pass = "mypass"
# from_smtp = "smtp.gmail.com"
# to_mail = "test2@yahoo.com"
#
# message = "Subject:Hello\n\nThis is the body of the mail"
#
# with smtplib.SMTP(from_smtp) as connection:
#     connection.starttls()
#     connection.login(user=from_mail, password=from_pass)
#     connection.sendmail(
#         from_addr=from_mail,
#         to_addrs=to_mail,
#         msg=message
#     )

import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with open("quotes.txt", mode="r") as file:
        quote_of_day = random.choice(file.readlines())
    print(quote_of_day)  # alternatively you can send it over Email using the code example above
else:
    print("it's not Monday, sorry.")

specific_date = dt.datetime(year=2023, month=2, day=28)
