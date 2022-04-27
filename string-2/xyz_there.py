def xyz_there(str):
  for i in range(len(str)):
    a = str[i:i+4]
    b = str[i+1:i+4]
    c = str[i:i+3]
    return (i == 0 and c == "xyz") or (a != ".xyz" and b == "xyz")
  return False