import matplotlib.pyplot as plt
from matplotlib import pylab
import pandas as pd
import numpy as np
sensor = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Stop3Profile.csv')
df_sensor = pd.DataFrame(sensor)
reference = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Stop3Reference.csv')
np_reference = np.array(reference.iloc[:,0])
twelvehunnid_array = np.full((1, len(R)), 1200)
R = twelvehunnid_array - np_reference
#print(R, 'This is R')
index_array = np.array([])
j = 0
while j < df_sensor.shape[1]:
	TT = np.array(df_sensor.iloc[:,j])
	#print(TT, 'This is TP')
	j = j + 1
	k = 0
	my_array = np.array([])
	while k <= TT.size - len(R):
		D = TT[k:k + len(R)]
		#print(D)
		H = D - R
		H = H**2
		h = np.sum(H)
		my_array = np.append(my_array, h)
		k = k + 1
		my_arrayl = list(my_array)
		#print(min(my_array), 'This is the min value')
		#print(my_arrayl.index(min(my_array)), 'This is the index')
		if k == TT.size - len(R):
			my_array1 = list(my_array)
			min_index = my_array1.index(min(my_array))
			index_array = np.append(index_array, min_index)
print(index_array, 'This is index array')