import math

#input radius
r = int(input())

#Euclidean geometry
dt = math.pi*r**2

#Taxicab geometry
de = 2*(r**2) #-->1/2*4(r**2)

#output
print(f"{dt:.6f}")
print(f"{de:.6f}")