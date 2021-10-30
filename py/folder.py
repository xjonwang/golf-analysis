import os 
import os.path
import time
n = 0 

for dirpath, dirnames, filenames in os.walk("."):
	for filename in [f for f in filenames if f.endswith("pom.xml")]:
		FileName = os.path.join(dirpath, filename)
		with open(FileName) as f:
			newText = f.read().replace('3.0.0-u11', '3.0.0-u12')
		with open(FileName, "w") as f:
			f.write(newText)
		print("Wonton Soup for 2")
#while k <= x.size - 10:
	D = x[k:k + 10]
	H = D - R
	H = H**2
	h = np.sum(H)
	my_array = np.append(my_array, h)
	k = k + 1
				
			
			
				
