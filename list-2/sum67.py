def sum67(nums):
  find_6=False
  sum=0
  for num in nums:
    if(num==6):                 
      find_6=True
      continue
    if(num==7 and find_6 is True): 
      find_6=False
      continue
    if(find_6 is False):          
       sum+=num
  return sum