# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

with open("quotes.txt") as data_file:
    data = data_file.readlines()
    print(data)

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=user_name,password=password)
connection.sendmail(from_addr=user_name,to_addrs="herbertasiedu19@gmail.com",msg=f"Motivational Quote\n\n{random.choice(data)}")

