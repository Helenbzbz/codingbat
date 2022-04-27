def count_code(str):
  count = 0
  for i in range(len(str)-3):
    cur = str[i:i+4]
    if cur[0:2] == "co" and cur[3] == "e": count += 1
  return count