import discord
import os
import requests
import json
import time
import datetime

from replit import db
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_playlist_name():
  today = datetime.datetime.now()
  playlist_name = today.strftime("%b") + today.strftime("%Y")
  return(playlist_name)

def update_playlist_db(name):
  if "playlists" in db.keys():
    playlist = db["playlists"]
    playlist.append(name)
  else:
    db["playlists"] = [name]

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

def botify_helper(content, arg):
  botify_str = ""
  if arg == "playlist":
    botify_str = "$botify add " + content + " $to " + get_playlist_name() + "\n"
  elif arg == "queue":
    botify_str = "$botify queue " + content + "\n"
  elif arg == "create":
    botify_str = "$botify create " + get_playlist_name() + "\n"
  return(botify_str)

fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty", "cunt"]

key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords"]

playlist_list = []

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author.name.lower() == "botify":
    return

  playlists = playlist_list
  
  if "playlists" in db.keys():
    playlists = playlists + db["playlists"]

  channel_name = message.channel.name

  if channel_name == "monthly-playlist-drop":
    await message.channel.send(botify_helper(message.content, "create"))
    time.sleep(10)
    if get_playlist_name() not in playlists:
      update_playlist_db(get_playlist_name())
      await message.channel.send(botify_helper(message.content, "create"))
      time.sleep(10)
    await message.channel.send(botify_helper(message.content, "playlist"))
    time.sleep(10)
    await message.channel.send(botify_helper(message.content, "queue"))
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

  if any(word.lower() in msg for word in options):
    censor_message = "That's not nice!"
    await message.channel.send(censor_message)
    return 
#Keeps the server alive on the server
keep_alive()    
client.run(os.getenv('TOKEN'))