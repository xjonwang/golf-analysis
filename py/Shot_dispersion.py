import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sys
#import xlrd
golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\ScoreSheet_revised.csv')
#print(golf.Par)
#print(golf)
golf_5 = pd.DataFrame(golf.loc[golf.Par == 5])
#print(golf_5)
golf_4 = pd.DataFrame(golf.loc[golf.Par == 4])
#print(golf_4)
golf_3 = pd.DataFrame(golf.loc[golf.Par == 3])
print((len(golf_3) + len(golf_4) + len(golf_5))/len(golf))

hole_list = [golf_5, golf_4, golf_3]

club_list = ["59 Wedge", "54 Wedge", "50 Wedge", "P Wedge", "9 Iron", "8 Iron", "7 Iron", "6 Iron", "5 Iron", "4 Iron", "3 Hybrid", "3 Wood"]

Par3ClubArray = ([])
Par4ClubArray = ([])
Par5ClubArray = ([])
for club in club_list:
	Par3Club = pd.DataFrame(golf_3.loc[golf_3.Club_1 == club])
	Par3ClubUsage = len(Par3Club)
	Par3ClubArray = np.append(Par3ClubArray, Par3ClubUsage)

print(Par3ClubArray)

for club in club_list:
	Par4Club = pd.DataFrame(golf_4.loc[golf_4.Club_2 == club])
	Par4ClubUsage = len(Par4Club)
	Par4ClubArray = np.append(Par4ClubArray, Par4ClubUsage)

print(Par4ClubArray)

for club in club_list:
	Par5Club = pd.DataFrame(golf_5.loc[golf_5.Club_3 == club])
	Par5ClubUsage = len(Par5Club)
	Par5ClubArray = np.append(Par5ClubArray, Par5ClubUsage)

print(Par5ClubArray)

ClubArray = Par3ClubArray + Par4ClubArray + Par5ClubArray
print(ClubArray)

ClubsArray = ([])
for x in range (0,12):
	my_list = [x]
	Clubs = int(ClubArray[x])*my_list
	ClubsArray = np.append(ClubsArray, Clubs)

print(ClubsArray)
print(np.percentile(ClubsArray, 75))