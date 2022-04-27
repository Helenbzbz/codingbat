def cat_dog(str):
  c = 0
  d = 0
  for i in range(len(str)):
    a = str[i:i+3]
    if a == "cat":
      c +=1    
    if a == "dog":
      d +=1
  return c == d