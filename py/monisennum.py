pre1 = int(input("enter the lower number: "))
pre2 = int(input("enter the higher number: "))

def isPrimeNum(num):
	if num == 2:
		return True
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				return False
			else:
				return True
				

def primeNumList(first,last, my_list):
	for myNum in range(first,last+1):
		if myNum > 1:
			if isPrimeNum(myNum):
				my_list.append(num)
	return my_list

my_list = []
primeNumList(pre1,pre2,my_list)
print(*my_list, sep='\n')

mon_list = []
for i in list(map(int, my_list)):
	for j in list(map(int, my_list)):
		num = i ** j - 1
		if isPrimeNum(num):
			print(num,"is a monisen number")
			mon_list.append(num)

			
mon_list = []
print(*mon_list, sep='\n')


	