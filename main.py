import discord
import os
#import time

from keep_alive import keep_alive
from helper_functions import get_quote
'''
from helper_functions import get_playlist_name
from helper_functions import update_playlist_db
from helper_functions import update_fuck_words
from helper_functions import delete_fuck_words
from helper_functions import botify_helper
'''
from replit import db

client = discord.Client()

fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty", "cunt", "bitch", "bastard"]


key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords"]

playlist_list = []

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author.bot.lower() == "true":
    #ignore bots
    return

  '''
  playlists = playlist_list
  
  if "playlists" in db.keys():
    playlists = playlists + db["playlists"]

  channel_name = message.channel.name

  if channel_name == "monthly-playlist-drop":
    if get_playlist_name() not in playlists:
      update_playlist_db(get_playlist_name())
      await message.channel.send(botify_helper(message.content, "create"))
      time.sleep(10)
    await message.channel.send(botify_helper(message.content, "playlist"))
    time.sleep(10)
    await message.channel.send(botify_helper(message.content, "queue"))
    return
  '''

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