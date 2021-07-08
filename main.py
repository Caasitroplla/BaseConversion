#This will be where scripts will be imported and run

print("hello world")


'''
Step 1 - Divide the decimal number to be converted by the value of the new base
Step 2 - Get the remainder from Step 1 as the rightmost digit (least significant digit) of new base number.
Step 3 - Divide the quotient of the previous divide by the new base
Step 4 - Record the remainder from Step 3 as the next digit (to the left) of the new base number
'''


# hate this arracy would remove it if not necessary
allChars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

allChars = [
  '0','1','2','3','4','5','6','7','8','9',
  'A','B','C','D','E','F','G','H','I','J',
  'K','L','M','N','O','P','Q','R','S','T',
  'U','V','W','X','Y','Z'
]

def normalise(input_value: str, input_value_base: int):

  values = []
  deanary_value = int()

  # Create an array of the values of each character
  for char in input_value:
    # Adds the numerical of each character to the array
    values.append(allChars.index(char)) 

  # Need to iterate through the array in reverse
  for value in reversed(characters):
    # Now for each value we time it by the base to the power of its index then add it to deanary total
    deanary_value += value * (input_value_base ** reversed(characters).index(value))

return deanary_value


def de_normalise(input_value): int, output_base: int):

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



