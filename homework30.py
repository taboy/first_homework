import random as r
d = r.randint(1, 10)
print( d )
pi=3.141

a = 1.0
for i in range(d):
    a = a/10.0

print( round(a, d))

count = 0
while a < 1:
    a *= 10
    count += 1

print('pi = ', round(pi, count), '\n')
