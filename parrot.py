prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# name = input("Please enter your name: ").lower()
# print(f"\nHello, {name.title()}!")
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt).lower()
# print(f"\nHello, {name.title()}!")

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little taller.")