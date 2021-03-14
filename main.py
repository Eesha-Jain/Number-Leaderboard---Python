from replit import db
import operator

def contains(value):
  for x in db.keys():
    if (db[x] == value):
      return True
  
  return False

def delete():
  for x in db.keys():
    del db[x]

username = input("Enter your username: ")
while (contains(username)):
  username = input("Already exists. Enter another username: ")

num = int(input("Enter a number: "))
while (num >= 2000 or num <= -2000):
  num = int(input("Number needs to be less than 2000 and greater than -2000. Enter another number: "))

db[username] = num

print("------------------------------------")
print("LEADERBOARD")

arr = {}

for x in db.keys():
  arr[x] = int(db[x])

sort = sorted(arr.items(), key=operator.itemgetter(1), reverse=True)

for value,x in sort:
  print(str(x) + ": " + value)