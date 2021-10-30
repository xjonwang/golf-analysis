pre1 = int(input("enter the lower number: "))
pre2 = int(input("enter the higher number: "))

def isPrimeNum(num):
	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				return False
			else:
				return True
				

def primeNumList(first,last, my_list):
	for num in range(first-1,last+1):
	    print("num is ", num)
		if num > 1:
			if isPrimeNum(num):
				my_list.append(num)
	return my_list

my_list = []
primeNumList(pre1,pre2,my_list)
print(*my_list, sep='\n')