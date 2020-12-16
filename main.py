import discord
import os
import requests
import json
from replit import db

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_fuck_words(message):
  if "fucks" in db.keys():
    fucks = db["fucks"]
    fucks.append(message)
  else: 
    db["fucks"] = [message]

def delete_fuck_words(idx):
  fucks = db["fuck_words"]
  if len(fucks) > idx:
    del fucks[idx]
    db["fucks"] = fucks


fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty"]

key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords", "$new", "$del"]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  options = fuck_words
  if "fucks" in db.keys():
    options = options + db["fucks"]

  msg = message.content.lower()

  if msg.startswith('$hello'):
    await message.channel.send('Hello {0}!'.format(message.author))
    return 
    
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    return 
    
  if msg.startswith("$listfuckwords"):
    for word in options:
      await message.channel.send(word + "\n")
    return

  if msg.startswith("$robottone"):
    for word in key_words:
      await message.channel.send(word + "\n")
    return


  if msg.startswith("$new"):
    fucksword = msg.split("new ", 1)[1]
    update_fuck_words(fucksword)
    await message.channel.send("Added new word")
    return 

  if msg.startswith("$del"):
    fucksword = []
    if "fucks" in db.keys():
      idx = int(msg.split("$del",1)[1])
      delete_fuck_words(idx)
      fucksword = db["fucks"]
    await message.channel.send(fucksword)
    return 

  if any(word.lower() in msg for word in options):
    censor_message = "That's not nice!"
    await message.channel.send(censor_message)
    return 
    
client.run(os.getenv('TOKEN'))