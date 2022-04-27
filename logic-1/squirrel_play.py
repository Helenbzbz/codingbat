def squirrel_play(temp, is_summer):
  if 60<= temp <= 90 and not is_summer:
    return True
  if 60<= temp <= 100 and is_summer:
    return True
  return False