import string
import time
import random

LOGO = """
          .:'
      __ :'__
   .'`__`-'__``.
  :__________.-'
  :_________:
   :_________`-;
    `.__.-.__.'
"""
print(LOGO)
print("Welcome to my Password Generator!")
letters = string.ascii_letters
numbers = string.digits

count = int(input("How many letters & numbers do you want to generate?: "))
password = "".join(random.choices(letters + numbers, k = count))
print(password)

time.sleep(5)