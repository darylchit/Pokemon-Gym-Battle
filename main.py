#Menghak Leev and Daryl Chit
#03/14/2023
#Pokémon Gym Battle - a game where the user must defeat three pokémon to win the game.

import random
import check_input
import fire
import water
import grass

def main():
#sets gym leader's random Pokemon
  gym_leaderList = [0, 0, 0]
  gym_leader = random.randint(0,2)
  if gym_leader == 0:
    gym_leader_type = "FIRE"
    gym_leaderList = [fire.Fire("Vulpix"), fire.Fire("Ninetales"), fire.Fire("Growlithe")]
  elif gym_leader == 1:
    gym_leader_type = "WATER"
    gym_leaderList = [water.Water("Wartortle"), water.Water("Psyduck"), water.Water("Poliwag")]
  elif gym_leader == 2:
    gym_leader_type = "GRASS"
    gym_leaderList = [grass.Grass("Oddish"), grass.Grass("Bellsprout"), grass.Grass("Exeggcute")]

#Takes user input to choose our own Pokemon
  print("PROF OAK: Hello Trainer! Today you're off to fight your first gym battle of 1 vs. 3 " + gym_leader_type + " pokemon.")
  player = check_input.get_int_range("Select the pokemon that you will fight with.\n1. I choose you, Charmander.\n2. Squirtle! GO!\n3. We can do it, Bulbasaur!\nPlease choose a pokemon: ", 1, 3) - 1 
  print()
  
  if player == 0:
    player = fire.Fire("Charmander")
  elif player == 1:
    player = water.Water("Squirtle")
  elif player == 2:
    player = grass.Grass("Bulbasaur")

  print("  -- GYM BATTLE --  ")

  #Loop that continues the game until user has defeated all three pokemon, or until the user’s pokemon is defeated. 
  while not len(gym_leaderList) == 0 and player.hp != 0:
    opponent = gym_leaderList[0]
    while opponent.hp != 0 and player.hp != 0:
      print("GYM LEADER: I choose you:\n" + str(opponent) + "\n\n" + str(player))
      #Choose between normal or special attack)
      type = check_input.get_int_range("Choose an Attack Type:\n1. Normal\n2. Special\nEnter attack type: ", 1, 2)
      print()
      #Based on their option before, displays menus of normal or special attacks and takes input for which attack to use.
      if type == 1:
        move = check_input.get_int_range(player.get_normal_menu(), 1, 2)
        print()
      elif type == 2:
        move = check_input.get_int_range(player.get_special_menu(), 1, 2)
        print()
  
      print(player.attack(opponent, type, move))

    #Randomizes Gym Leader's attacks while the Gym Leader still has HP. 
      if opponent.hp > 0:
        print(opponent.attack(player, random.randint(1, 2), random.randint(1, 2)) + "\n")
      #When one of the gym leader’s pokemon is defeated, remove it from the list. 
      else:
        print("GYM LEADER: NOOOOO! You defeated my pokemon!\n")
        gym_leaderList.pop(0)

  #Display a message when the user wins/loses.
  if len(gym_leaderList) == 0:
    print("YOU WON! You defeated the gym leader.")
  elif player.hp == 0:
    print("You lose...")

main()
   
