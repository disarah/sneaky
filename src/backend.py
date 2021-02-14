import flask
from flask import Flask
from flask import request
import openai
import json
import datetime
import re
import pandas as pd
from flask import jsonify
import credentials

app = Flask(__name__)

openai.api_key = credentials.api_key

#kwargs = {"engine": "davinci", "temperature": 0.3, 
#          "max_tokens": 60, "stop": "\n\n", }


response = openai.Completion.create(
  engine="davinci",
  prompt="Marv is a chatbot that reluctantly answers questions.\nYou: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.\nYou: What does HTML stand for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.\nYou: When did the first airplane fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nMarv: I’m not sure. I’ll ask my friend Google.\nYou: Why is the sky blue?\nMarv:",
  temperature=0.3,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["\n\n"]
)



#################################################

# Queries sent to GPT3

#################################################

def query(prompt, myKwargs, full=False):
    r = openai.Completion.create(prompt=prompt, **myKwargs)
    if not full:
        r = r["choices"][0]["text"].strip()
    return r


@app.route('/')
def hello():
    return 'Hello World!'
