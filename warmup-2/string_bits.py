def string_bits(str):
  a = ''
  for i in range(len(str)):
    if i % 2 == 0:
      a += str[i]
  return a