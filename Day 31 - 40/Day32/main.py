import smtplib


my_email = "generic@gmail.com"
password = "genericpassword"


with smtplib.SMTP("smtp.gmail.com") as connections:
    connections.starttls()
    connections.login(user=my_email, password=password)
    connections.sendmail(
        from_addr=my_email,
        to_addrs="generic@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of the email."
    )
    connections.close()

import datetime