import abc
import random

class Pokemon(abc.ABC):
  """Represents a pokemon, that is able to perform normal attacks.
  Attributes:
      _name (str)
      _type (int)
      _battle_table (list of int)
      _hp (int)
  """
  
  def __init__(self, name, type):
    """set the _name, and _type using the parameters, assign the _battle_table the 2D list given above, and set _hp to 25."""
    
    self._name = name
    self._type = type
    self._battle_table = [[1, .5, 2],[2, 1, .5], [.5, 2, 1]]
    self._hp = 25
  
  @property
  def hp(self): 
    """use a decorator to get (not set) the value of _hp."""
    
    return self._hp 
  
  def get_normal_menu(self):
    """returns a string with the menu options for the normal moves: slam and tackle."""
    
    return "Choose a Move:\n1. Slam\n2. Tackle\nEnter Move: "

  def _normal_move(self, opponent, move):
    """use the move parameter to choose to call either slam or tackle method, returns the string returned from those methods."""
    
    if move == 1:
      return self._slam(opponent)
    elif move == 2:
      return self._tackle(opponent)

  def _slam(self, opponent):
    """randomize some damage (slam 1-8, tackle 3-6), call take_damage on the opponent and return a string description of the move using both pokemons names, the type of move, and the amount of damage taken."""
    
    dmg = random.randint(1,8)
    opponent._take_damage(dmg)
    return self._name + " SLAMS " + opponent._name + " for " + str(dmg) + " damage. "
    
  def _tackle(self, opponent):
    """randomize some damage (slam 1-8, tackle 3-6), call take_damage on the opponent and return a string description of the move using both pokemons names, the type of move, and the amount of damage taken."""
    
    dmg = random.randint(3,6)
    opponent._take_damage(dmg)
    return self._name + " TACKLES " + opponent._name + " for " + str(dmg) + " damage. "
        
  @abc.abstractmethod
  def get_special_menu(self):
    """abstract (overridden in the subclasses) - returns the menu for the special moves of each type."""
    pass

  @abc.abstractmethod
  def _special_move(self, opponent, move):
    """abstract (overridden in the subclasses) - uses the move parameter to choose to call either of the special moves for that type."""
    pass

  def attack(self, opponent, type, move):
    """use the type parameter to choose to call either _normal_move or _special_move."""
  
    if type == 1:
      return self._normal_move(opponent, move)
    elif type == 2:
      return self._special_move(opponent, move)

  def __str__(self):
    """display the pokemon’s name and hp in the format “Name: hp/25”."""
    
    return self._name + " HP: " + str(self._hp) + "/25" 

  def _take_damage(self, dmg):
    """the damage the pokemon takes.  Subtract the dmg value from the pokemon’s _hp.  Check that the _hp doesn’t go past 0 (if it’s negative, reset it to 0). """
    
    self._hp -= dmg
    if self._hp < 0:
      self._hp = 0