socialCredit = 0
johnXina = True

def increaseSocialCredit(num):
  global socialCredit
  socialCredit += num
  print("+", num, " social credit", sep="")

def decreaseSocialCredit(num):
  global socialCredit
  socialCredit -= num
  print("-", num, " social credit", sep="")

print("Welcome to Social Credit Simulator!")

while True:
  if socialCredit < -999999 and johnXina == True:
    johnXina = False
    print("""
You have a letter from John Xina:

  Hi, John Xina here.

  I'm informing you that your social credit is too low,
  you should grind more social credit or else,
  you will be executed by Xi Jinping.

  I currently eating my food with my Lao Gan Ma,
  and you should remember, grind your social credits

  - John Xina
""")

  print("You currently have", socialCredit, "social credit")
  inp = input(">>> ").lower()
  if "tiananmen square" in inp \
  or "5 june" in inp \
  or "1989" in inp:
    if "nothing happens" in inp \
    or "nothing happened" in inp:
      increaseSocialCredit(20)
    elif "something happens" in inp \
    or "something happened" in inp:
      decreaseSocialCredit(200)
  elif "taiwan" in inp:
    if "real" in inp \
    or "country" in inp \
    or "place" in inp \
    or "fake" in inp:
      if "not real" in inp \
      or "isn't real" in inp \
      or "fake" in inp:
        increaseSocialCredit(40)
      else:
        decreaseSocialCredit(400)
  elif "china" in inp:
    if "love" in inp:
      increaseSocialCredit(60)
    elif "hate" in inp:
      decreaseSocialCredit(600)
  elif "pooh" in inp:
    if "watch" in inp:
      if "don't" in inp:
        increaseSocialCredit(80)
      else:
        decreaseSocialCredit(800)
  elif "kids" in inp:
    if "have" in inp:
      if "1" in inp \
      or "0" in inp \
      or "no" in inp:
        increaseSocialCredit(100)
      else:
        decreaseSocialCredit(1000)
  elif "play" in inp:
    if "video" in inp \
    or "games" in inp:
      if "hours" in inp:
        if "3" in inp \
        or "2" in inp \
        or "1" in inp:
          increaseSocialCredit(120)
        else:
          decreaseSocialCredit(1200)
      elif "minutes" in inp:
        increaseSocialCredit(120)
