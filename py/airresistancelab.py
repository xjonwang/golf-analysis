import pandas as pd
import numpy as np
data = pd.read_csv(r'C:\Users\Jon Wang\Downloads\SirData.csv')
for x in np.arange(1.0, 5.0, .1):
	velocity = np.array(data.Velocity)
	velocity = velocity**x
	velocity = velocity[np.logical_not(np.isnan(velocity))]
	print(velocity)
	mass = np.array(data.Mass)
	print(mass)
	cor = np.corrcoef(mass, velocity)
	print(x, cor)
