from random import randint

#adding lives -> when one or the other gets to 0, win / lose
player_lives=5
computer_lives=5
total_lives=5

#basket of choices ARRAY - index 0, 1, 2.
choices=["rock", "paper", "scissors"]

#let AI make a choice
computer=choices[randint(0, 2)]

# Set up a game loop here so we don't have to keep restarting
player = False