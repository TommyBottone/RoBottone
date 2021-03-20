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
api_twitter_fancy_d = twitter.authenticate_twitter_fancy_d()

#gifs for tits
titsStr = [
  "https://media1.giphy.com/media/l0HlK3RyTkaJIfRJu/giphy.gif",
  "https://media1.tenor.com/images/e257c0306583a544a6f86a7904b6c37b/tenor.gif?itemid=3529236",
  "https://lh3.googleusercontent.com/-cySiOTXr73s/YDAKin4bk3I/AAAAAAAAHZM/GTfX_9-y_lol1cPdIwINmHtMYJA9RvXXwCK8BGAsYHg/s0/2021-02-19.gif", 
  "https://tenor.com/view/boobs-bra-bounce-nice-hot-gif-15574009", "https://tenor.com/view/bounce-wink-boobs-gif-14988779",
 "https://tenor.com/view/busty-bounce-braless-gif-18275184", "https://tenor.com/view/bounce-bouncing-bouncy-wiggle-jiggle-gif-17035985",
 "https://tenor.com/view/sexy-sex-ahaha-gif-18162626", 
 "https://tenor.com/view/sexy-boobs-tits-hot-girl-dance-gif-15335472",
 "https://tenor.com/view/fembots-tits-sparks-fire-gif-16745917", 
 "https://tenor.com/view/hannahpalmer-hannahcpalmer-tiktok-sexy-sexy-girl-gif-19691102",
 "https://tenor.com/view/hannahpalmer-hannahcpalmer-tiktok-sexy-sexy-girl-gif-19691094", 
 "https://tenor.com/view/red-head-sabrina-lynn-gif-18884669", 
 "https://tenor.com/view/abell46s-reface-abell46s-sexy-abell46s-funny-sexy-gif-20364002",
 "https://tenor.com/view/alexis-ren-hot-gif-18055637", 
 "https://tenor.com/view/hannahpalmer-hannahcpalmer-tiktok-sexy-sexy-girl-gif-19691102",
 "https://steamuserimages-a.akamaihd.net/ugc/827950579297074612/574A69734C55E373E7ECF38BBDC6FD025D753CC2/",
 "https://imgur.com/OXrt9ZG",
 "https://i.pinimg.com/originals/1a/34/ae/1a34ae4726f2c42e359a3e81dcc23fb5.gif",
 "https://s3-us-west-2.amazonaws.com/hispotion-prod/wp-content/uploads/2012/05/Kate-Upton-Cat-Daddy-GIF_6.gif",
 "https://i.gifer.com/47hx.gif"
 ]

#gifs for ham
hamStr = ["https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"]
#gifs for awesome
awesomeStr = ["https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327", "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242"]
#gifs for pussy
pussyStr = ["https://tenor.com/view/alison-brie-alice-sophia-eve-pussy-pretty-beautiful-girl-gif-16850525", "https://i.makeagif.com/media/12-07-2017/gdW2fv.gif", "https://tenor.com/view/cat-kitty-kitten-money-slap-gif-4987644", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/good-morning-funny-animals-insomnia-cat-tired-crazy-cute-gif-11458685", "https://tenor.com/view/cat-sneaking-mountain-gif-5074481", "https://tenor.com/view/keyboard-cat-gif-3955335","https://tenor.com/view/cute-cat-kitten-kitty-pussy-cat-gif-17582631",
"https://i.pinimg.com/originals/5d/50/96/5d50964c25f8ce13e5531c60892c03dd.gif"]
#gifs for nice
niceStr = ["https://c.tenor.com/O73IijKloyUAAAAM/nice-south.gif", "https://tenor.com/view/nice-very-nice-gif-4295060", "https://tenor.com/view/nice-nooice-bling-key-and-peele-gif-4294979", "https://c.tenor.com/5u1KCEpdPqMAAAAM/community-poppop.gif", "https://tenor.com/view/sunglasses-tom-cruise-smile-sun-glass-smooth-gif-8129044"]
#gifs for omg
omgStr = ["https://tenor.com/view/sam-neill-double-glasses-take-off-shades-off-jurassic-park-gif-16455021", "https://tenor.com/view/taking-glasses-off-gif-9227031"] 
#gifs for Thankyou
tyStr = ["https://tenor.com/view/leonardo-dicaprio-thank-you-cheers-smile-gif-17045602", "https://tenor.com/view/thanks-thank-you-dwight-gif-3898407", "https://tenor.com/view/the-office-bow-michael-scott-steve-carell-office-gif-12985913", "https://tenor.com/view/thanks-south-park-drive-gif-6088544" ]
#gifs for crash
crashStr = ["https://i.giphy.com/media/xT0Gquis7l8OwC2hRm/giphy.webp"]

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

def get_image_from_nice():
  val = random.randint(0, len(niceStr)-1)
  img = niceStr[val]
  return img

def get_image_from_omg():
  val = random.randint(0, len(omgStr)-1)
  img = omgStr[val]
  return img

def get_image_from_thanks():
  val = random.randint(0, len(tyStr)-1)
  img = tyStr[val]
  return img

def get_image_from_crash():
  val = random.randint(0, len(crashStr)-1)
  img = crashStr[val]
  return img

def get_twitter(msg):
  retVal = []
  tag = msg.split(" ")    
  query = tag[0]
  
  if query == "#trending":
    woeid = 23424977 #US
    trends = api.trends_place(woeid)
    i = 0
    return_list = ""
    for value in trends: 
        for trend in value['trends']: 
            if i == 10:
              retVal.append(return_list)
              return retVal
            return_list = return_list + str(i+1) + ": " + trend['name'] + "\n"
            i+=1
  else:
    if any(word.lower() in msg for word in blocked_twitter):
      retVal.append("Sorry not going to look that up")
    else:
      for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(3)):
        retVal.append("@"+status.author.name + ": \n\t" + status.text)

  return retVal


def get_twitter_user(msg):
  user = msg.split("@")[1]
  retVal = []
  retVal.append(user + ": \n\t")
  tweets = api.user_timeline(screen_name = user, count = 3)
  for tweet in tweets:
    retVal.append(tweet._json["text"] + "\n\t")

  return retVal


def send_tweet(msg):
  api.update_status(msg)
  return
  
def send_tweet_fancy_d(msg):
  api_twitter_fancy_d.update_status(msg)
  return