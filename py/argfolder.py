import os 
import os.path
import time
import sys
a = str(input("enter the modified line: "))
b = str(input("enter the new line: "))
def folder(a,b):
	for dirpath, dirnames, filenames in os.walk("."):
		for filename in [f for f in filenames if f.endswith("pom.xml")]:
			FileName = os.path.join(dirpath, filename)
			with open(FileName) as f:
				newText = f.read().replace(a, b)
				print(a)
				print(b)
			with open(FileName, "w") as f:
				f.write(newText)


folder(a,b)