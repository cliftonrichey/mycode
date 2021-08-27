#!/usr/bin/env python3
import random

player1_dice = []
player2_dice = []

"""Making a dice game that has a random number of dice for each player"""


x = random.randint(1,6) #making a random number for x
y = random.randint(1,6) #making a random number for y

for i in range(x): #defining the number of rolls with x
  player1_dice.append(random.randint(1,6)) #rolling for 6 numbers

for i in range(y): #defining the number or rolls with y
  player2_dice.append(random.randint(1,6)) #rolling for 6 numbers

print("Player 1 rolled" + str(player1_dice))
print("Player 2 rolled" + str(player2_dice))

if sum(player1_dice) == sum(player2_dice):
  print("Draw")
elif sum(player1_dice) > sum(player2_dice):
  print("Player 1 wins")
else:
  print("Player 2 wins")

