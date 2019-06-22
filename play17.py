import math
x,y=list(map(int,input().split()))
s=math.gcd(x,y)
print((x*y)//s)
