#This will be where scripts will be imported and run
print("hello world")

'''
Step 1 - Divide the decimal number to be converted by the value of the new base
Step 2 - Get the remainder from Step 1 as the rightmost digit (least significant digit) of new base number.
Step 3 - Divide the quotient of the previous divide by the new base
Step 4 - Record the remainder from Step 3 as the next digit (to the left) of the new base number
'''

allChars = [
  '0','1','2','3','4','5','6','7','8','9',
  'A','B','C','D','E','F','G','H','I','J',
  'K','L','M','N','O','P','Q','R','S','T',
  'U','V','W','X','Y','Z'
]

def main():
  pass

def normalise(input, inputBase):

  characters = []

  for char in input:
    characters.append(char) # replace with search function appending place vlaue to array
