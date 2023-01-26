import pandas
import smtplib
import random
import datetime as dt

today_month = dt.datetime.month
today_day = dt.datetime.weekday
today = (today_month, today_day)


b_data = pandas.read_csv("birthdays.csv")
data_dict = b_data.to_dict()

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in b_data.iterrows()}

print(birthday_dict)

# if (today_month, today_day) in birthdays_dict:
#     pass