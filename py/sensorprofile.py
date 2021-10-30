import matplotlib.pyplot as plt
from matplotlib import pylab
import pandas as pd
import numpy as np
from scipy import stats
sensor = pd.read_csv(r'C:\Users\Jon Wang\Downloads\sensorProfile - sensorProfile.csv')
print(sensor)
np_sensor = np.array(sensor)
df_sensor = pd.DataFrame(sensor, columns = ['Trail_1', 'Trail_2', 'Trail_3', 'Trail_4', 'Trail_5'])
print(df_sensor)
T1 = np.array(df_sensor.Trail_1)
T2 = np.array(df_sensor.Trail_2)
T3 = np.array(df_sensor.Trail_3)
T4 = np.array(df_sensor.Trail_4)
T5 = np.array(df_sensor.Trail_5)

T12 = np.append(T1, T2)
T123 = np.append(T12, T3)
T1234 = np.append(T123, T4)
TP = np.append(T1234, T5)
xp = np.arange(np.count_nonzero(T1))
xp1 = np.append(xp, xp)
xp2 = np.append(xp1, xp1)
xval = np.append(xp2, xp)
#print(xval)
#print(TP)
#plt.scatter(xval, TP)
#slope, intercept, r_value, p_value, std_err = stats.linregress(xval, TP)
#line = slope*xval+intercept
#plt.plot(xval, TP, xval, line)
#plt.show()
#graph for mean of the trials
my_array = []
my_array2 = [] 
n = 0
while n <= 170:
	#print(n)
	m = np.mean(sensor.loc[n])
	n = n + 1
	my_array.append(m)
print(my_array)
plt.plot(xp, my_array)
plt.show()
		
#graph for one of the trials
my_array2 = np.array(sensor.Trail_1)
plt.plot(xp, my_array2)
plt.show()

np.convolve(my_array, my_array2)
