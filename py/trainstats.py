import numpy as np
import pandas as pd
import time
import random
import matplotlib.pyplot as plt
stopd = np.round(np.random.normal(3.5, 1, 100), 3)
statmodel = stopd
print(stopd)
std = np.std(stopd)
mean = np.mean(stopd)
median = np.median(stopd) 
n = 0
d = 0
b = np.mean(stopd)
c = np.std(stopd)
m100 = np.array([])
s100 = np.array([])
d100 = np.array([])
stopd2 = stopd
statmodel2 = stopd
p = 0
msm100 = np.array([])
ssm100 = np.array([])
psm100 = np.array([])
while d < 100:
		a = round(random.uniform(1.5, 5.5), 3)
		if b + c <= a:
			p = p + 1
			psm100 = np.append(psm100, p)
			statmodel2 = np.append(statmodel2, a)
			statmodel100 = statmodel2[p:100 + p]
			msm = np.mean(statmodel100)
			msm100 = np.append(msm100, msm)
			ssm = np.std(statmodel100)
			ssm100 = np.append(ssm100, ssm)
		elif b - c >= a:
			p = p + 1 
			psm100 = np.append(psm100, p)
			statmodel2 = np.append(statmodel2, a)
			statmodel100 = statmodel2[p:100 + p]
			msm = np.mean(statmodel100)
			msm100 = np.append(msm100, msm)
			ssm = np.std(statmodel100)
			ssm100 = np.append(ssm100, ssm)
		else:
			#time.sleep(.5)
			stopd2 = np.append(stopd2, a)
			d = d + 1
			d100 = np.append(d100, d)
			stopd100 = stopd2[d:100 + d]
			m = np.mean(stopd100)
			m100 = np.append(m100, m)
			#time.sleep(.5)
			s = np.std(stopd100)
			s100 = np.append(s100, s)
			b = np.mean(statmodel2)
			c = np.std(statmodel2)

plt.plot(d100, m100)			
plt.show()
plt.close()
plt.plot(d100, s100)
plt.show()
plt.close()
plt.plot(psm100, msm100)
plt.show()
plt.plot(psm100, ssm100)
plt.show()

	
def statmodel(a, n, statmodel2):
	while n < 100:
		a = round(random.uniform(1,6), 3)
		n = n + 1 
		statmodel2 = np.append(statmodel2, a)
	return statmodel2
statmodel2 = np.array([])
statmodel2 = statmodel(round(random.uniform(1,6), 3), 0, statmodel2)



