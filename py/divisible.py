def IsDivisible(num):
	if num % 7 == 0 and num % 5 != 0:
		return True
	else:
		return False
			

def DivisibleList(first,last,my_list):
	for num1 in range(first,last):
		if IsDivisible(num1):
			my_list.append(num1)
	return my_list
	

my_list = []
DivisibleList(2000,3200+1,my_list)
print(*my_list, sep='\n')
myList = ','.join(map(str, myList))

for roots, dirs, files in os.walk(r'C:\Users\Jon Wang\Downloads'):
	for file in files:
		if file.endswith(("pom.xml")):
			FileName = os.path.abspath(file)
			print(FileName)
			with open(FileName) as f:
				newText = f.read().replace('3.0.0-u11', '3.0.0-u12')
			with open(FileName, "w") as f:
				f.write(newText)
			print('fjf')
			
