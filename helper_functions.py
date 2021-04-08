import requests
import json
import random 
import cryptocompare
import tweepy
import twitter

#blocked twitter words
blocked_twitter = ["sex", "tits", "pussy", "gay", "lesbian", "titty", "ass", "nude", "naked", "girlsgonewild", "porn", "pawg", "nsfw", "fuck", "shit", "crap", "damn", "dammit", "fucking", "shitty", "cunt", "bitch", "bastard"]

crypto_list = ["BTC", "ETH", "ADA", "XRP", "LTC", "DOGE", "MANA", "ATOM", "SUSHI", "ADA", "BAT"]

api = twitter.authenticate_twitter()
api_twitter_fancy_d = twitter.authenticate_twitter_fancy_d()

#gifs for tits
tits_str = [
  "https://imgur.com/OXrt9ZG",
  "https://i.gifer.com/47hx.gif",
  "https://i.redd.it/ut1co24vhoo61.gif",
  "https://tenor.com/view/neekolul-gif-18144977",
  "https://tenor.com/view/sexy-sex-ahaha-gif-18162626",
  "https://tenor.com/view/alexis-ren-hot-gif-18055637",   
  "https://tenor.com/view/bounce-wink-boobs-gif-14988779",
  "https://tenor.com/view/busty-bounce-braless-gif-18275184",
  "https://tenor.com/view/red-head-sabrina-lynn-gif-18884669", 
  "https://media1.giphy.com/media/l0HlK3RyTkaJIfRJu/giphy.gif",
  "https://giphy.com/gifs/sexy-michelle-jenneke-CyIkFYHRZYkHS",
  "https://thumbs.gfycat.com/SardonicComplexGrunion-mobile.mp4",
  "https://tenor.com/view/cosplay-korean-hot-asian-gif-18522415",
  "https://tenor.com/view/fembots-tits-sparks-fire-gif-16745917",
  "https://tenor.com/view/boobs-bra-bounce-nice-hot-gif-15574009", 
  "https://tenor.com/view/vickyli-asian-sexy-hot-glasses-gif-8841599",
  "https://tenor.com/view/sexy-boobs-tits-hot-girl-dance-gif-15335472",
  "https://tenor.com/view/bikini-japanese-girl-beach-sexy-gif-18235976",
  "https://tenor.com/view/bounce-bouncing-bouncy-wiggle-jiggle-gif-17035985",
  "https://i.pinimg.com/originals/1a/34/ae/1a34ae4726f2c42e359a3e81dcc23fb5.gif",
  "https://tenor.com/view/neekolul-saree-pallu-navel-play-indian-girl-gif-18337461",
  "https://gfycat.com/assuredscrawnybergerpicard-sophie-mudd-celebrity-bikini-beach",
  "https://tenor.com/view/hannahpalmer-hannahcpalmer-tiktok-sexy-sexy-girl-gif-19691102",
  "https://tenor.com/view/abell46s-reface-abell46s-sexy-abell46s-funny-sexy-gif-20364002",
  "https://media1.tenor.com/images/e257c0306583a544a6f86a7904b6c37b/tenor.gif?itemid=3529236",
  "https://78.media.tumblr.com/e119d840f7361f53926373f187ad5d64/tumblr_pf17ouj29E1u2ragso4_1280.gif",
  "https://townsquare.media/site/390/files/2016/07/Zoe-Saldana-black-bra-and-panties.gif?w=600&h=338&q=75",
  "https://s3-us-west-2.amazonaws.com/hispotion-prod/wp-content/uploads/2012/05/Kate-Upton-Cat-Daddy-GIF_6.gif",
  "https://lh3.googleusercontent.com/-cySiOTXr73s/YDAKin4bk3I/AAAAAAAAHZM/GTfX_9-y_lol1cPdIwINmHtMYJA9RvXXwCK8BGAsYHg/s0/2021-02-19.gif",
  "https://thechive.com/wp-content/uploads/2018/12/hooters-and-howitzers-are-the-perfect-holiday-gif-24.gif?attachment_cache_bust=2698007&w=307"  
]
#gifs for omg
omg_str = ["https://tenor.com/view/jonah-hill-yay-greek-aldos-gif-7212866",
"https://tenor.com/view/daddys-home2-daddys-home2gifs-will-ferrell-dear-god-oh-lord-gif-9694391",
"https://tenor.com/view/omg-holy-crap-mother-of-gif-5431633"]
#gifs for ham
ham_str = ["https://tenor.com/view/30rock-sherri-shepherd-ham-gif-5281096"]
#gifs for awesome
awesome_str = [
  "https://tenor.com/view/workaholics-tight-butthole-hole-butt-gif-8279327", 
  "https://tenor.com/view/tight-cool-tightbutthole-butthole-workaholics-gif-5956242",
  "https://gfycat.com/academicunconsciousibadanmalimbe",
  "https://64.media.tumblr.com/tumblr_m8kmmsrUCA1r49x5ro1_400.gifv",
  "https://tenor.com/view/cool-peralta-gif-11062927"
  ]
