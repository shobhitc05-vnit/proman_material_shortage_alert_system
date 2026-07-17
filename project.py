import pandas as pd
df = pd.read_excel("inventory.xlsx")
print(df.head())


shortage_df = df[df["Current_Stock"] < df["Safety_Stock"]]
print(shortage_df)


import schedule
import time

import smtplib
from email.mime.text import MIMEText


def job():
  sender_email = "shobhitc05@gmail.com"
  password = "aaaa bbbb cccc dddd" # Use an app password for Gmail
  for index, row in shortage_df.iterrows():

      subject = f"URGENT: Material Shortage Alert - {row['Material_Name']}"

      body = f"""
      Material: {row['Material_Name']}
      Current Stock: {row['Current_Stock']}
      Safety Stock: {row['Safety_Stock']}

      Immediate action required.
      """

      msg = MIMEText(body)
      msg["Subject"] = subject
      msg["From"] = sender_email
      msg["To"] = row["Buyer_Email"]

      with smtplib.SMTP("smtp.gmail.com", 587) as server:
          server.starttls()
          server.login(sender_email, password)
          server.send_message(msg)

      print(f"Alert sent for {row['Material_Name']}")


schedule.every().day.at("09:00").do(job)

while True:
  schedule.run_pending()
  time.sleep(1)



