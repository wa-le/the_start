import smtplib

my_email = "mainstopstore@gmail.com"
my_email_pass = "--password here--"
recipient_email = "jamesupper2022@yahoo.com"
the_msg = "Subject:Hello\n\nHow are you doing and how is your health"

# connect to "your" email server
with smtplib.SMTP("smtp.gmail.com", port=587) as new_connect:
    # secure the connection
    new_connect.starttls()

    new_connect.login(user=my_email, password=my_email_pass)
    new_connect.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=the_msg)

