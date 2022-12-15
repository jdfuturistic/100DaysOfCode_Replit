print("\033[33m","Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!")

name=input("What is your name?")
enemy=input("What is your worst enemy’s name?")
superpower=input("What is your superpower?")
live=input("Where do you live?")
food=input("What is your favorite food?")

print("\033[32m","Hello ",name,"! Your ability to ","\033[35m",superpower," will make sure you never have to look at ","\033[31m",enemy," again. Go eat ",food," as you walk down the streets of ",live," and use ","\033[35m",superpower,"for good and not evil!")

print("Example")

print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")