import pokemon
import random

class Fire(pokemon.Pokemon):
  """Represents fire Pokemon"""

  def __init__(self, name):
    """call super to set the name and type (fire = 0, water = 1, grass = 2)."""
    
    super().__init__(name, 0)
  
  def get_special_menu(self):
    """Override the get_special_menu for this class."""
    
    return "Choose a Move:\n1. Ember\n2. Fire Blast\nEnter Move: "

  def _special_move(self, opponent, move):
    """Override the _special_move methods for this class, choose between special moves"""
    
    if move == 1:
      return self._ember(opponent)
    elif move == 2:
      return self._fire_blast(opponent)
    
  def _ember(self, opponent):
    """Randomize damage (move1 1-5), look up the multiplier in the battle table based on the two pokemon’s type and calculate the total damage the opposing pokemon will take. Return a string using both pokemons names, type of move, amount of damage taken, and whether it was effective or not. """

    move1 = random.randint(1,5)
    multiplier = self._battle_table[self._type][opponent._type]
    if multiplier == 2:
      eff = "\nIt was SUPER EFFECTIVE!"
    elif multiplier == .5:
      eff = "\nIt was not very effective."
    else:
      eff = ""
    dmg = multiplier * move1
    if dmg % 1 != 0:
      dmg += .5
    dmg = int(dmg)
    opponent._take_damage(dmg)
    
    return self._name + " engulfs " + opponent._name + " in EMBERS for " + str(dmg) + " damage." + eff 
  
  def _fire_blast(self, opponent):
    """Randomize damage (move2 3-4), look up the multiplier in the battle table based on the two pokemon’s type and calculate the total damage the opposing pokemon will take. Return a string using both pokemons names, type of move, amount of damage taken, and whether it was effective or not. """
  
    move2 = random.randint(3,4)
    multiplier = self._battle_table[self._type][opponent._type]
    if multiplier == 2:
      eff = "\nIt was SUPER EFFECTIVE!"
    elif multiplier == .5:
      eff = "\nIt was not very effective."
    else:
      eff = ""
    dmg = multiplier * move2
    if dmg % 1 != 0:
      dmg += .5
    dmg = int(dmg)
    opponent._take_damage(dmg)
    
    return self._name + " BLASTS " + opponent._name + " with FIRE for " + str(dmg) + " damage." + eff 
  