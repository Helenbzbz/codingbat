def front3(str):
  if len(str) <3:
    return str*3
  else:
    a = ''.join([str[0],str[1],str[2]])
    return a*3
