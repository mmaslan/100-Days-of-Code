import pandas
import smtplib


today = (today_month, today_day)


b_data = pandas.read_csv("birthdays.csv")
birthday_dict = b_data.to_dict()

print(birthday_dict)