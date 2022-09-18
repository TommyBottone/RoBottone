import requests
import json
import random 
import cryptocompare
import tweepy
import twitter


crypto_list = ["BTC", "ETH", "XRP", "LTC", "XLM", "MANA", "ATOM", "SHIB", "ADA", "BAT", "SUSHI", "HBAR"]

api = twitter.authenticate_twitter()
api_twitter_fancy_d = twitter.authenticate_twitter_fancy_d()

#gifs for nice awesome pop omg cool
nice_str = [
  "https://tenor.com/view/jonah-hill-yay-greek-aldos-gif-7212866",
  "https://tenor.com/view/daddys-home2-daddys-home2gifs-will-ferrell-dear-god-oh-lord-gif-9694391",
  "https://tenor.com/view/omg-holy-crap-mother-of-gif-5431633",
  "https://c.tenor.com/O73IijKloyUAAAAM/nice-south.gif", 
  "https://tenor.com/view/nice-very-nice-gif-4295060", 
  "https://tenor.com/view/nice-nooice-bling-key-and-peele-gif-4294979", 
  "https://tenor.com/view/sam-neill-double-glasses-take-off-shades-off-jurassic-park-gif-16455021", 
  "https://tenor.com/view/taking-glasses-off-gif-9227031",  
  "https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327", 
  "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242",
  "https://gfycat.com/academicunconsciousibadanmalimbe",
  "https://64.media.tumblr.com/tumblr_m8kmmsrUCA1r49x5ro1_400.gifv",
  "https://tenor.com/view/cool-peralta-gif-11062927",
  "https://64.media.tumblr.com/be4422803559ee9ce667f2621c6160d7/tumblr_mrwlfgF2Kx1r67id1o5_250.gif"]
#gifs for pop
pop_str = [
  "https://i.imgur.com/Z56FHaK.gif",
  "https://thumbs.gfycat.com/DefenselessSoulfulJellyfish-small.gif",
  "https://64.media.tumblr.com/963f92eab95222a64f2dcd78fed067dc/tumblr_mk3dpvfXdo1raykwto1_400.gif",
  "https://33.media.tumblr.com/527619f13e6b6fecdf7d28684188f38f/tumblr_mukltkFEPG1qmae8to2_r1_250.gif",
  "https://tenor.com/view/arrested-development-poppop-treat-gif-22319007",
  "https://gfycat.com/focusedshabbyandalusianhorse"
]

#gifs for ham
ham_str = ["https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"]
#gifs for Thankyou
ty_str = ["https://tenor.com/view/leonardo-dicaprio-thank-you-cheers-smile-gif-17045602", "https://tenor.com/view/thanks-thank-you-dwight-gif-3898407", "https://tenor.com/view/the-office-bow-michael-scott-steve-carell-office-gif-12985913", "https://tenor.com/view/thanks-south-park-drive-gif-6088544" ]
#gifs for crash
crash_str = ["https://i.giphy.com/media/xT0Gquis7l8OwC2hRm/giphy.webp"]
#gifs for work
work_str = [
  "https://giphy.com/gifs/memecandy-htpWSilDa2FdgEETvt",
  "https://giphy.com/gifs/filmeditor-movie-set-it-off-l0ErOSwfdlTJEaUq4",
  "https://giphy.com/gifs/julie-work-l4KichZaD8o5vFVNS",
  "https://giphy.com/gifs/funny-movie-work-QK21sAsxnJATS",
  "https://giphy.com/gifs/foxhomeent-3owyoUHuSSqDMEzVRu",
  "https://giphy.com/gifs/work-share-hard-na2v3jKhxosCI",
  "https://giphygifs.s3.amazonaws.com/media/RhEvCHIeZAZ6E/giphy.gif"
]
#gifs for mistake
mistake_str = [
  "https://tenor.com/view/error-the-simpsons-not-found-robot-gif-5012717",
  "https://tenor.com/view/arrested-development-season1-comedy-gob-ive-made-ahuge-mistake-gif-3450456",
  "https://c.tenor.com/vzrYP4mKYA4AAAAM/i-have-made-huge-mistake.gif"
]
#gifs for happybirthday
happy_birthday = [
  "https://i.imgur.com/EWlUSZ9.gif",
  "https://kindyou.com/wp-content/uploads/2018/01/Happy-Birthday-Gif-with-a-Sexy-Girl-4.gif",
  "https://kindyou.com/wp-content/uploads/2018/01/Birthday-Gif-with-a-Hilarious-Dance1.gif",
  "https://bestanimations.com/media/hot-birthday-gifts/1890499373daily-news-hot-birthday-gif.gif",
  "https://bestanimations.com/media/hot-birthday-gifts/1348878474hot-funny-girl-happy-birthday-wishes-for-guy-card-gif.gif",
  "https://c.tenor.com/KnWD3xyzkV4AAAAS/happy-birthday-gifts.gif"
]

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
      formatRetVal = formatRetVal + "\tDay High: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["HIGHDAY"]) + "\n"
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
      formatRetVal = formatRetVal + "\tHour Low: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["LOWHOUR"]) + "\n"
      formatRetVal = formatRetVal + "\tDay High: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["HIGHDAY"]) + "\n"
      formatRetVal = formatRetVal + "\tDay Low: " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["LOWDAY"]) + "\n"
    except:
      formatRetVal = get_image_from_mistake()
  return formatRetVal


