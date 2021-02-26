import os
from replit import db


def database():
  print("====")
  print(os.getenv("REPLIT_DB_URL"))
  db["conversions"] = {
    "crypto":"btc",
    "currency":"usd"
  }
  print("====")
  print(db["conversions"]);