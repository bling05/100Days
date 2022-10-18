import smtplib
import random

my_email = "brantonling404@gmail.com"
password = "rrumphcchgnowzxf"
to_email = "omarfchaudhry613@gmail.com"

def send_email():
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Your Inspirational Quote for the Day!\n\n{quote}"
        )
