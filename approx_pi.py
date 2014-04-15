import random

m = 0
size = 1000
n = 0
x = 0
y = 0

while n<size:
	x = random.random()
	y = random.random()
	if(((x**2)+(y**2))<=1):
		m+=1
	n+=1

print(4*(m/size))