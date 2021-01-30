import os
#import time
from discord.ext import commands

from keep_alive import keep_alive
from helper_functions import get_quote
from helper_functions import get_random_image
from replit import db
import random 

prefix = "$"
client = commands.Bot(prefix)


fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty", "cunt", "bitch", "bastard"]

options = fuck_words

key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords"]

players = {}

@client.command()
async def hello(ctx):
    await ctx.message.channel.send('Hello {0}!'.format(ctx.message.author.name))

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

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

@client.event
async def on_message(message):
  val = random.randint(0,99)
  if message.author.bot == True:
    #ignore bots
    return
  msg = message.content.lower()

  if any(word.lower() in msg for word in options):
    gifStr = "That's not nice!"
  elif msg.find("pussy") != -1:
    gifStr= "https://imgur.com/r/gifs/al9cdQK"
    if val % 2 == 0:
      await message.channel.send("Pussy on the chainwax!")
      gifStr="https://i.makeagif.com/media/12-07-2017/gdW2fv.gif"
    return
  elif msg.find("awesome") != -1:
    gifStr = "https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327"
    if val % 2 == 0:
      gifStr = "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242"
  elif msg.find("ham") != -1:
    gifStr = "https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"
  elif msg.find("tits") != -1:
    if val % 2:
      gifStr = "(o)Y(o)"
    else: 
      gifStr = "https://media1.tenor.com/images/e257c0306583a544a6f86a7904b6c37b/tenor.gif?itemid=3529236"

  await message.channel.send(gifStr)
  await client.process_commands(message)

@client.event
async def on_ready():

  options = fuck_words
  if "fucks" in db.keys():
    options = options + db["fucks"]
  print('We have logged in as {0.user}'.format(client))


#Keeps the server alive on the server
keep_alive()    
client.run(os.getenv('TOKEN'))