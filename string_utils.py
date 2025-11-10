def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  s = ""

  for index, char in enumerate(formula):
    if char.isdigit() == True:
      return (s, int(formula[index:]))
    else:
      s += char
    
  return (s, 1)
