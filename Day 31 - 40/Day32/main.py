import smtplib


my_email = "generic@gmail.com"
password = "genericpassword"

connections = smtplib.SMTP("smtp.gmail.com")
connections.starttls()
connections.login(user=my_email, password=password)
connections.sendmail(from_addr=my_email, to_addrs="generic@yahoo.com", msg="Hello")
connections.close()
