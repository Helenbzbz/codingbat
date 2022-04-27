def big_diff(nums):
  diff = 0
  for num in nums:
    a = num
    for b in nums:
      difference = abs(a-b)
      if diff < difference:
        diff = difference
  return diff
