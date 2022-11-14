from art import logo
import random
import os

clear = lambda: os.system("cls")


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def card_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  print(logo)

  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, score: {user_score} ")
    print(f"Computer's first card: {computer_cards[0]} ")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_deal = input("Type 'y' to get another card, type 'n' to pass:" )
      
      if user_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_cards != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))
    
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare_score(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "Went over, You lose"
    
  if user_score == computer_score:
    return "Draw"
  elif user_score > computer_score:
    return "You Win"
  elif user_score == 0:
    return "You win with a BlackJack!!!"
  elif computer_score == 0:
    return "Lose, opponent has BlackJack!!!"
  elif computer_score > 21:
    return "Opponent went over. You Win."
  elif user_score > 21:
    return "You went over. You Lose."
  else:
    return "You Lose"



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  card_game()