def bot_crypto():
  formatRetVal = ""

  for c in crypto_list:
    coin_type = c
    currency_type = "USD"
    retVal = compare_crypto(c, "USD")
    formatRetVal = formatRetVal + coin_type + " to " + currency_type + ": " + json.dumps(retVal["DISPLAY"][coin_type][currency_type]["PRICE"]) + "\n"
    
  return formatRetVal

def get_image_from_ham():
  val = random.randint(0,len(ham_str)-1)
  img = ham_str[val]
  return img

def get_image_from_pop():
  val = random.randint(0,len(pop_str)-1)
  img = pop_str[val]
  return img

nice_str_count_array = []
def get_image_from_nice():
  val = random.randint(0,len(nice_str)-1)
  if val in nice_str_count_array:
    img = get_image_from_nice()
  else:
    img = nice_str[val]
    nice_str_count_array.append(val)

  if len(nice_str_count_array) >= len(nice_str)-1:
    nice_str_count_array.clear()
  return img

def get_image_from_thanks():
  val = random.randint(0, len(ty_str)-1)
  img = ty_str[val]
  return img

def get_image_from_crash():
  val = random.randint(0, len(crash_str)-1)
  img = crash_str[val]
  return img

def get_happy_birthday():
  val = random.randint(0, len(happy_birthday)-1)
  img = happy_birthday[val]
  return img

work_str_count_array = []
def get_image_from_work():
  val = random.randint(0,len(work_str)-1)
  if val in work_str_count_array:
    img = get_image_from_work()
  else:
    img = work_str[val]
    work_str_count_array.append(val)

  if len(work_str_count_array) >= len(work_str)-1:
    work_str_count_array.clear()
  return img

mistake_str_count_array = []
def get_image_from_mistake():
  val = random.randint(0,len(mistake_str)-1)
  if val in mistake_str_count_array:
    img = get_image_from_mistake()
  else:
    img = mistake_str[val]
    mistake_str_count_array.append(val)

  if len(mistake_str_count_array) >= len(mistake_str)-1:
    mistake_str_count_array.clear()
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
      for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(3)):
        retVal.append("@"+status.author.name + ": \n\t" + status.text)

  return retVal

def get_twitter_user(msg):
  retVal = []
  user = msg.split("@")[1]

  retVal.append(user + ": \n\t")
  tweets = api.user_timeline(screen_name = user, count = 3)
  for tweet in tweets:
    retVal.append(tweet._json["text"] + "\n\t")

  return retVal

def send_tweet(msg):
  api.update_status(msg)
  return

def like_it_all(msg):
  user = msg
  if user.startswith("@"):
    user = msg.split("@")[1]
  tweets = api.user_timeline(screen_name = user, count = 50)
  for tweet in tweets:
    try:
      api.create_favorite(tweet.id)
    except:
      continue
  return
  
def send_tweet_fancy_d(msg):
  api_twitter_fancy_d.update_status(msg)
  return

#get twitter message
def get_twitter_message(msg):
  ret_val = ""
    #Check twitter for @
  if msg.startswith("@"):
    tweet_list = get_twitter_user(msg)
    if tweet_list != None:
      for tweet in tweet_list:
        ret_val += tweet + "\n"
  elif msg.startswith("#"):
    tweet_list = get_twitter(msg)
    if tweet_list != None:
      for tweet in tweet_list:
        ret_val += tweet + "\n"
    else:
      ret_val = get_image_from_mistake()
  else:
    msg = "#" + msg
    tweet_list = get_twitter(msg)
    if tweet_list != None:
      for tweet in tweet_list:
        ret_val += tweet + "\n"
        
  if ret_val == "" or ret_val == None:
    ret_val = get_image_from_mistake()

  return ret_val
