import os

from discord.ext import commands
from discord.ext import tasks
import python_weather 

from keep_alive import keep_alive
import helper_functions

prefix = "$"
client = commands.Bot(prefix)
wclient = python_weather.Client(format=python_weather.IMPERIAL)

class RoBottone:

  first_time = True

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

  @client.command()
  async def ham(ctx):
    url = helper_functions.get_image_from_ham()
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
    if ctx.message.author.name == "Gene_Paremesan" and ctx.message.author.discriminator == "9758":
      helper_functions.send_tweet(message)
    elif ctx.message.author.name == "FancyDynamics" and ctx.message.author.discriminator == "1201":
      helper_functions.send_tweet_fancy_d(message)
    else:
      await ctx.message.channel.send("You dont get to tweet: @" + ctx.message.author.name)
    return

  #get twitter stuff
  @client.command()
  async def twitter(ctx, *, message=None):
    if message == None:
      return
    str = helper_functions.get_twitter_message(message.lower())
    await ctx.message.channel.send(str)
    return

  @client.command()
  async def trending(ctx):
    str = helper_functions.get_twitter_message("#trending")
    await ctx.message.channel.send(str)
    return

  @client.command()
  async def cool(ctx):
    url = helper_functions.get_image_from_nice()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def nice(ctx):
    url = helper_functions.get_image_from_nice()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def awesome(ctx):
    url = helper_functions.get_image_from_nice()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def omg(ctx):
    url = helper_functions.get_image_from_nice()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def tits(ctx):
    url = helper_functions.get_image_from_tits()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def thanks(ctx):
    url = helper_functions.get_image_from_thanks()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def crash(ctx):
    url = helper_functions.get_image_from_crash()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def work(ctx):
    url = helper_functions.get_image_from_work()
    await ctx.message.channel.send(url)
    return

  @client.command()
  async def weather(ctx, *, message=None):
    if message == None:
      return
    try:
      weather = await wclient.find(message)
      forecast = weather.forecast[0]
      output = forecast.sky_text + "\t" + "Low: " + str(forecast.low) + "F\t" + "High: " + str(forecast.high) + "F"
      await ctx.message.channel.send(output)
    except:
      return

  @tasks.loop(hours=6.0)
  async def post_info(self):
    if self.first_time == True:
      self.first_time = False;
      return
    channel = client.get_channel(804355620018454589)
    formatRetVal = helper_functions.bot_crypto()
    await channel.send(formatRetVal)

  def __init__(self):
    keep_alive()   
    client.run(os.getenv('TOKEN'))


robot =  RoBottone()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  robot.post_info()
