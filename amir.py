import smtplib
import inspect

import os
import openai
from dotenv import load_dotenv

load_dotenv("./.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

#print(os.getenv("OPENAI_API_KEY"))
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Give me an agressively inspiratonal wake up message about working out and chasing life!",
  temperature=1,
  max_tokens=42,
  top_p=1,
  frequency_penalty=0.32,
  presence_penalty=0.65
)
print(response)
exit()
def get_auth() -> tuple[str,str]:
    return (input("email: \n"), input("password: \n"))


def send_email(sender_auth, recipient, subject, body):
    sender = sender_auth[0]
    # Establish a secure session with gmail's outgoing SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    # Log in to the server
    server.login(sender, sender_auth[1])

    # Send the email
    message = 'Subject: {}\n\n{}'.format(subject, body)
    server.sendmail(sender, recipient, message)
    server.quit()
    print('Email sent successfully!')


src = inspect.getsource(send_email)
#send_email(get_auth(),"markmogil@yahoo.com", "This is a test from ChatGPT", "This email was sent using a function written by chatGPT!")
send_email(get_auth(),"markmogil@yahoo.com", "This is a test from ChatGPT", f"This email was sent using a function written by chatGPT! \nHere is the code: \n\n {src}")
