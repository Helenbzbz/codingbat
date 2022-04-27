def count_hi(str):
  count = 0
  for i in range(len(str)):
    a = str[i:i+2]
    if a == "hi": count +=1
  return count