#gifs for pussy
pussy_str = ["https://tenor.com/view/alison-brie-alice-sophia-eve-pussy-pretty-beautiful-girl-gif-16850525", "https://i.makeagif.com/media/12-07-2017/gdW2fv.gif", "https://tenor.com/view/cat-kitty-kitten-money-slap-gif-4987644", "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", "https://tenor.com/view/good-morning-funny-animals-insomnia-cat-tired-crazy-cute-gif-11458685", 
"https://tenor.com/view/cat-sneaking-mountain-gif-5074481", "https://tenor.com/view/keyboard-cat-gif-3955335","https://tenor.com/view/cute-cat-kitten-kitty-pussy-cat-gif-17582631",
"https://i.pinimg.com/originals/5d/50/96/5d50964c25f8ce13e5531c60892c03dd.gif"]
#gifs for nice
nice_str = ["https://c.tenor.com/O73IijKloyUAAAAM/nice-south.gif", 
"https://tenor.com/view/nice-very-nice-gif-4295060", "https://tenor.com/view/nice-nooice-bling-key-and-peele-gif-4294979", "https://tenor.com/view/sam-neill-double-glasses-take-off-shades-off-jurassic-park-gif-16455021", 
"https://tenor.com/view/taking-glasses-off-gif-9227031"] 
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
#gifs for pop
pop_str = ["https://64.media.tumblr.com/be4422803559ee9ce667f2621c6160d7/tumblr_mrwlfgF2Kx1r67id1o5_250.gif",
"https://33.media.tumblr.com/527619f13e6b6fecdf7d28684188f38f/tumblr_mukltkFEPG1qmae8to2_r1_250.gif",
"https://i.imgur.com/Z56FHaK.gif",
"https://64.media.tumblr.com/963f92eab95222a64f2dcd78fed067dc/tumblr_mk3dpvfXdo1raykwto1_400.gif"]


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
      formatRetVal = "Could not find " + coin_type
  return formatRetVal

tits_str_count_array = []
def get_image_from_tits():
  val = random.randint(0,len(tits_str)-1)
  if val in tits_str_count_array:
    img = get_image_from_tits()
  else:
    img = tits_str[val]
    tits_str_count_array.append(val)

  if len(tits_str_count_array) >= len(tits_str)-1:
    tits_str_count_array.clear()
  return img

def get_image_from_pussy():
  val = random.randint(0,len(pussy_str)-1)
  img = pussy_str[val]
  return img


awesome_str_count_array = []
def get_image_from_awesome():
  val = random.randint(0,len(awesome_str)-1)
  if val in awesome_str_count_array:
    img = get_image_from_awesome()
  else:
    img = awesome_str[val]
    awesome_str_count_array.append(val)

  if len(awesome_str_count_array) >= len(awesome_str)-1:
    awesome_str_count_array.clear()
  return img

def get_image_from_ham():
  val = random.randint(0,len(ham_str)-1)
  img = ham_str[val]
  return img

def get_image_from_nice():
  val = random.randint(0, len(nice_str)-1)
  img = nice_str[val]
  return img

def get_image_from_omg():
  val = random.randint(0, len(omg_str)-1)
  img = omg_str[val]
  return img

def get_image_from_thanks():
  val = random.randint(0, len(ty_str)-1)
  img = ty_str[val]
  return img

def get_image_from_crash():
  val = random.randint(0, len(crash_str)-1)
  img = crash_str[val]
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

pop_str_count_array = []
def get_image_from_pop():
  val = random.randint(0,len(pop_str)-1)
  if val in pop_str_count_array:
    img = get_image_from_pop()
  else:
    img = pop_str[val]
    pop_str_count_array.append(val)

  if len(pop_str_count_array) >= len(pop_str)-1:
    pop_str_count_array.clear()
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
      retVal.append("Sorry, not going to look that up")
    else:
      for i, status in enumerate(tweepy.Cursor(api.search, q=query).items(3)):
        retVal.append("@"+status.author.name + ": \n\t" + status.text)

  return retVal


def get_twitter_user(msg):
  retVal = []
  if any(word.lower() in msg for word in blocked_twitter):
    retVal.append("Sorry, not going to look that up")
  else:
    user = msg.split("@")[1]

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