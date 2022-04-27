def front_times(str, n):
  if len(str) <3:
    return str*n
  else:
    a = ''.join([str[0],str[1],str[2]])
    return a*n
