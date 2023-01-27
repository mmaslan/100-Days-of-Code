import pandas
import smtplib
import random
from datetime import datetime


today = datetime.now()
today_tuple = (today.month, today.day)

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

b_data = pandas.read_csv("birthdays.csv")
data_dict = b_data.to_dict()

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in b_data.iterrows()}
print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(MY_EMAIL, MY_PASSWORD)
        connections.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

