import pandas
from datetime import datetime
import smtplib
from random import randint

USER = "your@mail.com"
PASSWORD = "password"



today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for [index, data_row] in data.iterrows()}


if today in birthdays_dict:
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    birthday_person_name = birthdays_dict[today]["name"]
    birthday_person_mail = birthdays_dict[today]["email"]

    with open(file_path) as letter:
        letter_content = letter.read()
        replaced_letter_content = letter_content.replace("[NAME]", birthday_person_name)

    with smtplib.SMTP("smtp.office365.com", 587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=birthday_person_mail, msg=f"Subject:Happy Birthday\n\n{replaced_letter_content}")














