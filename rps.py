import random
import os
import time
compliments = ["great job!", "well done!", "nice round!"]
insults = ["loser!", "your loss!", "no luck I guess?", "bad try!"]
botMoves = ["ROCK", "PAPER", "SCISSORS"]
print("Welcome to Rock Paper Scissors.\nYou will be playing against a bot!")
while True:
    time.sleep(5)
    os.system('cls')
    playerMove = input("Put in your move (Rock, Paper or Scissors) ").upper()
    print("You picked " + playerMove+ "\n")
    print("Rock")
    time.sleep(0.5)
    print("Paper")
    time.sleep(0.5)
    print("Scissors")
    time.sleep(0.5)
    print("Shoot!")
    time.sleep(0.5)
    os.system('cls')
    insult = random.choice(insults)
    compliment = random.choice(compliments)
    botMove = random.choice(botMoves)
    if botMove == playerMove:
        print(botMove + " is equal to " + playerMove + " It's a tie!")
        pass
    elif playerMove == "ROCK" and botMove == "PAPER":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Paper beats rock, "+ insult)
        pass
    elif playerMove == "ROCK" and botMove == "SCISSORS":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Rock beats siccors, "+ compliment)
        pass
    elif playerMove == "PAPER" and botMove == "SCISSORS":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Scissors beat paper, "+ insult)
        pass
    elif playerMove == "PAPER" and botMove == "ROCK":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Paper beats rock, " + compliment)
    elif playerMove == "SCISSORS" and botMove == "PAPER":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Scissors beats paper, " + compliment)
    elif playerMove == "SCISSORS" and botMove == "ROCK":
        print("Your move: "+ playerMove + "\n" + "Bot move: " + botMove +"\n\n")
        print("Rock beats siccors, " + insult)
    else:
        print("Error 404" + playerMove + " not found!")
        time.sleep(1)
        os.system('cls')
        pass





