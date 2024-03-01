import pokemon
import random

class Water(pokemon.Pokemon):
  """Represents water Pokemon"""

  def __init__(self, name):
    """call super to set the name and type (fire = 0, water = 1, grass = 2)."""
    
    super().__init__(name, 1)
  
  def get_special_menu(self):
    """Override the get_special_menu for this class."""
    
    return "Choose a Move:\n1. Water Gun\n2. Bubble Beam\nEnter Move: "

  def _special_move(self, opponent, move):
    """Override the _special_move methods for this class."""
    
    if move == 1:
      return self._water_gun(opponent)
    elif move == 2:
      return self._bubble_beam(opponent)
    
  def _water_gun(self, opponent):
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

    return self._name + " shoots " + opponent._name + " with a water gun for " + str(dmg) + " damage." + eff 
  
  def _bubble_beam(self, opponent):
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

    return self._name + " blasts " + opponent._name + " with a BUBBLE BEAM for " + str(dmg) + " damage." + eff 
    
  