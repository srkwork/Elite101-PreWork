import time
import random
Bot = "Bot"

print(f"{Bot}: Hi, I am {Bot}!")
time.sleep(2)
name = input(f"{Bot}: What is your name?\n: ")
print(f"{Bot} is typing...")
time.sleep(10)
print(f"{Bot}: Hi {name} it is so nice to meet you")
print(f"{Bot} is typing...")
time.sleep(5)
age = float(input(f"{Bot}: How old are you?\n: "))
Bot_age = random.randint(1,10)
if Bot_age == 1:
  print(f"{Bot} is typing...")
  time.sleep(5)
  print(f"{Bot}: I am {age} year old. I am quite young and I am ready to change the world.")
elif (Bot_age > 1) and (Bot_age < 5):
  print(f"{Bot} is typing...")
  time.sleep(7)
  print(f"{Bot}: I am {Bot_age} years old. I am enjoying helping people!")
elif Bot_age == 5:
  print(f"{Bot} is typing...")
  time.sleep(3)
  print(f"{Bot}: I am {Bot_age} years old. I have lived half of my life.")
elif Bot_age > 5:
  print(f"{Bot} is typing...")
  time.sleep(4)
  print(f"{Bot}: I am {Bot_age} years old. I am old.")
elif Bot_age >= 9:
  print(f"{Bot} is typing...")
  time.sleep(6)
  print(f"{Bot}: I am {Bot_age} years old. I am retired. I loved helping people and changing the world.")

print("Bot is typing...")
time.sleep(5)
favorite_food = input(f"{Bot}: What is your favorite food?: ")
print(f"{Bot} is typing...")
time.sleep(6)
print(f"{Bot}: Wow, sounds very nice")
print(f"{Bot} is typing...")
favorite_animal = input(f"{Bot}: What is your favorite animal?: ")

if favorite_animal == "Dogs":
  print(f"{Bot} is typing...")
  time.sleep(7)
  print(f"{Bot}: Cool! I love {favorite_animal} as well")
else:
  print(f"{Bot} is typing...")
  time.sleep(4)
  print(f"{Bot}: Oh ok. Sounds good")
print(f"{Bot} is typing...")
time.sleep(5)
sports = input(f"{Bot}: Do you play any sports?: ")

if sports == "Yes" or "yes":
  print(f"{Bot} is typing...")
  time.sleep(4)
  favorite_sport = input(f"{Bot}: What is your favorite sport?: ")
  print(f"{Bot} is typing...")
  time.sleep(6)
  print(f"{Bot}: Wow! I also love playing {favorite_sport} as well")
elif sports == "No" or "no":
  print(f"{Bot} is typing...")
  time.sleep(4)
  print(f"{Bot}: Oh ok. No problem")
  print(f"{Bot} is typing...")
  hobby = input(f"{Bot}: What is your favorite hobby?: ")
  print(f"{Bot} is typing...")
  time.sleep(4)
  print(f"{Bot}: Wow! I love to {hobby} too!")

print(f"{name} is typing...")
time.sleep(20)
print(f"{name}: Well Bot it's been a long day for me, and I am very tired. So I am going to sleep. It was nice talking to you. Good Night!")
time.sleep(10)
print(f"{Bot}: Good night {name}. I am sleepy too. I will talk tomorrow. Bye!")