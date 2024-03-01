import pokemon
import random

class Grass(pokemon.Pokemon):
  """Represents grass Pokemon"""

  def __init__(self, name):
    """call super to set the name and type (fire = 0, water = 1, grass = 2)."""
    
    super().__init__(name, 2)
  
  def get_special_menu(self):
    """Override the get_special_menu for this class."""
    
    return "Choose a Move:\n1. Razor Leaf\n2. Solar Beam\nEnter Move: "

  def _special_move(self, opponent, move):
    """Override the _special_move methods for this class."""
    
    if move == 1:
      return self._razor_leaf(opponent)
    elif move == 2:
      return self._solar_beam(opponent)
    
  def _razor_leaf(self, opponent):
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
      dmg += 0.5
    dmg = int(dmg)  
    opponent._take_damage(dmg)
    
    return self._name + " slices " + opponent._name + " with RAZOR sharp LEAVES for " + str(dmg) + " damage." + eff 
  
  def _solar_beam(self, opponent):
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
      dmg += 0.5  
    dmg = int(dmg)
    opponent._take_damage(dmg) 

    return self._name + " blasts " + opponent._name + " with a SOLAR BEAM for " + str(dmg) + " damage." + eff 
  