import math
def make_pi():
    a= math.pi
    b=str(round(a,2))
    c=b[0:1]+b[2:] 
    return  [int(x) for x in c]

print(make_pi())