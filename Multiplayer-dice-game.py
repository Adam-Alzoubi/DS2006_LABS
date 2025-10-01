#Welcome to battle of dices (Multiplayer game)

import random
from Dices import rollD6 , rollD6_repeated

players=["player1" , "player2" , "player3","player4"]

# Initialize variable to track wins
wins = {player: 0 for player in players}
rounds_played= 0
limits = 10

 

while players <10 
    input("Press ENTER to roll the dice...")

    players= rollD6() + rollD6_repeated()

    
    input("\nPress ENTER to continue...")

  
  