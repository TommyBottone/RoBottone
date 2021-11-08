from replit import db

class Meow_Meow_Beans:

  def __init__(self):
    return
      
  def user_exists(self, user_name):
    keys = db.keys()
    
    if user_name.lower() in (key.lower() for key in keys):
      return True 
    else:
      return False

  def add_user(self, user_name):
    if self.user_exists(user_name):
      return

    db[user_name] = 3
    return

  def score_user(self, user_from, user_to, mmb):
    if mmb > 5:
      mmb = 5
    elif mmb < 1:
      mmb = 1

    if user_from == user_to:
      return "self"
    if self.user_exists(user_to):
      db[user_to] = int(mmb)
    else:
      return "dne"

  def get_score(self, user):
    if self.user_exists(user) == True:
      value = db[user]
      if value == 0:
        return "nobeans.png"
      elif value == 1:
        return "1bean.jpg"
      elif value == 2:
        return "2beans.jpg"
      elif value == 3:
        return "3beans.jpg"
      elif value == 4:
        return "4beans.jpg"
      elif value == 5:
        return "5beans.jpg"
        