def split_before_each_uppercases(formula):
  if not formula:
    return []

  index = 0
  split_string = []

  for i, char in enumerate(formula):

    if char.isupper() and index < i:
      split_string.append(formula[index:i])
      index = i

  split_string.append(formula[index:])
  
  return split_string

def split_at_first_digit(formula):
  s = ""

  for index, char in enumerate(formula):
    if char.isdigit() == True:
      return (s, int(formula[index:]))
    else:
      s += char
    
  return (s, 1)
