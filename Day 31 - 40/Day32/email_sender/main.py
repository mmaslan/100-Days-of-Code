import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "generic@gmail.com"
PASSWORD = "genericpassword"


random_quote = random.choice(list(open("quotes.txt", "r")))

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(MY_EMAIL, PASSWORD)
        connections.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday motivation:\n\n{random_quote}."
        )
        connections.close()

