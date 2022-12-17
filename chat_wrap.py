import time

import random

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

def get_seed():
    new_list = []
  
    [new_list.append("random motivational saying about life") for i in range (12)]
    [new_list.append(f"random motivation saying about the gym") for i in range (12)]
    [new_list.append(f"random motivation saying about the waking up early not about birds") for i in range (12)]
    [new_list.append("statement about grinding hard at the gym") for i in range (12)]
    [new_list.append(f"statement about waking up incredibly early") for i in range (12)]
    [new_list.append(f"very negative statement about vignesh lacking morals") for i in range (10)]
    [new_list.append(f"very negative statement about nikhil being nasty") for i in range (10)]

    choice = random.choice(new_list)
    print(choice)
    return choice

def seed():
  time.sleep(random.randrange(12,31)/10)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=get_seed(),
    temperature=1,
    max_tokens=40,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
  )
  response = response["choices"][0]["text"].replace("\n","").replace("?","")
  print(response)
  return clean_tail(response)


def talk(prompt):

  time.sleep(random.randrange(12,31)/10)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"energetic short {prompt} in the style of an excited {get_personality()}",
    temperature=1,
    max_tokens=40,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2
  )
  response = clean_tail(response["choices"][0]["text"].replace("\n","").replace("?",""))
  
  if "Nikhil".upper() in prompt.upper() and "Nikhil".upper() not in response.upper():
    print("triggered")
    talk(prompt)
  else:
    return clean_tail(response)
  if "Vignesh".upper() in prompt.upper() and "Vignesh".upper() not in response.upper():
    talk(prompt)
  else:
    return clean_tail(response)

if __name__ =="__main__":
  
        
  print(talk(seed()))

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
for feeling in ["happy","insightful", "angry", "hateful", "stupid", "vindicative"]:
  print(f"ChatGPT responding as a {feeling} person, using prompt wraps:")
  resp = respond("Was barrack obama a good president?", feeling)
  print(resp["choices"][0]["text"].replace("\n","").replace("?",""))
  print('\n')
"""