import os
import json
from coinbase.wallet.clinet import Client
from coinbase.wallet.error import AuthenticationError
import cryptocompare

key = os.getenv('CB-ACCESS-KEY')
secret = os.getenv('CB-ACCESS-SIGN')

client = Client(key,secret)

#Class to access coinbase and other crypto API
class CoinbaseWallet:

  total = 0
  message = []

  def __init__(self):
    try:
      accounts = client.get_accounts()
      for wallet in accounts.data:
        self.message.append(str(wallet['name']) + ' ' + str(wallet['native_balance']))
        value = str(wallet['native_balance']).replace('USD', '')
        self.total += float(value)

      self.message.append('Total Balance: ' + 'USD ' + str(self.total))
      print("\n".join(self.message))
    except AuthenticationError:
      print("Could not authenticate with your Coinbase API.")

  #Get buy rate from coinbase
  def get_rate(currency='BTC', compare="USD"):
    currency_pair = currency + "-" + compare
    rates = client.get_buy_price(currency_pair)
    return rates["data"]

  #get sell rate from coinbase
  def get_buy_price(currency='BTC', compare="USD"):
    currency_pair = currency + "-" + compare
    price = client.get_sell_price(currency_pair)
    return price["data"]

  #call the buy command
  def do_buy(id, amount, currency, payment_method):
    return

  #use cryptocompare API 
  def compare_crypto(crypto="BTC", currency="USD"):
    price = cryptocompare.get_price(crypto, currency, True)
    return price 
  '''
  Get the crypto values/change/percentage/high/low/volume
  Options:
  crypto: symbol for crypto to convert
  currency: Currency symbol to convert crpyto to
  duration: duration to check - options DAY, 24, HOUR 
    DAY: Check the daily difference
    24: Check the 24 hour change
    HOUR: Check the hour difference
  '''
  #get current value 
  def crypto_current_value(self, crypto="BTC", currency="USD",duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    return json.dumps(price["RAW"][crypto][currency]["PRICE"])

  #get total value change
  def crypto_change_total(self, crypto="BTC", currency="USD", duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    if duration.toUpper() == "DAY":
      return json.dumps(price["RAW"][crypto][currency]["CHANGEDAY"])
    if duration.toUpper() == "24":
      return json.dumps(price["RAW"][crypto][currency]["CHANGE24HOUR"])
    if duration.toUpper() == "HOUR":
      return json.dumps(price["RAW"][crypto][currency]["CHANGEHOUR"])
    return 0
      
  #get percentage change
  def crypto_percent(self, crypto="BTC", currency="USD", duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    if duration.toUpper() == "DAY":
      return json.dumps(price["RAW"][crypto][currency]["CHANGEPCTDAY"])
    if duration.toUpper() == "24":
      return json.dumps(price["RAW"][crypto][currency]["CHANGE24HOUR"])
    if duration.toUpper() == "HOUR":
      return json.dumps(price["RAW"][crypto][currency]["CHANGEPCTHOUR"])
    return 0

  #get crypto high value
  def crypto_high(self, crypto="BTC", currency="USD", duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    if duration.toUpper() == "DAY":
      return json.dumps(price["RAW"][crypto][currency]["HIGHDAY"])
    if duration.toUpper() == "24":
      return json.dumps(price["RAW"][crypto][currency]["HIGH24HOUR"])
    if duration.toUpper() == "HOUR":
      return json.dumps(price["RAW"][crypto][currency]["HIGHHOUR"])
    return 0
    
  #get crypto low value
  def crypto_low(self, crypto="BTC", currency="USD", duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    if duration.toUpper() == "DAY":
      return json.dumps(price["RAW"][crypto][currency]["LOWDAY"])
    if duration.toUpper() == "24":
      return json.dumps(price["RAW"][crypto][currency]["LOW24HOUR"])
    if duration.toUpper() == "HOUR":
      return json.dumps(price["RAW"][crypto][currency]["LOWHOUR"])
    return 0

  #get crypto volume
  def crypto_volume(self, crypto="BTC", currency="USD", duration="DAY"):
    price = self.compare_crypto(crypto, currency)
    if duration.toUpper() == "DAY":
      return json.dumps(price["RAW"][crypto][currency]["VOLUMEDAY"])
    if duration.toUpper() == "HOUR":
      return json.dumps(price["RAW"][crypto][currency]["VOLUMEHOUR"])
    return 0
