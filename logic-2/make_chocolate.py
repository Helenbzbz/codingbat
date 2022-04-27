def make_chocolate(small, big, goal):
  if goal%5 > small:
    return -1
  if small+big*5 < goal:
    return -1
  if goal > big*5:
    return goal-big*5
  return goal%5