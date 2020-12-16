import discord
import os
import requests
import json
import asana

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

fuck_words = ["fuck", "Fuck", "shit", "Shit", "crap", "Crap", "damn", "Damn", "dammit", "Dammit", "titty", "Titty", "ass", "Ass", "fucking", "Fucking", "shitty", "Shitty"]


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello {0}!'.format(message.author))
    
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in message.content for word in fuck_words):
    censor_message = "That's not nice!"
    await message.channel.send(censor_message)


client.run(os.getenv('TOKEN'))