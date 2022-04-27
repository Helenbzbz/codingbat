def xyz_there(str):
  for i in range(len(str)-3):
    if i == 0:
      print(str[i:i+3])
      return str[i:i+3] == 'xyz' 
    else:
      a = str[i:i+3]
      b = str[i-1:i+3]
    return a == "xyz" and b != ".xyz"
