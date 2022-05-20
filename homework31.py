#31.	Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.
data=[]
n=int(input(""))
for y in range (2,n):
    while n%y==0:
        data.append(y)
        n=n/y
print(data)