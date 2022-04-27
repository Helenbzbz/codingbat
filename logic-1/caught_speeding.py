def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed >= 81 + 5:
      return 2
    elif speed >= 61 + 5 and speed <= 80 + 5:
      return 1
    else:
      return 0
  else:
    if speed >= 81:
      return 2
    elif speed >= 61 and speed <= 80:
      return 1
    else:
      return 0