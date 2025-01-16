def create_xmas_tree(height, ornament):
  num = 2*(height-1) + 1
  result = ( "\n" + ( ((num-1)//2) * "_" ) + "#" + ( ((num-1)//2) * "_" ) ) * 2

  for element in range(0,height):
    result = ( "\n" + ( element * "_" ) + ( ( num - (2 * element) ) * (ornament) ) + ( element * "_" ) ) + result

  return result[1:]
