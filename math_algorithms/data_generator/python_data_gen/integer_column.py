import random

class Integer16:

  def __init__(self, min_value, max_value):
    self.min_value = min_value
    self.max_value = max_value

  def generate_value(self):
    return str(random.randint(self.min_value, self.max_value))
