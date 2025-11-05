number=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
while len(number)>0:
    number=number.pop()
    if (number%2==0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)