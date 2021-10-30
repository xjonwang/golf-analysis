b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

for x in range(-b,b+1):
	for y in range(-b,b+1):
		if x + y == b:
			if x * y == c: 
				print(x)
				print(y)
		else:
			continue
		
