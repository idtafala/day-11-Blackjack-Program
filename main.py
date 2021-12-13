from art import logo
import random
from replit import clear


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

play = True


def compare(score1 , score2 , player , dealer):
  if score1 == score2 :
    print(f"Your final hand : {player} : final score : {score1}")
    print(f"Computer's final hand: {dealer} : final score : {score2}")
    print("draw \U0001F606")
  elif score1 > score2 and score1 <22 :
    print(f"Your final hand : {player} : final score : {score1}")
    print(f"Computer's final hand: {dealer} : final score : {score2}")
    print("you win \U0001f600")
  elif score2 > 21 :
    print(f"Your final hand : {player} : final score : {score1}")
    print(f"Computer's final hand: {dealer} : final score : {score2}")
    print("you win \U0001f600")
  else :
    print(f"Your final hand : {player} : final score : {score1}")
    print(f"Computer's final hand: {dealer} : final score : {score2}")
    print("you lose \U0001F923")


def game() :
  print(logo)
  cards_play= cards
  player = []
  dealer =[]

  #player cards :
  for x in range(0,2) :
    x1 = random.choice(cards_play)
    cards_play.remove(x1)
    player.append(x1)

  #dealer first card :
  for y in range(0,2) :
    y1 = random.choice(cards_play)
    cards_play.remove(y1)
    dealer.append(y1)


  score1 = sum(player)
  score2 = sum(dealer)

  #starting the game 
  print(f"Your cards : {player} , current score : {score1}")
  print(f"Computer's first card : {dealer[0]}")
  print(dealer)


  #hit or stand :
  another_card =""
  while not (another_card == "y" or another_card =="n") :
    another_card = input("Type'y' to get another card, type 'n' to pass :")
  
  def new_card_dealer(score2) :
    while score2 <16 :
        y2 = random.choice(cards_play)
        cards_play.remove(y2)
        dealer.append(y2)
        return sum(dealer)

  if another_card == "y" :
    again = True
    while again == True :
      x1 = random.choice(cards_play)
      cards_play.remove(x1)
      player.append(x1)
      score1 = sum(player)
      print(f"Your cards : {player} , current score : {score1}")
      print(f"Computer's first card : {dealer[0]}")
      if score1 > 21 :
        print("You lose !")
        again = False
      else : 
        another_card =""
        while not (another_card == "y" or another_card =="n") :
          another_card = input("Type'y' to get another card, type 'n' to pass :")
          if another_card == "n" :
            again = False
  
  if another_card == "n" :
    if 11 in dealer and score2 >21 :
      dealer[dealer.index(11)] = 1
      compare(score1 , score2 , player , dealer)

    elif score2 < 16 :
      score2 = new_card_dealer(score2)
      compare(score1 , score2 , player , dealer)
    else :
      compare(score1 , score2 , player , dealer) 

  cards_play = cards   
# main function 
while(play == True) :
  start = input("Do you want to play a game of Blackjack? Type 'y' or 'n'") 
  if  start == "y":
    clear()
    game()
  else : 
    clear()
    play = False
    
  
