import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.352024
MY_LONG = 18.646639
MY_EMAIL = "generic@gmail.com"
PASSWORD = "genericpassword"


def if_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 or MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if if_iss_overhead() and is_night():
        connections = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")
        connections.starttls()
        connections.login(MY_EMAIL, PASSWORD)
        connections.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: ISS is right above your head."
        )
        connections.close()
