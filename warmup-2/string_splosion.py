def string_splosion(str):
  a = list()
  for i in range(len(str)):
    a += str[:i+1]
  return ''.join(a)