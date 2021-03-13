import os
#import time
from discord.ext import commands

from keep_alive import keep_alive
import helper_functions

from database import database
#import chain

prefix = "$"
client = commands.Bot(prefix)

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
    quote = helper_functions.get_quote()
    await ctx.message.channel.send(quote)
    return 

@client.command()
async def message(ctx):
  await ctx.message.channel.send(ctx.message)

@client.command()
async def image(ctx):
  url = helper_functions.get_random_image()
  await ctx.message.channel.send(url)

#get crypto price
@client.command() 
async def crypto(ctx, *, message=None):
  formatRetVal = helper_functions.format_crypto(message)
  await ctx.message.channel.send(formatRetVal)
  return

#send tweet
@client.command() 
async def tweet(ctx, *, message=None):
  if ctx.message.author.name == "Gene_Paremesan":
    helper_functions.send_tweet(message)
  elif ctx.message.author.name == "FancyDynamics":
    helper_functions.send_tweet_fancy_d(message)
  else:
    await ctx.message.channel.send("You dont get to tweet: @" + ctx.message.author.name)
  return
#check the RoBottone Chain
@client.command() 
async def blockchain(ctx):
  #chain_value = chain.get_chain()
  #await ctx.message.channel.send(chain_value)
  return

@client.command() 
async def mine(ctx):
  #chain_value = chain.mine_chain(ctx.message.author.name)
  #await ctx.message.channel.send(chain_value)
  return

@client.event
async def on_message(message):
  if message.author.bot == True:
    #ignore bots
    return
  
  msg = message.content.lower()

  #Check twitter for hashtag
  if msg.startswith("#"):
    tweet_list = helper_functions.get_twitter(msg)
    if tweet_list != None:
      for tweet in tweet_list:
        await message.channel.send(tweet)
    return

  elif msg.startswith("@"):
    tweets = helper_functions.get_twitter_user(msg)
    if tweets != None:
      for tweet in tweets:
        await message.channel.send(tweet)
    return 

  gifStr = ""
  if msg.find("pussy") != -1:
    gifStr= helper_functions.get_image_from_pussy()
  #Check for awesome
  elif msg.find("awesome") != -1:
    gifStr = helper_functions.get_image_from_awesome()
  #Check for hap
  elif msg.find("ham") != -1:
    gifStr = helper_functions.get_image_from_ham()
  #Check for tits
  elif msg.find("tits") != -1:
    gifStr = helper_functions.get_image_from_tits()
  #check for nice
  elif msg.find("nice") != -1:
    gifStr = helper_functions.get_image_from_nice()
  #check for omg
  elif msg.find("omg") != -1:
    gifStr = helper_functions.get_image_from_omg()
  #check for thanks
  elif msg.find("ty") != -1 or msg.find("thank") != -1 or msg.find("thx") != -1:
    gifStr = helper_functions.get_image_from_thanks()
  if gifStr != "":
    await message.channel.send(gifStr)

  await client.process_commands(message)

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))


#Keeps the server alive on the server
keep_alive()    
client.run(os.getenv('TOKEN'))
#chain.start_blockchain()
database()