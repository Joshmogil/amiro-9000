import time

import random
import datetime

# using now() to get current time
current_time = datetime.datetime.now()
import os
import openai
from dotenv import load_dotenv

load_dotenv("./.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

def clean_tail(response):
  try:
    if response[-1] not in ".?!":
      comma = response.rfind(",")
      period = response.rfind(".")
      mark = response.rfind("?")
      exclaim = response.rfind("!")
      last_ender= max([comma,period,mark,exclaim])
      response = response[0:last_ender+1]
      if last_ender == comma:
        response = response[0:-1]+"."
    if not response[0].isalpha():
      response = response[1:]

    return response
  except:
    return response


def get_personality():
    return random.choice([
        "man"
        ])

def get_morning_seed():
    new_list = []
  
    [new_list.append("in a single thought or sentence, Give a short inspirational message about getting after it! in the style of an excited man") for i in range (12)]
    [new_list.append(f"in a single thought or sentence, Brag about attacking the gym or waking up early!") for i in range (12)]

    choice = random.choice(new_list)
    print(choice)
    return choice

def get_night_seed():
    new_list = []
    [new_list.append(f"in a single thought or sentence, meanly talk down to all of your friends about how they should feel bad about not being the most successful versions of themselves") for i in range (15)]
    [new_list.append(f"in a single thought or sentence, brag about how you will wake up extremely early to fight demons in the gym jocko-style! in an amped up and inspirational way!") for i in range (10)]
    [new_list.append(f"in a single thought or sentence, Talk about how tomorrow is a new opportunity in an inspirational way! in the style of an excited man") for i in range (10)]
    [new_list.append(f"in a single thought or sentence, Tell me your suspicions about a ficticious person named vig in the style of an excited man") for i in range (7)]
    [new_list.append(f"in a single thought or sentence, be offended or slighted by a ficticious person named nikhil in the style of an excited man") for i in range (7)]

    choice = random.choice(new_list)
    print(choice)
    return choice




def talk():
  print(current_time.hour)

  if current_time.hour<12:
    prompt=get_morning_seed()
  else:
    prompt=get_night_seed()

  time.sleep(random.randrange(12,31)/10)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f" {prompt} ",
    temperature=1,
    max_tokens=40,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
  )
  response = clean_tail(response["choices"][0]["text"].replace("\n","").replace("?",""))

  return clean_tail(response)

if __name__ =="__main__":
  
        
  print(talk())



"""
def respond(message, feeling):
  time.sleep(random.randrange(12,31)/10)
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Respond how an extremely {feeling} person would respond to the message: {message}",
  temperature=1,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0.32,
  presence_penalty=0.65
  )
  return response
"""
"""
for feeling in ["happy","insightful", "angry", "hateful", "stupid", "vindicative"]:
  print(f"ChatGPT responding as a {feeling} person, using prompt wraps:")
  resp = respond("Was barrack obama a good president?", feeling)
  print(resp["choices"][0]["text"].replace("\n","").replace("?",""))
  print('\n')
"""