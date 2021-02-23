import os
#import time
from discord.ext import commands

from keep_alive import keep_alive
from helper_functions import get_quote
from helper_functions import get_random_image
from helper_functions import format_crypto
import random 
import tweepy
import twitter

prefix = "$"
client = commands.Bot(prefix)

fuck_words = ["fuck", "shit", "crap", "damn", "dammit", "titty", "ass", "fucking", "shitty", "cunt", "bitch", "bastard"]

options = fuck_words

blocked_twitter = ["sex", "tits", "pussy", "gay", "lesbian", "titty", "ass", "nude", "naked", "girlsgonewild", "porn", "pawg", "nsfw", "fuck", "shit", "crap", "damn", "dammit", "fucking", "shitty", "cunt", "bitch", "bastard"]

key_words = ["$robottone", "$hello", "$inspire", "$listfuckwords"]

api = twitter.authenticate_twitter()

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
    
  val = random.randint(0,99)

  msg = message.content.lower()

  #Check twitter for hashtag
  if msg.startswith("#"):
    tag = msg.split(" ")    
    query = tag[0]
    await message.channel.send(query)
    
    if query == "#trending":
      woeid = 2347572 #US
      trends = api.trends_place(1)

      i = 0

      for value in trends: 
          for trend in value['trends']: 
              if i == 10:
                return
              await message.channel.send(trend['name']) 
              i+=1
              
    else:
      if any(word.lower() in msg for word in blocked_twitter):
        await message.channel.send("Sorry not going to look that up")
        return

      for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(3)):
        await message.channel.send(status.text)
        await message.channel.send("==========================================================================================================================")
    return

  gifStr = ""
  #Check for swears
  if any(word.lower() in msg for word in options):
    gifStr = "That's not nice!"
  #Check for pussy
  elif msg.find("pussy") != -1:
    mod = 2
    gifStr= "https://tenor.com/view/alison-brie-alice-sophia-eve-pussy-pretty-beautiful-girl-gif-16850525"
    if val % mod == 0:
      await message.channel.send("Pussy on the chainwax!")
      gifStr="https://i.makeagif.com/media/12-07-2017/gdW2fv.gif"
  #Check for awesome
  elif msg.find("awesome") != -1:
    mod = 2
    gifStr = "https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327"
    if val % mod == 0:
      gifStr = "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242"
  #Check for hap
  elif msg.find("ham") != -1:
    gifStr = "https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"
  #Check for tits
  elif msg.find("tits") != -1:
    mod = 3
    if val % mod == 0:
      gifStr = "https://media1.giphy.com/media/l0HlK3RyTkaJIfRJu/giphy.gif"
    elif val % mod == 1 : 
      gifStr = "https://media1.tenor.com/images/e257c0306583a544a6f86a7904b6c37b/tenor.gif?itemid=3529236"
    else:
      gifStr = "https://lh3.googleusercontent.com/-cySiOTXr73s/YDAKin4bk3I/AAAAAAAAHZM/GTfX_9-y_lol1cPdIwINmHtMYJA9RvXXwCK8BGAsYHg/s0/2021-02-19.gif"

  if gifStr != "":
    await message.channel.send(gifStr)

  await client.process_commands(message)

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))


#Keeps the server alive on the server
keep_alive()    
client.run(os.getenv('TOKEN'))
