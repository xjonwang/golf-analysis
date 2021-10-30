pre1 = int(input("enter the lower number: "))
pre2 = int(input("enter the higher number: "))

def IsPerfectSquare(pre1,pre2,square):
	if pre1 and pre2 > 1:
		for i in range(1,pre2+1):
			if square/i == i:
				return True
			else:
				continue
		return False
			
def PerfectSquareList(pre1,pre2,my_list):
	for square in range(pre1,pre2+1):
		if IsPerfectSquare(pre1,pre2,square):
			my_list.append(square)
	return my_list

my_list = []
PerfectSquareList(pre1,pre2,my_list)
print(my_list, sep=' ', end='', flush=True)
		
cube_list = []
for cube in list(map(int, my_list)):
	for x in range(1,cube+1):
		if cube/x**2 == x:
			print(cube,'is a perfect square and a perfect cube')
		else:
			continue
	