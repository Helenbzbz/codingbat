def xyz_there(str):
  for i in range(len(str)-2):
    if i == 0 and str[i:i+3] == 'xyz':
      return True

    if i > 0:
      if (str[i:i+3]) == 'xyz' and str[i-1:i+3] != '.xyz':
        return True
  return False
  
xyz_there('abcxyz')