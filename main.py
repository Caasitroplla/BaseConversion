#This will be where scripts will be imported and run

'''
Step 1 - Divide the decimal number to be converted by the value of the new base
Step 2 - Get the remainder from Step 1 as the rightmost digit (least significant digit) of new base number.
Step 3 - Divide the quotient of the previous divide by the new base
Step 4 - Record the remainder from Step 3 as the next digit (to the left) of the new base number
'''


# hate this arracy would remove it if not necessary
all_chars = [
  '0','1','2','3','4','5','6','7','8','9',
  'A','B','C','D','E','F','G','H','I','J',
  'K','L','M','N','O','P','Q','R','S','T',
  'U','V','W','X','Y','Z'
]