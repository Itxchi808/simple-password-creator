import random
import string

low = list(string.ascii_letters)
high = list(string.ascii_letters+string.punctuation+string.digits)
mid = list(string.digits+string.ascii_letters)

password = ""

print("""
      Please select level.
      
      1) Low
      2) Medium
      3) High
      
      99) Exit
      """)

chose = int(input("> "))

if chose == 99:
    exit()

if chose == 1:
    length = int(input('Length: '))
    for i in range(length):
        password = password+random.choice(low)
    print(password)
if chose == 2:
    length = int(input('Length: '))
    for i in range(length):
        password = password+random.choice(mid)
    print(password)
    
if chose == 3:
    length = int(input('Length: '))
    for i in range(length):
        password = password+random.choice(high)
    print(password)