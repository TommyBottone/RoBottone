import requests
import json
import datetime
import random 

from replit import db

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

