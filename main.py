import os
#import time
from discord.ext import commands

from keep_alive import keep_alive
from helper_functions import get_quote
from helper_functions import get_random_image
from helper_functions import format_crypto
from helper_functions import get_image_from_tits
from helper_functions import get_image_from_ham
from helper_functions import get_image_from_awesome
from helper_functions import get_image_from_pussy
from helper_functions import get_twitter
import random 

prefix = "$"
client = commands.Bot(prefix)

fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty", "cunt", "bitch", "bastard"]

options = fuck_words

key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords"]


@client.command()
async def hello(ctx):
    await ctx.message.channel.send('Hello {0}!'.format(ctx.message.author.name))
    return

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    return

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    return

@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.message.channel.send(quote)
    return 

@client.command()
async def listbadwords(ctx):
    for word in options:
      await ctx.message.channel.send(word + "\n")
    return

@client.command()
async def robottone(ctx):
    for word in key_words:
      await ctx.message.channel.send(word + "\n")
    return

@client.command()
async def message(ctx):
  await ctx.message.channel.send(ctx.message)

@client.command()
async def image(ctx):
  url = get_random_image()
  await ctx.message.channel.send(url)

#play youtube link
@client.command(pass_context=True)
async def play(ctx, url):
  async with ctx.typing():
    return  

#get crypto price
@client.command() 
async def crypto(ctx, *, message=None):
  formatRetVal = format_crypto(message)
  await ctx.message.channel.send(formatRetVal)
  return

@client.event
async def on_message(message):
  if message.author.bot == True:
    #ignore bots
    return
    
  msg = message.content.lower()

  #Check twitter for hashtag
  if msg.startswith("#"):
    await message.channel.send(get_twitter(msg))

  gifStr = ""
  #Check for swears
  if any(word.lower() in msg for word in options):
    gifStr = "That's not nice!"
  #Check for pussy
  elif msg.find("pussy") != -1:
    gifStr= get_image_from_pussy()
  #Check for awesome
  elif msg.find("awesome") != -1:
    gifStr = get_image_from_awesome()
  #Check for hap
  elif msg.find("ham") != -1:
    gifStr = get_image_from_ham()
  #Check for tits
  elif msg.find("tits") != -1:
    gifStr = get_image_from_tits()

  if gifStr != "":
    await message.channel.send(gifStr)

  await client.process_commands(message)

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))


#Keeps the server alive on the server
keep_alive()    
client.run(os.getenv('TOKEN'))
