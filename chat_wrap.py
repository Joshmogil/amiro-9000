import time

import random

import os
import openai
from dotenv import load_dotenv

load_dotenv("./.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

def talk(prompt):
  time.sleep(random.randrange(12,31)/10)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=98,
    top_p=1,
    frequency_penalty=0.32,
    presence_penalty=0.65
  )
  return response

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

for feeling in ["happy","insightful", "angry", "hateful", "stupid", "vindicative"]:
  print(f"ChatGPT responding as a {feeling} person, using prompt wraps:")
  resp = respond("Was barrack obama a good president?", feeling)
  print(resp["choices"][0]["text"].replace("\n","").replace("?",""))
  print('\n')