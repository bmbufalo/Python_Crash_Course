"""
message = "Hello World!"
print(message)

name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)
bicycles = ['trek', 'cannondatel', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati' 
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
print(sorted(cars,reverse=True))
cars.reverse()
print(cars)
cars.reverse()
count = len(cars)
print(count)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone. That was a great magic show!")


# for value in range(1, 6):
#   print(value)

numbers = list(range(6))
print(numbers)
"""

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#   print(player.title())
# print(players[:4])


""" Slicing lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
"""

""" Tuples

dimensions = (200, 50)
# print(dimensions[0]) = 250
# print(dimensions[1])
print("Original dimensions:")
for dimension in dimensions:
  print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
  print(dimension)

"""

""" If statements


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
"""
# Variables
child = 0
teen = 25
adult = 40
elderly = 20
age = int(input("Enter your age: "))
# Conditionals
if age < 4:
    price = child
elif age < 18:
    price = teen
elif age < 65:
    price = adult
else:
    price = elderly
# Output
print(f"Your admission cost is ${price}.")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'extra cheese', 'french fries']

for requested_topping in requested_toppings:
  if requested_topping in available_toppings:
    print(f"Adding {requested_topping}.")
  else:
    print(f"Sorry, we don't have {requested_topping}.")
    
print("\nFinished making your pizza!")
"""
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#         print("\nFinished making your pizza!")
#         # print("Sorry, we are out of green peppers right now.")
# else:
#         print("Are you sure you want a plain pizza?")

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

"""

# Chapter 6: Dictionaries

