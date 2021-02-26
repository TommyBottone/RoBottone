import requests
import json
import random 
import cryptocompare
import tweepy
import twitter

#blocked twitter words
blocked_twitter = ["sex", "tits", "pussy", "gay", "lesbian", "titty", "ass", "nude", "naked", "girlsgonewild", "porn", "pawg", "nsfw", "fuck", "shit", "crap", "damn", "dammit", "fucking", "shitty", "cunt", "bitch", "bastard"]

crypto_list = ["BTC", "ETH", "ADA", "XRP", "LTC", "DOGE", "MANA", "ATOM"]

api = twitter.authenticate_twitter()

#gifs for tits
titsStr = ["https://media1.giphy.com/media/l0HlK3RyTkaJIfRJu/giphy.gif","https://media1.tenor.com/images/e257c0306583a544a6f86a7904b6c37b/tenor.gif?itemid=3529236","https://lh3.googleusercontent.com/-cySiOTXr73s/YDAKin4bk3I/AAAAAAAAHZM/GTfX_9-y_lol1cPdIwINmHtMYJA9RvXXwCK8BGAsYHg/s0/2021-02-19.gif"]
#gifs for ham
hamStr = ["https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"]
#gifs for awesome
awesomeStr = ["https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327", "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242"]
#gifs for pussy
pussyStr = ["https://tenor.com/view/alison-brie-alice-sophia-eve-pussy-pretty-beautiful-girl-gif-16850525", "https://i.makeagif.com/media/12-07-2017/gdW2fv.gif"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

def get_random_image():
  url = "https://picsum.photos/200/300?random=" + str(random.randint(0,99))
  return(url)

def compare_crypto(crypto="BTC", currency="USD"):
  price = cryptocompare.get_price(crypto, currency, True)
  return price 

def format_crypto(message):
  formatRetVal = ""
  tag = []

  if message == None:
    for c in crypto_list:
      coin_type = c
      currency_type = "USD"
      retVal = compare_crypto(c, "USD")
      formatRetVal = formatRetVal + coin_type + " to " + currency_type + ": \n" 
      formatRetVal = formatRetVal + "\tCurrent: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["PRICE"]) + "\n"
      formatRetVal = formatRetVal + "\tHour High: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["HIGHHOUR"]) + "\n"
      formatRetVal = formatRetVal + "\tHour Low: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["LOWHOUR"]) + "\n"
    return formatRetVal

  elif len(message.split(" ")) == 1:
      tag = [message.upper().split(" ")[0], "USD"]
  else:
    tag = message.upper().split(" ")
  #print raw 
  if len(tag) > 2:
    if tag[2] == "RAW":
      coin_type = tag[0]
      currency_type = tag[1]
      retVal = compare_crypto(coin_type, currency_type)
      formatRetVal = coin_type + " to " + currency_type + ": \n" 
      formatRetVal = formatRetVal + json.dumps(retVal["DISPLAY"])
  else:
    coin_type = tag[0]
    currency_type = tag[1]
    retVal = compare_crypto(coin_type, currency_type)
    try:
      formatRetVal = coin_type + " to " + currency_type + ": \n" 
      formatRetVal = formatRetVal + "\tCurrent: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["PRICE"]) + "\n"
      formatRetVal = formatRetVal + "\tHour High: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["HIGHHOUR"]) + "\n"
      formatRetVal = formatRetVal + "\tHour Low: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["LOWHOUR"])
    except:
      formatRetVal = "Could not find " + coin_type
  return formatRetVal

def get_image_from_tits():
  val = random.randint(0,len(titsStr)-1)
  img = titsStr[val]
  return img 

def get_image_from_pussy():
  val = random.randint(0,len(pussyStr)-1)
  img = pussyStr[val]
  return img

def get_image_from_awesome():
  val = random.randint(0,len(awesomeStr)-1)
  img = awesomeStr[val]
  return img

def get_image_from_ham():
  val = random.randint(0,len(hamStr)-1)
  img = hamStr[val]
  return img

def get_twitter(msg):
  retVal = ""
  tag = msg.split(" ")    
  query = tag[0]
  
  if query == "#trending":
    woeid = 23424977 #US
    trends = api.trends_place(woeid)
    i = 0
    for value in trends: 
        for trend in value['trends']: 
            if i == 10:
              return retVal
            retVal = retVal + str(i+1) + ": " + trend['name'] + "\n"
            i+=1
  else:
    if any(word.lower() in msg for word in blocked_twitter):
      retVal = "Sorry not going to look that up"
    else:
      for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(3)):
        retVal = retVal + status.text + "\n\n\n"

  return retVal

  