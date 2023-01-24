import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "generic@gmail.com"
password = "genericpassword"


random_quote = random.choice(list(open("quotes.txt", "r")))

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=my_email, password=password)
        connections.sendmail(
            from_addr=my_email,
            to_addrs="generic@yahoo.com",
            msg=f"Subject:Hello\n\n{random_quote}."
        )
        connections.close()

