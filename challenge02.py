def createFrame(names):
  maxLen = 0

  if not names:
    return '***\n* *\n***'

  for name in names:
    if len(name) > maxLen:
      maxLen = len(name)
    
  result = (maxLen+4) * "*"

  for name in names:
    result += '\n* ' + name + ( (maxLen-len(name)) * " ") + ' *'

  result += '\n'+((maxLen+4) * "*")

  return result
