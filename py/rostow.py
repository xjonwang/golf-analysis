import pandas as pd
import numpy as np
c = input("Input the name of the country: ")
america = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Rostow Latin America - Sheet1.csv')
country = pd.DataFrame(america.loc[america.Country == c])
j = 0
print(country)
country_array = np.array([])
x_array = np.array([])
win_array = np.array([])
tie_array = np.array([])
lose_array = np.array([])
while j <= 27:
	x = pd.DataFrame(america.iloc[j,:])
	j = j + 1
	gdp = country.GDP - float(x.iloc[1,:])
	print(gdp)
	if float(gdp) > 0:
		country_array = np.append(country_array, 'c')
	elif float(gdp) < 0:
		x_array = np.append(x_array, 'x')
	pc = country.pc - float(x.iloc[2,:])
	if float(pc) > 0:
		country_array = np.append(country_array, 'c')
	elif float(pc) < 0:
		x_array = np.append(x_array, 'x')
	life = country.life - float(x.iloc[3,:])
	if float(life) > 0:
		country_array = np.append(country_array, 'c')
	elif float(life) < 0:
		x_array = np.append(x_array, 'x')
	literacy = country.literacy - float(x.iloc[4,:])
	if float(literacy) > 0:
		country_array = np.append(country_array, 'c')
	elif float(literacy) < 0:
		x_array = np.append(x_array, 'x')
	IMR = country.IMR - float(x.iloc[5,:])
	if float(IMR) < 0:
		country_array = np.append(country_array, 'c')
	elif float(IMR) > 0:
		x_array = np.append(x_array, 'x')
	NIR = country.NIR - float(x.iloc[6,:])
	if float(NIR) < 0:
		country_array = np.append(country_array, 'c')
	elif float(NIR) > 0:
		x_array = np.append(x_array, 'x')
	TFR = country.TFR - float(x.iloc[7,:])
	if float(TFR) < 0:
		country_array = np.append(country_array, 'c')
	elif float(TFR) > 0:
		x_array = np.append(x_array, 'x')
	if len(country_array) - len(x_array) > 0:
		print("Win")
		win_array = np.append(win_array, 'w')
	elif len(country_array) - len(x_array) < 0:
		print("Lose")
		lose_array = np.append(lose_array, 'l')
	else:
		print("Tie")
		tie_array = np.append(tie_array, 't')
	country_array = np.array([])
	x_array = np.array([])
print(len(win_array), 'win')
print(len(tie_array), 'tie')
print(len(lose_array), 'lose')
	
		