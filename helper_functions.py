import requests
import json
import datetime
import random 
import cryptocompare
import tweepy
import twitter

from replit import db
#blocked twitter words
blocked_twitter = ["sex", "tits", "pussy", "gay", "lesbian", "titty", "ass", "nude", "naked", "girlsgonewild", "porn", "pawg", "nsfw", "fuck", "shit", "crap", "damn", "dammit", "fucking", "shitty", "cunt", "bitch", "bastard"]
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


def get_playlist_name():
    today = datetime.datetime.now()
    playlist_name = today.strftime("%b") + today.strftime("%Y")
    return (playlist_name)


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
        botify_str = "$botify add " + content + " $to " + get_playlist_name(
        ) + "\n"
    elif arg == "queue":
        botify_str = "$botify queue " + content + "\n"
    elif arg == "create":
        botify_str = "$botify create " + get_playlist_name() + "\n"
    return (botify_str)

def compare_crypto(crypto="BTC", currency="USD"):
  price = cryptocompare.get_price(crypto, currency, True)
  return price 

def format_crypto(message):
  formatRetVal = ""
  tag = []
  if message == None or len(message.split(" ")) < 2:
    formatRetVal = "format: $crypto (COIN_TYPE) (CURRENCY_TYPE) (optional:RAW)"
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
      formatRetVal = "format: $crypto (COIN_TYPE) (CURRENCY_TYPE) (optional:RAW)"
  else:
    coin_type = tag[0]
    currency_type = tag[1]
    retVal = compare_crypto(coin_type, currency_type)
    formatRetVal = coin_type + " to " + currency_type + ": \n" 
    formatRetVal = formatRetVal + "\tCurrent: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["PRICE"]) + "\n"
    formatRetVal = formatRetVal + "\tHour High: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["HIGHHOUR"]) + "\n"
    formatRetVal = formatRetVal + "\tHour Low: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["LOWHOUR"])
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