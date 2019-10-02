import random
import string

class Varchar:

  def __init__(self, min_value, max_value):
    self.min_value = min_value
    self.max_value = max_value

  def generate_value(self):
    letters = string.ascii_letters
    random_range = random.randint(self.min_value, self.max_value)
    return ''.join(random.choice(letters) for i in range(random_range))
