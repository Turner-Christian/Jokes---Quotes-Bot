from jokes import jokes_list
from quotes import  quotes_list
import time
import random

def jokeBot():
    print("Do you want to hear a joke?  y/n")
    user_input = input()
    if user_input == "y":
        this_joke = random.choice(jokes_list)
        print("...Ok let me think...")
        time.sleep(2)
        print(this_joke["setup"])
        time.sleep(5)
        print(this_joke["punchline"])
        time.sleep(2)
        print("")
        jokeBot()
    elif user_input == "n":
        print("Sadness....")
    else:
        print("Invalid input")
        jokeBot()

jokeBot()

def quoteBot():
    print("Do you want to hear a quote?  y/n")
    userInput = input()
    if userInput == "y":
        random_quote = random.choice(quotes_list)
        print(random_quote["text"])
        time.sleep(2)
        print(random_quote["author"])
        time.sleep(5)
        print("")
        quoteBot()
    elif userInput == "n":
        print("Sadness....")
    else:
        print("Invalid input")
        quoteBot()
