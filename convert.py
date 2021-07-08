from main import normalise


def normalise(input_value: str, input_value_base: int):

  values = []
  deanary_value = int()

  # Create an array of the values of each character
  for char in input_value:
    # Adds the numerical of each character to the array
    values.append(all_chars.index(char)) 

  # Need to iterate through the array in reverse
  for value in reversed(values):
    # Now for each value we time it by the base to the power of its index then add it to deanary total
    deanary_value += value * (input_value_base ** reversed(values).index(value))

  return deanary_value


def de_normalise(input_value: int, output_base: int):

  values = []

  # First we need to find the first power of the base thats above the input_value
  power = 0
  while input_value < output_base ** power:
    # Increases the power by until its greater than the input_value
    power += 1

  # Go through every power seeing if it can be taken from the input_value (also need to do it in reverse greatest power first)
  for i in range(power, 0):
    if output_base ** i < input_value:
      input_value -= (output_base ** i)

  # Im stuck this is just going to binary at this point with different base

def convert(value, targetBase, base: int=10):
    if base != 10:
        normalise