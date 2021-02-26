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
from database import database
import chain

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
    quote = get_quote()
    await ctx.message.channel.send(quote)
    return 

@client.command()
async def message(ctx):
  await ctx.message.channel.send(ctx.message)

@client.command()
async def image(ctx):
  url = get_random_image()
  await ctx.message.channel.send(url)

#get crypto price
@client.command() 
async def crypto(ctx, *, message=None):
  formatRetVal = format_crypto(message)
  await ctx.message.channel.send(formatRetVal)
  return

#check the RoBottone Chain
@client.command() 
async def blockchain(ctx):
  chain_value = chain.get_chain()
  await ctx.message.channel.send(chain_value)
  return

@client.command() 
async def mine(ctx):
  chain_value = chain.mine_chain(ctx.message.author.name)
  await ctx.message.channel.send(chain_value)
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
  if msg.find("pussy") != -1:
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
chain.start_blockchain()
database()