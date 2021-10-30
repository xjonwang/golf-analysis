import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pylab
import scipy.stats as stats
import random
import sys
#import xlrd
golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\ScoreSheet - Sheet1.csv')
np_golf = np.array(golf)
#print(golf.Par)
#print(golf)
golf_sznS18 = pd.DataFrame(golf.loc[golf.Season == 'Summer 2018'])
golf_sznF18 = pd.DataFrame(golf.loc[golf.Season == 'Fall 2018'])
golf_5 = pd.DataFrame(golf.loc[golf.Par == 5])
#print(golf_5)
golf_4 = pd.DataFrame(golf.loc[golf.Par == 4])
#print(golf_4)
golf_3 = pd.DataFrame(golf.loc[golf.Par == 3])
print((len(golf_3) + len(golf_4) + len(golf_5))/len(golf))

golf_4missfairway = pd.DataFrame(golf_4.loc[golf_4.Result != 'Fairway'])
golf_5missfairway = pd.DataFrame(golf_5.loc[golf_5.Result_2 != 'Fairway'])
#print(golf_3)
#print(golf.Yard)
#Standard Deviation of golf
std_3 = np.std(golf_3.Score)
print("The Standard Deviation for par 3s is ", std_3)
std_4 = np.std(golf_4.Score)
print("The Standard Deviation for par 4s is ", std_4)
std_5 = np.std(golf_5.Score)
print("The Standard Deviation for par 5s is ", std_5)
#Mean of golf
mean_3 = np.mean(golf_3.Score)
print("The average for par 3s is ", mean_3)
mean_4 = np.mean(golf_4.Score)
print("The average for par 4s is ", mean_4)
mean_5 = np.mean(golf_5.Score)
print("The average for par 5s is ", mean_5)
print("Average score is ", mean_3 * 4 + mean_4 * 10 + mean_5 * 4)
#GIR
golf_3gr = pd.DataFrame(golf_3.loc[golf_3.Result == 'Green'])
print("Par 3 GIR is ", len(golf_3gr)/len(golf_3) * 100)
golf_4gr = pd.DataFrame(golf_4.loc[golf_4.Result_2 == 'Green'])
print("Par 4 GIR is ", len(golf_4gr)/len(golf_4) * 100)
golf_5gr = pd.DataFrame(golf_5.loc[golf_5.Result_3 == 'Green'])
print("Par 5 GIR is ", len(golf_5gr)/len(golf_5) * 100)
print("The overall GIR is ", (len(golf_3gr) + len(golf_4gr) + len(golf_5gr))/(len(golf)) * 100)

golf_45 = golf_4.append(golf_5)
#print(golf_45)
golf_fairway = pd.DataFrame(golf_45.loc[golf_45.Result == 'Fairway'])
print("Fairway Percentage is ", len(golf_fairway)/len(golf_45) * 100)

golf_missfairway = pd.DataFrame(golf_45.loc[golf_45.Result != 'Fairway'])
golf_missright = pd.DataFrame(golf_missfairway.loc[golf_missfairway.Miss_1 == 'Right'])
golf_missleft = pd.DataFrame(golf_missfairway.loc[golf_missfairway.Miss_1 == 'Left'])
print("Left rough tendency", len(golf_missleft)/len(golf_45) * 100)
print("Right rough tendency", len(golf_missright)/len(golf_45) * 100)

def fairway_pie(fairway, left, right):
	labels_fairway = 'Fairway', 'Miss Right', 'Miss Left'
	sizes_fairway = [len(fairway), len(right), len(left)]
	colors_fairway = ['gold', 'yellowgreen', 'lightskyblue']
	explode_fairway = (0.1, 0, 0)
	#Plot
	plt.pie(sizes_fairway, explode = explode_fairway, labels = labels_fairway, colors = colors_fairway, autopct = '%.2f', shadow = True)
	plt.title("Fairways hit")
	plt.show()

fairway_pie(golf_fairway, golf_missleft, golf_missright)

golf_dr = pd.DataFrame(golf.loc[golf.Club_1 == 'Driver'])
#print(golf_dr)
golf_yd = np.array(golf_dr.Yard)
#print(golf_yd)
golf_1st = np.array(golf_dr.To_Hole1)
#print(golf_1st.astype(int))
golf_dist = np.subtract(golf_yd, golf_1st.astype(int))
print("The average driving distance is ", np.mean(golf_dist))

golf_3_1 = pd.DataFrame(golf_3gr.loc[golf_3gr.Result_2 == 'Made'])
#print(golf_3_1)
golf_3_2 = pd.DataFrame(golf_3gr.loc[golf_3gr.Result_3 == 'Made'])
#print(golf_3_2)
golf_3_3 = pd.DataFrame(golf_3gr.loc[golf_3gr.Result_4 == 'Made'])
#print(golf_3_3)
print("The putts per GIR on par 3s is ", (len(golf_3_1) + len(golf_3_2) * 2 + len(golf_3_3) * 3) / len(golf_3gr))

golf_4_1 = pd.DataFrame(golf_4gr.loc[golf_4gr.Result_3 == 'Made'])
#print(golf_3_1)
golf_4_2 = pd.DataFrame(golf_4gr.loc[golf_4gr.Result_4 == 'Made'])
#print(golf_3_2)
golf_4_3 = pd.DataFrame(golf_4gr.loc[golf_4gr.Result_5 == 'Made'])
#print(golf_3_3)
print("The putts per GIR on par 4s is ", (len(golf_4_1) + len(golf_4_2) * 2 + len(golf_4_3) * 3) / len(golf_4gr))

golf_5_1 = pd.DataFrame(golf_5gr.loc[golf_5gr.Result_4 == 'Made'])
#print(golf_3_1)
golf_5_2 = pd.DataFrame(golf_5gr.loc[golf_5gr.Result_5 == 'Made'])
#print(golf_3_2)
golf_5_3 = pd.DataFrame(golf_5gr.loc[golf_5gr.Result_6 == 'Made'])
#print(golf_3_3)
print("The putts per GIR on par 5s is ", (len(golf_5_1) + len(golf_5_2) * 2 + len(golf_5_3) * 3) / len(golf_5gr))

#Scrambling
golf_3mgr = pd.DataFrame(golf_3.loc[golf_3.Result != 'Green'])
golf_3scrm = pd.DataFrame(golf_3mgr.loc[golf_3mgr.Result_3 == 'Made'])
print("The scrambling percentage for par 3s is ", len(golf_3scrm)/len(golf_3mgr) * 100)
golf_4mgr = pd.DataFrame(golf_4.loc[golf_4.Result_2 != 'Green'])
golf_4scrm = pd.DataFrame(golf_4mgr.loc[golf_4mgr.Result_4 == 'Made'])
print("The scrambling percentage for par 4s is ", len(golf_4scrm)/len(golf_4mgr) * 100)
golf_5mgr = pd.DataFrame(golf_5.loc[golf_5.Result_3 != 'Green'])
golf_5scrm = pd.DataFrame(golf_5mgr.loc[golf_5mgr.Result_5 == 'Made'])
print("The scrambling percentage for par 5s is ", len(golf_5scrm)/len(golf_5mgr) * 100)
print("The overall scrambling rate is ", (len(golf_3scrm) + len(golf_4scrm) + len(golf_5scrm))/(len(golf_3mgr) + len(golf_4mgr) + len(golf_5mgr)) * 100)

golf_3missleft = pd.DataFrame(golf_3mgr.loc[golf_3mgr.Miss_1 == 'Left'])
golf_3missright = pd.DataFrame(golf_3mgr.loc[golf_3mgr.Miss_1 == 'Right'])
golf_4missleft = pd.DataFrame(golf_4mgr.loc[golf_4mgr.Miss_2 == 'Left'])
golf_4missright = pd.DataFrame(golf_4mgr.loc[golf_4mgr.Miss_2 == 'Right'])
golf_5missleft = pd.DataFrame(golf_5mgr.loc[golf_5mgr.Miss_3 == 'Left'])
golf_5missright = pd.DataFrame(golf_5mgr.loc[golf_5mgr.Miss_3 == 'Right'])
print("Left approach percentage is ", (len(golf_3missleft) + len(golf_4missleft) + len(golf_5missleft))/len(golf) * 100)
print("Right approach percentage is ", (len(golf_3missright) + len(golf_4missright) + len(golf_5missright))/len(golf) * 100)

#Scrambling by Distance
golf_3mL15 = pd.DataFrame(golf_3mgr.loc[golf_3mgr.To_Hole1 <= 10])
golf_3mL15s = pd.DataFrame(golf_3mL15.loc[golf_3mL15.Result_3 == 'Made'])

golf_4mL15 = pd.DataFrame(golf_4mgr.loc[golf_4mgr.To_Hole2 <= 10])
golf_4mL15s = pd.DataFrame(golf_4mL15.loc[golf_4mL15.Result_4 == 'Made'])

golf_5mL15 = pd.DataFrame(golf_5mgr.loc[golf_5mgr.To_Hole1 <= 10])
golf_5mL15s = pd.DataFrame(golf_5mL15.loc[golf_5mL15.Result_5 == 'Made'])
print("The scrambling rate from less than 10 yards is ", (len(golf_3mL15s) + len(golf_4mL15s) + len(golf_5mL15s))/(len(golf_3mL15) + len(golf_4mL15) + len(golf_5mL15)) * 100)

golf_3mG15 = pd.DataFrame(golf_3mgr.loc[golf_3mgr.To_Hole1 >= 10])
golf_3m1525 = pd.DataFrame(golf_3mG15.loc[golf_3mG15.To_Hole1 <= 20])
golf_3m1525s = pd.DataFrame(golf_3m1525.loc[golf_3m1525.Result_3 == 'Made'])

golf_4mG15 = pd.DataFrame(golf_4mgr.loc[golf_4mgr.To_Hole2 >= 10])
golf_4m1525 = pd.DataFrame(golf_4mG15.loc[golf_4mG15.To_Hole2 <= 20])
golf_4m1525s = pd.DataFrame(golf_4m1525.loc[golf_4m1525.Result_4 == 'Made'])

golf_5mG15 = pd.DataFrame(golf_5mgr.loc[golf_5mgr.To_Hole3 >= 10])
golf_5m1525 = pd.DataFrame(golf_5mG15.loc[golf_5mG15.To_Hole3 <= 20])
golf_5m1525s = pd.DataFrame(golf_5m1525.loc[golf_5m1525.Result_5 == 'Made'])
print("The scrambling rate from 10-20 yards is ", (len(golf_3m1525s) + len(golf_4m1525s) + len(golf_5m1525s))/(len(golf_3m1525) + len(golf_4m1525) + len(golf_5m1525)) * 100)

golf_3mG25 = pd.DataFrame(golf_3mgr.loc[golf_3mgr.To_Hole1 >= 20])
golf_3m2535 = pd.DataFrame(golf_3mG25.loc[golf_3mG25.To_Hole1 <= 30])
golf_3m2535s = pd.DataFrame(golf_3m2535.loc[golf_3m2535.Result_3 == 'Made'])

golf_4mG25 = pd.DataFrame(golf_4mgr.loc[golf_4mgr.To_Hole2 >= 20])
golf_4m2535 = pd.DataFrame(golf_4mG25.loc[golf_4mG25.To_Hole2 <= 30])
golf_4m2535s = pd.DataFrame(golf_4m2535.loc[golf_4m2535.Result_4 == 'Made'])

golf_5mG25 = pd.DataFrame(golf_5mgr.loc[golf_5mgr.To_Hole3 >= 20])
golf_5m2535 = pd.DataFrame(golf_5mG25.loc[golf_5mG25.To_Hole3 <= 30])
golf_5m2535s = pd.DataFrame(golf_5m2535.loc[golf_5m2535.Result_5 == 'Made'])
print("The scrambling rate from 20-30 yards is ", (len(golf_3m2535s) + len(golf_4m2535s) + len(golf_5m2535s))/(len(golf_3m2535) + len(golf_4m2535) + len(golf_5m2535)) * 100)

golf_3mG35 = pd.DataFrame(golf_3mgr.loc[golf_3mgr.To_Hole1 >= 30])
golf_3m3545 = pd.DataFrame(golf_3mG35.loc[golf_3mG35.To_Hole1 <= 40])
golf_3m3545s = pd.DataFrame(golf_3m3545.loc[golf_3m3545.Result_3 == 'Made'])

golf_4mG35 = pd.DataFrame(golf_4mgr.loc[golf_4mgr.To_Hole2 >= 30])
golf_4m3545 = pd.DataFrame(golf_4mG35.loc[golf_4mG35.To_Hole2 <= 40])
golf_4m3545s = pd.DataFrame(golf_4m3545.loc[golf_4m3545.Result_4 == 'Made'])

golf_5mG35 = pd.DataFrame(golf_5mgr.loc[golf_5mgr.To_Hole3 >= 30])
golf_5m3545 = pd.DataFrame(golf_5mG35.loc[golf_5mG35.To_Hole3 <= 40])
golf_5m3545s = pd.DataFrame(golf_5m3545.loc[golf_5m3545.Result_5 == 'Made'])
print("The scrambling rate from 30-40 yards is ", (len(golf_3m3545s) + len(golf_4m3545s) + len(golf_5m3545s))/(len(golf_3m3545) + len(golf_4m3545) + len(golf_5m3545)) * 100)

golf_3mG45 = pd.DataFrame(golf_3mgr.loc[golf_3mgr.To_Hole1 >= 40])
golf_3mG45s = pd.DataFrame(golf_3mG45.loc[golf_3mG45.Result_3 == 'Made'])

golf_4mG45 = pd.DataFrame(golf_4mgr.loc[golf_4mgr.To_Hole2 >= 40])
golf_4mG45s = pd.DataFrame(golf_4mG45.loc[golf_4mG45.Result_4 == 'Made'])

golf_5mG45 = pd.DataFrame(golf_5mgr.loc[golf_5mgr.To_Hole1 >= 40])
golf_5mG45s = pd.DataFrame(golf_5mG45.loc[golf_5mG45.Result_5 == 'Made'])
print("The scrambling rate from more than 40 yards is ", (len(golf_3mG45s) + len(golf_4mG45s) + len(golf_5mG45s))/(len(golf_3mG45) + len(golf_4mG45) + len(golf_5mG45)) * 100)



#for x in nums:
	#a = golf_chips[x]
	#b = title[x]
	#pieshortgame(a, b)

#Proximity to hole
npf_3p = pd.DataFrame(golf_3.loc[golf_3.Unit_1 == "FT"])
npy_3p = pd.DataFrame(golf_3.loc[golf_3.Unit_1 == "Yard"])
feet_3p = np.array(npf_3p.To_Hole1)
yard_3p = np.array(npy_3p.To_Hole1)
yard_3pcl = yard_3p * 3
golf_3p = np.append(yard_3pcl, feet_3p)
golf_3pm = np.mean(golf_3p)
#print(golf_3pm)

npf_4p = pd.DataFrame(golf_4.loc[golf_4.Unit_2 == "FT"])
npy_4p = pd.DataFrame(golf_4.loc[golf_4.Unit_2 == "Yard"])
feet_4p = np.array(npf_4p.To_Hole2)
yard_4p = np.array(npy_4p.To_Hole2)
yard_4pcl = yard_4p * 3
golf_4p = np.append(yard_4pcl, feet_4p)
golf_4pm = np.mean(golf_4p)
#print(golf_4pm)

npf_5p = pd.DataFrame(golf_5.loc[golf_5.Unit_3 == "FT"])
npy_5p = pd.DataFrame(golf_5.loc[golf_5.Unit_3 == "Yard"])
feet_5p = np.array(npf_5p.To_Hole3)
yard_5p = np.array(npy_5p.To_Hole3)
yard_5pcl = yard_5p * 3
golf_5p = np.append(yard_5pcl, feet_5p)
golf_5pm = np.mean(golf_5p)
#print(golf_5pm)

print("The overall proximity to hole is ", (golf_3pm * len(golf_3) + golf_4pm * len(golf_4) + golf_5pm * len(golf_5)) / len(golf))

#print(golf_3.describe())

golf_3G100 = pd.DataFrame(golf_3.loc[golf_3.Yard >= 100])
golf_3100125 = pd.DataFrame(golf_3G100.loc[golf_3G100.Yard <= 125])
npf_3100125p = pd.DataFrame(golf_3100125.loc[golf_3100125.Unit_1 == "FT"])
npy_3100125p = pd.DataFrame(golf_3100125.loc[golf_3100125.Unit_1 == "Yard"])
feet_3100125p = np.array(npf_3100125p.To_Hole1)
yard_3100125p = np.array(npy_3100125p.To_Hole1)
yard_3100125pcl = yard_3100125p * 3
golf_3100125p = np.append(yard_3100125pcl, feet_3100125p)
golf_3100125pm = np.mean(golf_3100125p)
#print("The proximity to hole on par 3s from 100-125 yards is ", golf_3L125pm)

golf_3G125 = pd.DataFrame(golf_3.loc[golf_3.Yard >= 125])
golf_3125150 = pd.DataFrame(golf_3G125.loc[golf_3G125.Yard <= 150])
npf_3125150p = pd.DataFrame(golf_3125150.loc[golf_3125150.Unit_1 == "FT"])
npy_3125150p = pd.DataFrame(golf_3125150.loc[golf_3125150.Unit_1 == "Yard"])
feet_3125150p = np.array(npf_3125150p.To_Hole1)
yard_3125150p = np.array(npy_3125150p.To_Hole1)
yard_3125150pcl = yard_3125150p * 3
golf_3125150p = np.append(yard_3125150pcl, feet_3125150p)
golf_3125150pm = np.mean(golf_3125150p)
#print("The proximity to hole on par 3s from 125-150 yards is ", golf_3125150pm)

golf_3G150 = pd.DataFrame(golf_3.loc[golf_3.Yard >= 150])
golf_3150175 = pd.DataFrame(golf_3G150.loc[golf_3G150.Yard <= 175])
npf_3150175p = pd.DataFrame(golf_3150175.loc[golf_3150175.Unit_1 == "FT"])
npy_3150175p = pd.DataFrame(golf_3150175.loc[golf_3150175.Unit_1 == "Yard"])
feet_3150175p = np.array(npf_3150175p.To_Hole1)
yard_3150175p = np.array(npy_3150175p.To_Hole1)
yard_3150175pcl = yard_3150175p * 3
golf_3150175p = np.append(yard_3150175pcl, feet_3150175p)
golf_3150175pm = np.mean(golf_3150175p)
#print("The proximity to hole on par 3s from 150-175 yards is ", golf_3150175pm)

golf_3G175 = pd.DataFrame(golf_3.loc[golf_3.Yard >= 175])
npf_3G175p = pd.DataFrame(golf_3G175.loc[golf_3G175.Unit_1 == "FT"])
npy_3G175p = pd.DataFrame(golf_3G175.loc[golf_3G175.Unit_1 == "Yard"])
feet_3G175p = np.array(npf_3G175p.To_Hole1)
yard_3G175p = np.array(npy_3G175p.To_Hole1)
yard_3G175pcl = yard_3G175p * 3
golf_3G175p = np.append(yard_3G175pcl, feet_3G175p)
golf_3G175pm = np.mean(golf_3G175p)
#print("The proximity to hole on par 3s from more than 175 yards is ", golf_3G175pm)

golf_4L75 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 <= 75])
npf_4L75p = pd.DataFrame(golf_4L75.loc[golf_4L75.Unit_2 == "FT"])
npy_4L75p = pd.DataFrame(golf_4L75.loc[golf_4L75.Unit_2 == "Yard"])
feet_4L75p = np.array(npf_4L75p.To_Hole2)
yard_4L75p = np.array(npy_4L75p.To_Hole2)
yard_4L75pcl = yard_4L75p * 3
golf_4L75p = np.append(yard_4L75pcl, feet_4L75p)
golf_4L75pm = np.mean(golf_4L75p)
#print("The proximity to hole on par 4s from less than 75 yards is ", golf_4L75pm)

golf_4G75 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 >= 75])
golf_475100 = pd.DataFrame(golf_4G75.loc[golf_4G75.To_Hole1 <= 100])
npf_475100p = pd.DataFrame(golf_475100.loc[golf_475100.Unit_2 == "FT"])
npy_475100p = pd.DataFrame(golf_475100.loc[golf_475100.Unit_2 == "Yard"])
feet_475100p = np.array(npf_475100p.To_Hole2)
yard_475100p = np.array(npy_475100p.To_Hole2)
yard_475100pcl = yard_475100p * 3
golf_475100p = np.append(yard_475100pcl, feet_475100p)
golf_475100pm = np.mean(golf_475100p)
#print("The proximity to hole on par 4s from 75-100 yards is ", golf_475100pm)

golf_4G100 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 >= 100])
golf_4100125 = pd.DataFrame(golf_4G100.loc[golf_4G100.To_Hole1 <= 125])
npf_4100125p = pd.DataFrame(golf_4100125.loc[golf_4100125.Unit_2 == "FT"])
npy_4100125p = pd.DataFrame(golf_4100125.loc[golf_4100125.Unit_2 == "Yard"])
feet_4100125p = np.array(npf_4100125p.To_Hole2)
yard_4100125p = np.array(npy_4100125p.To_Hole2)
yard_4100125pcl = yard_4100125p * 3
golf_4100125p = np.append(yard_4100125pcl, feet_4100125p)
golf_4100125pm = np.mean(golf_4100125p)
#print("The proximity to hole on par 4s from 100-125 yards is ", golf_4100125pm)

golf_4G125 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 >= 125])
golf_4125150 = pd.DataFrame(golf_4G125.loc[golf_4G125.To_Hole1 <= 150])
npf_4125150p = pd.DataFrame(golf_4125150.loc[golf_4125150.Unit_2 == "FT"])
npy_4125150p = pd.DataFrame(golf_4125150.loc[golf_4125150.Unit_2 == "Yard"])
feet_4125150p = np.array(npf_4125150p.To_Hole2)
yard_4125150p = np.array(npy_4125150p.To_Hole2)
yard_4125150pcl = yard_4125150p * 3
golf_4125150p = np.append(yard_4125150pcl, feet_4125150p)
golf_4125150pm = np.mean(golf_4125150p)
#print("The proximity to hole on par 4s from 125-150 yards is ", golf_4125150pm)

golf_4G150 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 >= 150])
golf_4150175 = pd.DataFrame(golf_4G150.loc[golf_4G150.To_Hole1 <= 175])
npf_4150175p = pd.DataFrame(golf_4150175.loc[golf_4150175.Unit_2 == "FT"])
npy_4150175p = pd.DataFrame(golf_4150175.loc[golf_4150175.Unit_2 == "Yard"])
feet_4150175p = np.array(npf_4150175p.To_Hole2)
yard_4150175p = np.array(npy_4150175p.To_Hole2)
yard_4150175pcl = yard_4150175p * 3
golf_4150175p = np.append(yard_4150175pcl, feet_4150175p)
golf_4150175pm = np.mean(golf_4150175p)
#print("The proximity to hole on par 4s from 150-175 yards is ", golf_4150175pm)

golf_4G175 = pd.DataFrame(golf_4.loc[golf_4.To_Hole1 >= 175])
npf_4G175p = pd.DataFrame(golf_4G175.loc[golf_4G175.Unit_2 == "FT"])
npy_4G175p = pd.DataFrame(golf_4G175.loc[golf_4G175.Unit_2 == "Yard"])
feet_4G175p = np.array(npf_4G175p.To_Hole2)
yard_4G175p = np.array(npy_4G175p.To_Hole2)
yard_4G175pcl = yard_4G175p * 3
golf_4G175p = np.append(yard_4G175pcl, feet_4G175p)
golf_4G175pm = np.mean(golf_4G175p)
#print("The proximity to hole on par 4s from more than 175 yards is ", golf_4G175pm)


golf_5L75 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 <= 75])
npf_5L75p = pd.DataFrame(golf_5L75.loc[golf_5L75.Unit_3 == "FT"])
npy_5L75p = pd.DataFrame(golf_5L75.loc[golf_5L75.Unit_3 == "Yard"])
feet_5L75p = np.array(npf_5L75p.To_Hole3)
yard_5L75p = np.array(npy_5L75p.To_Hole3)
yard_5L75pcl = yard_5L75p * 3
golf_5L75p = np.append(yard_5L75pcl, feet_5L75p)
golf_5L75pm = np.mean(golf_5L75p)
#print("The proximity to hole on par 5s from less than 75 yards is ", golf_5L75pm)

golf_5G75 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 >= 75])
golf_575100 = pd.DataFrame(golf_5G75.loc[golf_5G75.To_Hole2 <= 100])
npf_575100p = pd.DataFrame(golf_575100.loc[golf_575100.Unit_3 == "FT"])
npy_575100p = pd.DataFrame(golf_575100.loc[golf_575100.Unit_3 == "Yard"])
feet_575100p = np.array(npf_575100p.To_Hole3)
yard_575100p = np.array(npy_575100p.To_Hole3)
yard_575100pcl = yard_575100p * 3
golf_575100p = np.append(yard_575100pcl, feet_575100p)
golf_575100pm = np.mean(golf_575100p)
#print("The proximity to hole on par 5s from 75-100 yards is ", golf_575100pm)

golf_5G100 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 >= 100])
golf_5100125 = pd.DataFrame(golf_5G100.loc[golf_5G100.To_Hole2 <= 125])
npf_5100125p = pd.DataFrame(golf_5100125.loc[golf_5100125.Unit_3 == "FT"])
npy_5100125p = pd.DataFrame(golf_5100125.loc[golf_5100125.Unit_3 == "Yard"])
feet_5100125p = np.array(npf_5100125p.To_Hole3)
yard_5100125p = np.array(npy_5100125p.To_Hole3)
yard_5100125pcl = yard_5100125p * 3
golf_5100125p = np.append(yard_5100125pcl, feet_5100125p)
golf_5100125pm = np.mean(golf_5100125p)
#print("The proximity to hole on par 5s from 100-125 yards is ", golf_5100125pm)

golf_5G125 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 >= 125])
golf_5125150 = pd.DataFrame(golf_5G125.loc[golf_5G125.To_Hole2 <= 150])
npf_5125150p = pd.DataFrame(golf_5125150.loc[golf_5125150.Unit_3 == "FT"])
npy_5125150p = pd.DataFrame(golf_5125150.loc[golf_5125150.Unit_3 == "Yard"])
feet_5125150p = np.array(npf_5125150p.To_Hole3)
yard_5125150p = np.array(npy_5125150p.To_Hole3)
yard_5125150pcl = yard_5125150p * 3
golf_5125150p = np.append(yard_5125150pcl, feet_5125150p)
golf_5125150pm = np.mean(golf_5125150p)
#print("The proximity to hole on par 5s from 125-150 yards is ", golf_5125150pm)

golf_5G150 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 >= 150])
golf_5150175 = pd.DataFrame(golf_5G150.loc[golf_5G150.To_Hole2 <= 175])
npf_5150175p = pd.DataFrame(golf_5150175.loc[golf_5150175.Unit_3 == "FT"])
npy_5150175p = pd.DataFrame(golf_5150175.loc[golf_5150175.Unit_3 == "Yard"])
feet_5150175p = np.array(npf_5150175p.To_Hole3)
yard_5150175p = np.array(npy_5150175p.To_Hole3)
yard_5150175pcl = yard_5150175p * 3
golf_5150175p = np.append(yard_5150175pcl, feet_5150175p)
golf_5150175pm = np.mean(golf_5150175p)
#print("The proximity to hole on par 5s from 150-175 yards is ", golf_5150175pm)

golf_5G175 = pd.DataFrame(golf_5.loc[golf_5.To_Hole2 >= 175])
npf_5G175p = pd.DataFrame(golf_5G175.loc[golf_5G175.Unit_3 == "FT"])
npy_5G175p = pd.DataFrame(golf_5G175.loc[golf_5G175.Unit_3 == "Yard"])
feet_5G175p = np.array(npf_5G175p.To_Hole3)
yard_5G175p = np.array(npy_5G175p.To_Hole3)
yard_5G175pcl = yard_5G175p * 3
golf_5G175p = np.append(yard_5G175pcl, feet_5G175p)
golf_5G175pm = np.mean(golf_5G175p)
#print("The proximity to hole on par 5s from more than 175 yards is ", golf_5G175pm)

golf_L75 = np.append(golf_5L75p, golf_4L75p)
print("The proximity to hole on shots less than 75 yards is ", np.mean(golf_L75))
golf_75100 = np.append(golf_575100p, golf_475100p)
print("The proximity to hole on shots 75-100 yards is ", np.mean(golf_75100))
#golf_100125 = np.append(golf_5100125p, golf_4100125p, golf_3100125p)
golf_100125f = np.append(golf_5100125p, golf_4100125p)
golf_100125 = np.append(golf_100125f, golf_3100125p)
print("The proximity to hole on shots 100-125 yards is ", np.mean(golf_100125))
golf_125150f = np.append(golf_5125150p, golf_4125150p)
golf_125150 = np.append(golf_125150f, golf_3125150p)
print("The proximity to hole on shots 125-150 yards is ", np.mean(golf_125150))
golf_150175f = np.append(golf_5150175p, golf_4150175p)
golf_150175 = np.append(golf_150175f, golf_3150175p)
print("The proximity to hole on shots 150-175 yards is ", np.mean(golf_150175))
golf_G175f = np.append(golf_5G175p, golf_4G175p)
golf_G175 = np.append(golf_G175f, golf_3G175p)
print("The proximity to hole on shots more than 175 yards is ", np.mean(golf_G175))

golf_4L75mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 <= 75])
npf_4L75pmf = pd.DataFrame(golf_4L75mf.loc[golf_4L75mf.Unit_2 == "FT"])
npy_4L75pmf = pd.DataFrame(golf_4L75mf.loc[golf_4L75mf.Unit_2 == "Yard"])
feet_4L75pmf = np.array(npf_4L75pmf.To_Hole2)
yard_4L75pmf = np.array(npy_4L75pmf.To_Hole2)
yard_4L75pclmf = yard_4L75pmf * 3
golf_4L75pmf = np.append(yard_4L75pclmf, feet_4L75pmf)
#print("The proximity to hole on par 4s from less than 75 yards is ", golf_4L75pm)

golf_4G75mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 >= 75])
golf_475100mf = pd.DataFrame(golf_4G75mf.loc[golf_4G75mf.To_Hole1 <= 100])
npf_475100pmf = pd.DataFrame(golf_475100mf.loc[golf_475100mf.Unit_2 == "FT"])
npy_475100pmf = pd.DataFrame(golf_475100mf.loc[golf_475100mf.Unit_2 == "Yard"])
feet_475100pmf = np.array(npf_475100pmf.To_Hole2)
yard_475100pmf = np.array(npy_475100pmf.To_Hole2)
yard_475100pclmf = yard_475100pmf * 3
golf_475100pmf = np.append(yard_475100pclmf, feet_475100pmf)
#print("The proximity to hole on par 4s from 75-100 yards is ", golf_475100pm)

golf_4G100mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 >= 100])
golf_4100125mf = pd.DataFrame(golf_4G100mf.loc[golf_4G100mf.To_Hole1 <= 125])
npf_4100125pmf = pd.DataFrame(golf_4100125mf.loc[golf_4100125mf.Unit_2 == "FT"])
npy_4100125pmf = pd.DataFrame(golf_4100125mf.loc[golf_4100125mf.Unit_2 == "Yard"])
feet_4100125pmf = np.array(npf_4100125pmf.To_Hole2)
yard_4100125pmf = np.array(npy_4100125pmf.To_Hole2)
yard_4100125pclmf = yard_4100125pmf * 3
golf_4100125pmf = np.append(yard_4100125pclmf, feet_4100125pmf)
#print("The proximity to hole on par 4s from 100-125 yards is ", golf_4100125pm)

golf_4G125mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 >= 125])
golf_4125150mf = pd.DataFrame(golf_4G125mf.loc[golf_4G125mf.To_Hole1 <= 150])
npf_4125150pmf = pd.DataFrame(golf_4125150mf.loc[golf_4125150mf.Unit_2 == "FT"])
npy_4125150pmf = pd.DataFrame(golf_4125150mf.loc[golf_4125150mf.Unit_2 == "Yard"])
feet_4125150pmf = np.array(npf_4125150pmf.To_Hole2)
yard_4125150pmf = np.array(npy_4125150pmf.To_Hole2)
yard_4125150pclmf = yard_4125150pmf * 3
golf_4125150pmf = np.append(yard_4125150pclmf, feet_4125150pmf)
#print("The proximity to hole on par 4s from 125-150 yards is ", golf_4125150pm)

golf_4G150mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 >= 150])
golf_4150175mf = pd.DataFrame(golf_4G150mf.loc[golf_4G150mf.To_Hole1 <= 175])
npf_4150175pmf = pd.DataFrame(golf_4150175mf.loc[golf_4150175mf.Unit_2 == "FT"])
npy_4150175pmf = pd.DataFrame(golf_4150175mf.loc[golf_4150175mf.Unit_2 == "Yard"])
feet_4150175pmf = np.array(npf_4150175pmf.To_Hole2)
yard_4150175pmf = np.array(npy_4150175pmf.To_Hole2)
yard_4150175pclmf = yard_4150175pmf * 3
golf_4150175pmf = np.append(yard_4150175pclmf, feet_4150175pmf)
#print("The proximity to hole on par 4s from 150-175 yards is ", golf_4150175pm)

golf_4G175mf = pd.DataFrame(golf_4missfairway.loc[golf_4missfairway.To_Hole1 >= 175])
npf_4G175pmf = pd.DataFrame(golf_4G175mf.loc[golf_4G175mf.Unit_2 == "FT"])
npy_4G175pmf = pd.DataFrame(golf_4G175mf.loc[golf_4G175mf.Unit_2 == "Yard"])
feet_4G175pmf = np.array(npf_4G175pmf.To_Hole2)
yard_4G175pmf = np.array(npy_4G175pmf.To_Hole2)
yard_4G175pclmf = yard_4G175pmf * 3
golf_4G175pmf = np.append(yard_4G175pclmf, feet_4G175pmf)
#print("The proximity to hole on par 4s from more than 175 yards is ", golf_4G175pm)


golf_5L75mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 <= 75])
npf_5L75pmf = pd.DataFrame(golf_5L75mf.loc[golf_5L75mf.Unit_3 == "FT"])
npy_5L75pmf = pd.DataFrame(golf_5L75mf.loc[golf_5L75mf.Unit_3 == "Yard"])
feet_5L75pmf = np.array(npf_5L75pmf.To_Hole3)
yard_5L75pmf = np.array(npy_5L75pmf.To_Hole3)
yard_5L75pclmf = yard_5L75pmf * 3
golf_5L75pmf = np.append(yard_5L75pclmf, feet_5L75pmf)
#print("The proximity to hole on par 5s from less than 75 yards is ", golf_5L75pm)

golf_5G75mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 >= 75])
golf_575100mf = pd.DataFrame(golf_5G75mf.loc[golf_5G75mf.To_Hole2 <= 100])
npf_575100pmf = pd.DataFrame(golf_575100mf.loc[golf_575100mf.Unit_3 == "FT"])
npy_575100pmf = pd.DataFrame(golf_575100mf.loc[golf_575100mf.Unit_3 == "Yard"])
feet_575100pmf = np.array(npf_575100pmf.To_Hole3)
yard_575100pmf = np.array(npy_575100pmf.To_Hole3)
yard_575100pclmf = yard_575100pmf * 3
golf_575100pmf = np.append(yard_575100pclmf, feet_575100pmf)
#print("The proximity to hole on par 5s from 75-100 yards is ", golf_575100pm)

golf_5G100mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 >= 100])
golf_5100125mf = pd.DataFrame(golf_5G100mf.loc[golf_5G100mf.To_Hole2 <= 125])
npf_5100125pmf = pd.DataFrame(golf_5100125mf.loc[golf_5100125mf.Unit_3 == "FT"])
npy_5100125pmf = pd.DataFrame(golf_5100125mf.loc[golf_5100125mf.Unit_3 == "Yard"])
feet_5100125pmf = np.array(npf_5100125pmf.To_Hole3)
yard_5100125pmf = np.array(npy_5100125pmf.To_Hole3)
yard_5100125pclmf = yard_5100125pmf * 3
golf_5100125pmf = np.append(yard_5100125pclmf, feet_5100125pmf)
#print("The proximity to hole on par 5s from 100-125 yards is ", golf_5100125pm)

golf_5G125mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 >= 125])
golf_5125150mf = pd.DataFrame(golf_5G125mf.loc[golf_5G125mf.To_Hole2 <= 150])
npf_5125150pmf = pd.DataFrame(golf_5125150mf.loc[golf_5125150mf.Unit_3 == "FT"])
npy_5125150pmf = pd.DataFrame(golf_5125150mf.loc[golf_5125150mf.Unit_3 == "Yard"])
feet_5125150pmf = np.array(npf_5125150pmf.To_Hole3)
yard_5125150pmf = np.array(npy_5125150pmf.To_Hole3)
yard_5125150pclmf = yard_5125150pmf * 3
golf_5125150pmf = np.append(yard_5125150pclmf, feet_5125150pmf)
#print("The proximity to hole on par 5s from 125-150 yards is ", golf_5125150pm)

golf_5G150mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 >= 150])
golf_5150175mf = pd.DataFrame(golf_5G150mf.loc[golf_5G150mf.To_Hole2 <= 175])
npf_5150175pmf = pd.DataFrame(golf_5150175mf.loc[golf_5150175mf.Unit_3 == "FT"])
npy_5150175pmf = pd.DataFrame(golf_5150175mf.loc[golf_5150175mf.Unit_3 == "Yard"])
feet_5150175pmf = np.array(npf_5150175pmf.To_Hole3)
yard_5150175pmf = np.array(npy_5150175pmf.To_Hole3)
yard_5150175pclmf = yard_5150175pmf * 3
golf_5150175pmf = np.append(yard_5150175pclmf, feet_5150175pmf)
#print("The proximity to hole on par 5s from 150-175 yards is ", golf_5150175pm)

golf_5G175mf = pd.DataFrame(golf_5missfairway.loc[golf_5missfairway.To_Hole2 >= 175])
npf_5G175pmf = pd.DataFrame(golf_5G175mf.loc[golf_5G175mf.Unit_3 == "FT"])
npy_5G175pmf = pd.DataFrame(golf_5G175mf.loc[golf_5G175mf.Unit_3 == "Yard"])
feet_5G175pmf = np.array(npf_5G175pmf.To_Hole3)
yard_5G175pmf = np.array(npy_5G175pmf.To_Hole3)
yard_5G175pclmf = yard_5G175pmf * 3
golf_5G175pmf = np.append(yard_5G175pclmf, feet_5G175pmf)
#print("The proximity to hole on par 5s from more than 175 yards is ", golf_5G175pm)

golf_L75mf = np.append(golf_5L75pmf, golf_4L75pmf)
print("The proximity to hole on shots less than 75 yards from the rough is ", np.mean(golf_L75mf))
golf_75100mf = np.append(golf_575100pmf, golf_475100pmf)
print("The proximity to hole on shots 75-100 yards from the rough is ", np.mean(golf_75100mf))
#golf_100125 = np.append(golf_5100125p, golf_4100125p, golf_3100125p)
golf_100125mf = np.append(golf_5100125pmf, golf_4100125pmf)
print("The proximity to hole on shots 100-125 yards from the roughis ", np.mean(golf_100125mf))
golf_125150mf = np.append(golf_5125150pmf, golf_4125150pmf)
print("The proximity to hole on shots 125-150 yards from the rough is ", np.mean(golf_125150mf))
golf_150175mf = np.append(golf_5150175pmf, golf_4150175pmf)
print("The proximity to hole on shots 150-175 yards from the rough is ", np.mean(golf_150175mf))
golf_G175mf = np.append(golf_5G175pmf, golf_4G175pmf)
print("The proximity to hole on shots more than 175 yards from the rough is ", np.mean(golf_G175mf))

#Sand Save pct
golf_3sand = pd.DataFrame(golf_3.loc[golf_3.Result == 'Bunker'])
golf_3ssave = pd.DataFrame(golf_3sand.loc[golf_3sand.Result_3 == 'Made'])
golf_4sand = pd.DataFrame(golf_4.loc[golf_4.Result_2 == 'Bunker'])
golf_4ssave = pd.DataFrame(golf_4sand.loc[golf_4sand.Result_4 == 'Made'])
golf_5sand = pd.DataFrame(golf_5.loc[golf_5.Result == 'Bunker'])
golf_5ssave = pd.DataFrame(golf_5sand.loc[golf_5sand.Result_5 == 'Made'])
print("Sand save percentage is ", (len(golf_3ssave) + len(golf_4ssave) + len(golf_5ssave))/(len(golf_3sand) + len(golf_4sand) + len(golf_5sand)) * 100)
#Holes per Birdie
golf_3b = pd.DataFrame(golf_3.loc[golf_3.Score == 2])
golf_4b = pd.DataFrame(golf_4.loc[golf_4.Score == 3])
golf_5b = pd.DataFrame(golf_5.loc[golf_5.Score == 4])
print("Holes per birdie is ", (len(golf))/(len(golf_3b) + len(golf_4b) + len(golf_5b)))

golf_u1f = pd.DataFrame(golf.loc[golf.Unit_1 == 'FT'])
golf_u2f = pd.DataFrame(golf.loc[golf.Unit_2 == 'FT'])
golf_u3f = pd.DataFrame(golf.loc[golf.Unit_3 == 'FT'])
golf_u4f = pd.DataFrame(golf.loc[golf.Unit_4 == 'FT'])
golf_u5f = pd.DataFrame(golf.loc[golf.Unit_5 == 'FT'])
golf_u6f = pd.DataFrame(golf.loc[golf.Unit_6 == 'FT'])
golf_u7f = pd.DataFrame(golf.loc[golf.Unit_7 == 'FT'])
golf_u12f = golf_u1f.append(golf_u2f)
golf_u123f = golf_u12f.append(golf_u3f)
golf_u1234f = golf_u123f.append(golf_u4f)
golf_u12345f = golf_u1234f.append(golf_u5f)
golf_u123456f = golf_u12345f.append(golf_u6f)
golf_ftd = golf_u123456f.append(golf_u7f)
golf_ft = golf_ftd.drop_duplicates()
golf_ft03 = np.array([])
golf_ft45 = np.array([])
golf_ft68 = np.array([])
golf_ft912 = np.array([])
golf_ft1317 = np.array([])
golf_ft1825 = np.array([])
golf_ft2635 = np.array([])
golf_ft3645 = np.array([])
golf_ft4655 = np.array([])
golf_ft5665 = np.array([])
putt_num = [0, 1, 2, 3, 4, 5, 6, 7]
golf_puttbins = (3, 5, 8, 12, 17, 25, 35, 45)
golf_puttbins2 = (0, 3, 5, 8, 12, 17, 25, 35)
def putting_distances(f, a, b):
	golf_putt1 = pd.DataFrame(f.loc[f.To_Hole1 <= a])
	golf_puttd1 = pd.DataFrame(golf_putt1.loc[golf_putt1.To_Hole1 > b])
	golf_puttdistance1 = pd.DataFrame(golf_puttd1.loc[golf_puttd1.Unit_1 == 'FT'])
	golf_puttdistance1m = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_2 == 'Made'])
	golf_puttdistance1mi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_3 == 'Made'])
	golf_puttdistance1mimi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_4 == 'Made'])
	golf_puttdistance1mimimi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_5 == 'Made'])
	golf_putt2 = pd.DataFrame(f.loc[f.To_Hole2 <= a])
	golf_puttd2 = pd.DataFrame(golf_putt2.loc[golf_putt2.To_Hole2 > b])
	golf_puttdistance2 = pd.DataFrame(golf_puttd2.loc[golf_puttd2.Unit_2 == 'FT'])
	golf_puttdistance2m = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_3 == 'Made'])
	golf_puttdistance2mi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_4 == 'Made'])
	golf_puttdistance2mimi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_5 == 'Made'])
	golf_puttdistance2mimimi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_6 == 'Made'])
	golf_putt3 = pd.DataFrame(f.loc[f.To_Hole3 <= a])
	golf_puttd3 = pd.DataFrame(golf_putt3.loc[golf_putt3.To_Hole3 > b])
	golf_puttdistance3 = pd.DataFrame(golf_puttd3.loc[golf_puttd3.Unit_3 == 'FT'])
	golf_puttdistance3m = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_4 == 'Made'])
	golf_puttdistance3mi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_5 == 'Made'])
	golf_puttdistance3mimi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_6 == 'Made'])
	golf_puttdistance3mimimi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_7 == 'Made'])
	golf_putt4 = pd.DataFrame(f.loc[f.To_Hole4 <= a])
	golf_puttd4 = pd.DataFrame(golf_putt4.loc[golf_putt4.To_Hole4 > b])
	golf_puttdistance4 = pd.DataFrame(golf_puttd4.loc[golf_puttd4.Unit_4 == 'FT'])
	golf_puttdistance4m = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_5 == 'Made'])
	golf_puttdistance4mi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_6 == 'Made'])
	golf_puttdistance4mimi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_7 == 'Made'])
	golf_puttdistance4mimimi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_8 == 'Made'])
	golf_putt5 = pd.DataFrame(f.loc[f.To_Hole5 <= a])
	golf_puttd5 = pd.DataFrame(golf_putt5.loc[golf_putt5.To_Hole5 > b])
	golf_puttdistance5 = pd.DataFrame(golf_puttd5.loc[golf_puttd5.Unit_5 == 'FT'])
	golf_puttdistance5m = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_6 == 'Made'])
	golf_puttdistance5mi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_7 == 'Made'])
	golf_puttdistance5mimi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_8 == 'Made'])
	golf_puttdistance5mimimi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_9 == 'Made'])
	golf_putt6 = pd.DataFrame(f.loc[f.To_Hole6 <= a])
	golf_puttd6 = pd.DataFrame(golf_putt6.loc[golf_putt6.To_Hole6 > b])
	golf_puttdistance6 = pd.DataFrame(golf_puttd6.loc[golf_puttd6.Unit_6 == 'FT'])
	golf_puttdistance6m = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_7 == 'Made'])
	golf_puttdistance6mi = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_8 == 'Made'])
	golf_puttdistance6mimi = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_9 == 'Made'])
	golf_putt7 = pd.DataFrame(f.loc[f.To_Hole7 <= a])
	golf_puttd7 = pd.DataFrame(golf_putt7.loc[golf_putt7.To_Hole7 > b])
	golf_puttdistance7 = pd.DataFrame(golf_puttd7.loc[golf_puttd7.Unit_7 == 'FT'])
	golf_puttdistance7m = pd.DataFrame(golf_puttdistance7.loc[golf_puttdistance7.Result_8 == 'Made'])
	golf_puttdistance7mi = pd.DataFrame(golf_puttdistance7.loc[golf_puttdistance7.Result_9 == 'Made'])
	golf_puttlength = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) + len(golf_puttdistance6) + len(golf_puttdistance7)
	print(golf_puttlength, '1')
	golf_puttlength2 = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) + len(golf_puttdistance6) 
	print(golf_puttlength2, '2')
	golf_puttlength3 = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) 
	print(golf_puttlength3, '3')
	golf_1putt = len(golf_puttdistance1m) + len(golf_puttdistance2m) + len(golf_puttdistance3m) + len(golf_puttdistance4m) + len(golf_puttdistance5m) + len(golf_puttdistance6m) + len(golf_puttdistance7m)
	golf_2putt = len(golf_puttdistance1mi) + len(golf_puttdistance2mi) + len(golf_puttdistance3mi) + len(golf_puttdistance4mi) + len(golf_puttdistance5mi) + len(golf_puttdistance6mi) + len(golf_puttdistance7mi)
	golf_3putt = len(golf_puttdistance1mimi) + len(golf_puttdistance2mimi) + len(golf_puttdistance3mimi) + len(golf_puttdistance4mimi) + len(golf_puttdistance5mimi) + len(golf_puttdistance6mimi)
	golf_4putt = len(golf_puttdistance1mimimi) + len(golf_puttdistance2mimimi) + len(golf_puttdistance3mimimi) + len(golf_puttdistance4mimimi) + len(golf_puttdistance5mimimi)
	print(golf_4putt)
	golf_1puttp = golf_1putt/golf_puttlength
	golf_2puttp = golf_2putt/golf_puttlength 
	golf_3puttp = golf_3putt/golf_puttlength
	golf_4puttp = golf_4putt/golf_puttlength
	#print('1 putt percentage:', golf_1putt/golf_puttlength)
	#print('2 putt percentage:', golf_2putt/golf_puttlength)
	#print('3 putt percentage:', golf_3putt/golf_puttlength)
	golf_puttrange = np.array([golf_1puttp, golf_2puttp, golf_3puttp, golf_4puttp])
	print('text', golf_puttrange)
	print('text', np.sum(golf_puttrange))
	return golf_puttrange
	
golf_pp = [golf_ft03, golf_ft45, golf_ft68, golf_ft912, golf_ft1317, golf_ft1825, golf_ft2635, golf_ft3645, golf_ft4655, golf_ft5665]
for x in putt_num:
	f = golf_ft
	a = golf_puttbins[x]
	b = golf_puttbins2[x]
	golf_puttrange = putting_distances(f, a, b)
	golf_pp[x] = np.append(golf_pp[x], golf_puttrange)

golf_ft03 = golf_pp[0]
golf_ft45 = golf_pp[1]
golf_ft68 = golf_pp[2]
golf_ft912 = golf_pp[3]
golf_ft1317 = golf_pp[4]
golf_ft1825 = golf_pp[5]
golf_ft2635 = golf_pp[6]
golf_ft3645 = golf_pp[7]

#print(golf_ft)
golf_f4s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 4])
golf_ft4s1 = pd.DataFrame(golf_f4s1.loc[golf_f4s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft4s1m = pd.DataFrame(golf_ft4s1.loc[golf_ft4s1.Result_2 == 'Made'])
golf_f4s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 4])
golf_ft4s2 = pd.DataFrame(golf_f4s2.loc[golf_f4s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft4s2m = pd.DataFrame(golf_ft4s2.loc[golf_ft4s2.Result_3 == 'Made'])
golf_f4s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 4])
golf_ft4s3 = pd.DataFrame(golf_f4s3.loc[golf_f4s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft4s3m = pd.DataFrame(golf_ft4s3.loc[golf_ft4s3.Result_4 == 'Made'])
golf_f4s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 4])
golf_ft4s4 = pd.DataFrame(golf_f4s4.loc[golf_f4s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft4s4m = pd.DataFrame(golf_ft4s4.loc[golf_ft4s4.Result_5 == 'Made'])
golf_f4s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 4])
golf_ft4s5 = pd.DataFrame(golf_f4s5.loc[golf_f4s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft4s5m = pd.DataFrame(golf_ft4s5.loc[golf_ft4s5.Result_6 == 'Made'])
golf_f4s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 4])
golf_ft4s6 = pd.DataFrame(golf_f4s6.loc[golf_f4s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft4s6m = pd.DataFrame(golf_ft4s6.loc[golf_ft4s6.Result_7 == 'Made'])
golf_f4s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 4])
golf_ft4s7 = pd.DataFrame(golf_f4s7.loc[golf_f4s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft4s7m = pd.DataFrame(golf_ft4s7.loc[golf_ft4s7.Result_8 == 'Made'])
print("4 foot make percentage", (len(golf_ft4s1m) + len(golf_ft4s2m) + len(golf_ft4s3m) + len(golf_ft4s4m) + len(golf_ft4s5m) + len(golf_ft4s6m) + len(golf_ft4s7m))/(len(golf_ft4s1) + len(golf_ft4s2) +len(golf_ft4s3) + len(golf_ft4s4) + len(golf_ft4s5) + len(golf_ft4s6) + len(golf_ft4s7)) * 100)

golf_f5s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 5])
golf_ft5s1 = pd.DataFrame(golf_f5s1.loc[golf_f5s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft5s1m = pd.DataFrame(golf_ft5s1.loc[golf_ft5s1.Result_2 == 'Made'])
golf_f5s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 5])
golf_ft5s2 = pd.DataFrame(golf_f5s2.loc[golf_f5s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft5s2m = pd.DataFrame(golf_ft5s2.loc[golf_ft5s2.Result_3 == 'Made'])
golf_f5s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 5])
golf_ft5s3 = pd.DataFrame(golf_f5s3.loc[golf_f5s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft5s3m = pd.DataFrame(golf_ft5s3.loc[golf_ft5s3.Result_4 == 'Made'])
golf_f5s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 5])
golf_ft5s4 = pd.DataFrame(golf_f5s4.loc[golf_f5s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft5s4m = pd.DataFrame(golf_ft5s4.loc[golf_ft5s4.Result_5 == 'Made'])
golf_f5s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 5])
golf_ft5s5 = pd.DataFrame(golf_f5s5.loc[golf_f5s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft5s5m = pd.DataFrame(golf_ft5s5.loc[golf_ft5s5.Result_6 == 'Made'])
golf_f5s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 5])
golf_ft5s6 = pd.DataFrame(golf_f5s6.loc[golf_f5s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft5s6m = pd.DataFrame(golf_ft5s6.loc[golf_ft5s6.Result_7 == 'Made'])
golf_f5s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 5])
golf_ft5s7 = pd.DataFrame(golf_f5s7.loc[golf_f5s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft5s7m = pd.DataFrame(golf_ft5s7.loc[golf_ft5s7.Result_8 == 'Made'])
print("5 foot make percentage", (len(golf_ft5s1m) + len(golf_ft5s2m) + len(golf_ft5s3m) + len(golf_ft5s4m) + len(golf_ft5s5m) + len(golf_ft5s6m) + len(golf_ft5s7m))/(len(golf_ft5s1) + len(golf_ft5s2) +len(golf_ft5s3) + len(golf_ft5s4) + len(golf_ft5s5) + len(golf_ft5s6) + len(golf_ft5s7)) * 100)

golf_f6s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 6])
golf_ft6s1 = pd.DataFrame(golf_f6s1.loc[golf_f6s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft6s1m = pd.DataFrame(golf_ft6s1.loc[golf_ft6s1.Result_2 == 'Made'])
golf_f6s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 6])
golf_ft6s2 = pd.DataFrame(golf_f6s2.loc[golf_f6s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft6s2m = pd.DataFrame(golf_ft6s2.loc[golf_ft6s2.Result_3 == 'Made'])
golf_f6s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 6])
golf_ft6s3 = pd.DataFrame(golf_f6s3.loc[golf_f6s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft6s3m = pd.DataFrame(golf_ft6s3.loc[golf_ft6s3.Result_4 == 'Made'])
golf_f6s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 6])
golf_ft6s4 = pd.DataFrame(golf_f6s4.loc[golf_f6s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft6s4m = pd.DataFrame(golf_ft6s4.loc[golf_ft6s4.Result_5 == 'Made'])
golf_f6s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 6])
golf_ft6s5 = pd.DataFrame(golf_f6s5.loc[golf_f6s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft6s5m = pd.DataFrame(golf_ft6s5.loc[golf_ft6s5.Result_6 == 'Made'])
golf_f6s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 6])
golf_ft6s6 = pd.DataFrame(golf_f6s6.loc[golf_f6s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft6s6m = pd.DataFrame(golf_ft6s6.loc[golf_ft6s6.Result_7 == 'Made'])
golf_f6s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 6])
golf_ft6s7 = pd.DataFrame(golf_f6s7.loc[golf_f6s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft6s7m = pd.DataFrame(golf_ft6s7.loc[golf_ft6s7.Result_8 == 'Made'])
print("6 foot make percentage", (len(golf_ft6s1m) + len(golf_ft6s2m) + len(golf_ft6s3m) + len(golf_ft6s4m) + len(golf_ft6s5m) + len(golf_ft6s6m) + len(golf_ft6s7m))/(len(golf_ft6s1) + len(golf_ft6s2) +len(golf_ft6s3) + len(golf_ft6s4) + len(golf_ft6s5) + len(golf_ft6s6) + len(golf_ft6s7)) * 100)

golf_f7s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 7])
golf_ft7s1 = pd.DataFrame(golf_f7s1.loc[golf_f7s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft7s1m = pd.DataFrame(golf_ft7s1.loc[golf_ft7s1.Result_2 == 'Made'])
golf_f7s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 7])
golf_ft7s2 = pd.DataFrame(golf_f7s2.loc[golf_f7s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft7s2m = pd.DataFrame(golf_ft7s2.loc[golf_ft7s2.Result_3 == 'Made'])
golf_f7s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 7])
golf_ft7s3 = pd.DataFrame(golf_f7s3.loc[golf_f7s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft7s3m = pd.DataFrame(golf_ft7s3.loc[golf_ft7s3.Result_4 == 'Made'])
golf_f7s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 7])
golf_ft7s4 = pd.DataFrame(golf_f7s4.loc[golf_f7s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft7s4m = pd.DataFrame(golf_ft7s4.loc[golf_ft7s4.Result_5 == 'Made'])
golf_f7s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 7])
golf_ft7s5 = pd.DataFrame(golf_f7s5.loc[golf_f7s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft7s5m = pd.DataFrame(golf_ft7s5.loc[golf_ft7s5.Result_6 == 'Made'])
golf_f7s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 7])
golf_ft7s6 = pd.DataFrame(golf_f7s6.loc[golf_f7s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft7s6m = pd.DataFrame(golf_ft7s6.loc[golf_ft7s6.Result_7 == 'Made'])
golf_f7s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 7])
golf_ft7s7 = pd.DataFrame(golf_f7s7.loc[golf_f7s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft7s7m = pd.DataFrame(golf_ft7s7.loc[golf_ft7s7.Result_8 == 'Made'])
print("7 foot make percentage", (len(golf_ft7s1m) + len(golf_ft7s2m) + len(golf_ft7s3m) + len(golf_ft7s4m) + len(golf_ft7s5m) + len(golf_ft7s6m) + len(golf_ft7s7m))/(len(golf_ft7s1) + len(golf_ft7s2) +len(golf_ft7s3) + len(golf_ft7s4) + len(golf_ft7s5) + len(golf_ft7s6) + len(golf_ft7s7)) * 100)

golf_f8s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 8])
golf_ft8s1 = pd.DataFrame(golf_f8s1.loc[golf_f8s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft8s1m = pd.DataFrame(golf_ft8s1.loc[golf_ft8s1.Result_2 == 'Made'])
golf_f8s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 8])
golf_ft8s2 = pd.DataFrame(golf_f8s2.loc[golf_f8s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft8s2m = pd.DataFrame(golf_ft8s2.loc[golf_ft8s2.Result_3 == 'Made'])
golf_f8s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 8])
golf_ft8s3 = pd.DataFrame(golf_f8s3.loc[golf_f8s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft8s3m = pd.DataFrame(golf_ft8s3.loc[golf_ft8s3.Result_4 == 'Made'])
golf_f8s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 8])
golf_ft8s4 = pd.DataFrame(golf_f8s4.loc[golf_f8s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft8s4m = pd.DataFrame(golf_ft8s4.loc[golf_ft8s4.Result_5 == 'Made'])
golf_f8s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 8])
golf_ft8s5 = pd.DataFrame(golf_f8s5.loc[golf_f8s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft8s5m = pd.DataFrame(golf_ft8s5.loc[golf_ft8s5.Result_6 == 'Made'])
golf_f8s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 8])
golf_ft8s6 = pd.DataFrame(golf_f8s6.loc[golf_f8s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft8s6m = pd.DataFrame(golf_ft8s6.loc[golf_ft8s6.Result_7 == 'Made'])
golf_f8s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 8])
golf_ft8s7 = pd.DataFrame(golf_f8s7.loc[golf_f8s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft8s7m = pd.DataFrame(golf_ft8s7.loc[golf_ft8s7.Result_8 == 'Made'])
print("8 foot make percentage", (len(golf_ft8s1m) + len(golf_ft8s2m) + len(golf_ft8s3m) + len(golf_ft8s4m) + len(golf_ft8s5m) + len(golf_ft8s6m) + len(golf_ft8s7m))/(len(golf_ft8s1) + len(golf_ft8s2) +len(golf_ft8s3) + len(golf_ft8s4) + len(golf_ft8s5) + len(golf_ft8s6) + len(golf_ft8s7)) * 100)

golf_f9s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 9])
golf_ft9s1 = pd.DataFrame(golf_f9s1.loc[golf_f9s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft9s1m = pd.DataFrame(golf_ft9s1.loc[golf_ft9s1.Result_2 == 'Made'])
golf_f9s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 9])
golf_ft9s2 = pd.DataFrame(golf_f9s2.loc[golf_f9s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft9s2m = pd.DataFrame(golf_ft9s2.loc[golf_ft9s2.Result_3 == 'Made'])
golf_f9s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 9])
golf_ft9s3 = pd.DataFrame(golf_f9s3.loc[golf_f9s3.Unit_3 == 'FT'])
#print(golf_ft9s3)
golf_ft9s3m = pd.DataFrame(golf_ft9s3.loc[golf_ft9s3.Result_4 == 'Made'])
golf_f9s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 9])
golf_ft9s4 = pd.DataFrame(golf_f9s4.loc[golf_f9s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft9s4m = pd.DataFrame(golf_ft9s4.loc[golf_ft9s4.Result_5 == 'Made'])
golf_f9s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 9])
golf_ft9s5 = pd.DataFrame(golf_f9s5.loc[golf_f9s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft9s5m = pd.DataFrame(golf_ft9s5.loc[golf_ft9s5.Result_6 == 'Made'])
golf_f9s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 9])
golf_ft9s6 = pd.DataFrame(golf_f9s6.loc[golf_f9s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft9s6m = pd.DataFrame(golf_ft9s6.loc[golf_ft9s6.Result_7 == 'Made'])
golf_f9s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 9])
golf_ft9s7 = pd.DataFrame(golf_f9s7.loc[golf_f9s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft9s7m = pd.DataFrame(golf_ft8s7.loc[golf_ft8s7.Result_8 == 'Made'])
print("9 foot make percentage", (len(golf_ft9s1m) + len(golf_ft9s2m) + len(golf_ft9s3m) + len(golf_ft9s4m) + len(golf_ft9s5m) + len(golf_ft9s6m) + len(golf_ft9s7m))/(len(golf_ft9s1) + len(golf_ft9s2) +len(golf_ft9s3) + len(golf_ft9s4) + len(golf_ft9s5) + len(golf_ft9s6) + len(golf_ft9s7)) * 100)

golf_f10s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 == 10])
golf_ft10s1 = pd.DataFrame(golf_f10s1.loc[golf_f10s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft10s1m = pd.DataFrame(golf_ft10s1.loc[golf_ft10s1.Result_2 == 'Made'])
golf_f10s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 == 10])
golf_ft10s2 = pd.DataFrame(golf_f10s2.loc[golf_f10s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft10s2m = pd.DataFrame(golf_ft10s2.loc[golf_ft10s2.Result_3 == 'Made'])
golf_f10s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 == 10])
golf_ft10s3 = pd.DataFrame(golf_f10s3.loc[golf_f10s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft10s3m = pd.DataFrame(golf_ft10s3.loc[golf_ft10s3.Result_4 == 'Made'])
golf_f10s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 == 10])
golf_ft10s4 = pd.DataFrame(golf_f10s4.loc[golf_f10s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft10s4m = pd.DataFrame(golf_ft10s4.loc[golf_ft10s4.Result_5 == 'Made'])
golf_f10s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 == 10])
golf_ft10s5 = pd.DataFrame(golf_f10s5.loc[golf_f10s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft10s5m = pd.DataFrame(golf_ft10s5.loc[golf_ft10s5.Result_6 == 'Made'])
golf_f10s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 == 10])
golf_ft10s6 = pd.DataFrame(golf_f10s6.loc[golf_f10s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft10s6m = pd.DataFrame(golf_ft10s6.loc[golf_ft10s6.Result_7 == 'Made'])
golf_f10s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 == 10])
golf_ft10s7 = pd.DataFrame(golf_f10s7.loc[golf_f10s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft10s7m = pd.DataFrame(golf_ft10s7.loc[golf_ft10s7.Result_8 == 'Made'])
print("10 foot make percentage", (len(golf_ft10s1m) + len(golf_ft10s2m) + len(golf_ft10s3m) + len(golf_ft10s4m) + len(golf_ft10s5m) + len(golf_ft10s6m) + len(golf_ft10s7m))/(len(golf_ft10s1) + len(golf_ft10s2) +len(golf_ft10s3) + len(golf_ft10s4) + len(golf_ft10s5) + len(golf_ft10s6) + len(golf_ft10s7)) * 100)

golf_ftG10s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 11])
golf_f1015s1 = pd.DataFrame(golf_ftG10s1[golf_ftG10s1.To_Hole1 <= 15])
golf_ft1015s1 = pd.DataFrame(golf_f1015s1.loc[golf_f1015s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft1015s1m = pd.DataFrame(golf_ft1015s1.loc[golf_ft1015s1.Result_2 == 'Made'])
golf_ftG10s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 11])
golf_f1015s2 = pd.DataFrame(golf_ftG10s2[golf_ftG10s2.To_Hole2 <= 15])
golf_ft1015s2 = pd.DataFrame(golf_f1015s2.loc[golf_f1015s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft1015s2m = pd.DataFrame(golf_ft1015s2.loc[golf_ft1015s2.Result_3 == 'Made'])
golf_ftG10s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 11])
golf_f1015s3 = pd.DataFrame(golf_ftG10s3[golf_ftG10s3.To_Hole3 <= 15])
golf_ft1015s3 = pd.DataFrame(golf_f1015s3.loc[golf_f1015s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft1015s3m = pd.DataFrame(golf_ft1015s3.loc[golf_ft1015s3.Result_4 == 'Made'])
golf_ftG10s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 11])
golf_f1015s4 = pd.DataFrame(golf_ftG10s4[golf_ftG10s4.To_Hole4 <= 15])
golf_ft1015s4 = pd.DataFrame(golf_f1015s4.loc[golf_f1015s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft1015s4m = pd.DataFrame(golf_ft1015s4.loc[golf_ft1015s4.Result_5 == 'Made'])
golf_ftG10s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 11])
golf_f1015s5 = pd.DataFrame(golf_ftG10s5[golf_ftG10s5.To_Hole5 <= 15])
golf_ft1015s5 = pd.DataFrame(golf_f1015s5.loc[golf_f1015s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft1015s5m = pd.DataFrame(golf_ft1015s5.loc[golf_ft1015s5.Result_6 == 'Made'])
golf_ftG10s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 11])
golf_f1015s6 = pd.DataFrame(golf_ftG10s6[golf_ftG10s6.To_Hole6 <= 15])
golf_ft1015s6 = pd.DataFrame(golf_f1015s6.loc[golf_f1015s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft1015s6m = pd.DataFrame(golf_ft1015s6.loc[golf_ft1015s6.Result_7 == 'Made'])
golf_ftG10s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 >= 11])
golf_f1015s7 = pd.DataFrame(golf_ftG10s7[golf_ftG10s7.To_Hole7 <= 15])
golf_ft1015s7 = pd.DataFrame(golf_f1015s7.loc[golf_f1015s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft1015s7m = pd.DataFrame(golf_ft1015s7.loc[golf_ft1015s7.Result_8 == 'Made'])
print("11-15 foot make percentage", (len(golf_ft1015s1m) + len(golf_ft1015s2m) + len(golf_ft1015s3m) + len(golf_ft1015s4m) + len(golf_ft1015s5m) + len(golf_ft1015s6m) + len(golf_ft1015s7m))/(len(golf_ft1015s1) + len(golf_ft1015s2) +len(golf_ft1015s3) + len(golf_ft1015s4) + len(golf_ft1015s5) + len(golf_ft1015s6) + len(golf_ft1015s7)) * 100)

golf_ftG15s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 16])
golf_f1520s1 = pd.DataFrame(golf_ftG15s1[golf_ftG15s1.To_Hole1 <= 20])
golf_ft1520s1 = pd.DataFrame(golf_f1520s1.loc[golf_f1520s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft1520s1m = pd.DataFrame(golf_ft1520s1.loc[golf_ft1520s1.Result_2 == 'Made'])
golf_ftG15s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 16])
golf_f1520s2 = pd.DataFrame(golf_ftG15s2[golf_ftG15s2.To_Hole2 <= 20])
golf_ft1520s2 = pd.DataFrame(golf_f1520s2.loc[golf_f1520s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft1520s2m = pd.DataFrame(golf_ft1520s2.loc[golf_ft1520s2.Result_3 == 'Made'])
golf_ftG15s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 16])
golf_f1520s3 = pd.DataFrame(golf_ftG15s3[golf_ftG15s3.To_Hole3 <= 20])
golf_ft1520s3 = pd.DataFrame(golf_f1520s3.loc[golf_f1520s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft1520s3m = pd.DataFrame(golf_ft1520s3.loc[golf_ft1520s3.Result_4 == 'Made'])
golf_ftG15s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 16])
golf_f1520s4 = pd.DataFrame(golf_ftG15s4[golf_ftG15s4.To_Hole4 <= 20])
golf_ft1520s4 = pd.DataFrame(golf_f1520s4.loc[golf_f1520s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft1520s4m = pd.DataFrame(golf_ft1520s4.loc[golf_ft1520s4.Result_5 == 'Made'])
golf_ftG15s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 16])
golf_f1520s5 = pd.DataFrame(golf_ftG15s5[golf_ftG15s5.To_Hole5 <= 20])
golf_ft1520s5 = pd.DataFrame(golf_f1520s5.loc[golf_f1520s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft1520s5m = pd.DataFrame(golf_ft1520s5.loc[golf_ft1520s5.Result_6 == 'Made'])
golf_ftG15s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 16])
golf_f1520s6 = pd.DataFrame(golf_ftG15s6[golf_ftG15s6.To_Hole6 <= 20])
golf_ft1520s6 = pd.DataFrame(golf_f1520s6.loc[golf_f1520s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft1520s6m = pd.DataFrame(golf_ft1520s6.loc[golf_ft1520s6.Result_7 == 'Made'])
golf_ftG15s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 >= 16])
golf_f1520s7 = pd.DataFrame(golf_ftG15s7[golf_ftG15s7.To_Hole7 <= 20])
golf_ft1520s7 = pd.DataFrame(golf_f1520s7.loc[golf_f1520s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft1520s7m = pd.DataFrame(golf_ft1520s7.loc[golf_ft1520s7.Result_8 == 'Made'])
print("16-20 foot make percentage", (len(golf_ft1520s1m) + len(golf_ft1520s2m) + len(golf_ft1520s3m) + len(golf_ft1520s4m) + len(golf_ft1520s5m) + len(golf_ft1520s6m) + len(golf_ft1520s7m))/(len(golf_ft1520s1) + len(golf_ft1520s2) +len(golf_ft1520s3) + len(golf_ft1520s4) + len(golf_ft1520s5) + len(golf_ft1520s6) + len(golf_ft1520s7)) * 100)

golf_fG20s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 21])
golf_f2030s1 = pd.DataFrame(golf_fG20s1[golf_fG20s1.To_Hole1 <= 30])
golf_ft2030s1 = pd.DataFrame(golf_f2030s1.loc[golf_f2030s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft2030s1m = pd.DataFrame(golf_ft2030s1.loc[golf_ft2030s1.Result_2 == 'Made'])
golf_fG20s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 21])
golf_f2030s2 = pd.DataFrame(golf_fG20s2[golf_fG20s2.To_Hole2 <= 30])
golf_ft2030s2 = pd.DataFrame(golf_f2030s2.loc[golf_f2030s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft2030s2m = pd.DataFrame(golf_ft2030s2.loc[golf_ft2030s2.Result_3 == 'Made'])
golf_fG20s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 21])
golf_f2030s3 = pd.DataFrame(golf_fG20s3[golf_fG20s3.To_Hole3 <= 30])
golf_ft2030s3 = pd.DataFrame(golf_f2030s3.loc[golf_f2030s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft2030s3m = pd.DataFrame(golf_ft2030s3.loc[golf_ft2030s3.Result_4 == 'Made'])
golf_fG20s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 21])
golf_f2030s4 = pd.DataFrame(golf_fG20s4[golf_fG20s4.To_Hole4 <= 30])
golf_ft2030s4 = pd.DataFrame(golf_f2030s4.loc[golf_f2030s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft2030s4m = pd.DataFrame(golf_ft2030s4.loc[golf_ft2030s4.Result_5 == 'Made'])
golf_fG20s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 21])
golf_f2030s5 = pd.DataFrame(golf_fG20s5[golf_fG20s5.To_Hole5 <= 30])
golf_ft2030s5 = pd.DataFrame(golf_f2030s5.loc[golf_f2030s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft2030s5m = pd.DataFrame(golf_ft2030s5.loc[golf_ft2030s5.Result_6 == 'Made'])
golf_fG20s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 21])
golf_f2030s6 = pd.DataFrame(golf_fG20s6[golf_fG20s6.To_Hole6 <= 30])
golf_ft2030s6 = pd.DataFrame(golf_f2030s6.loc[golf_f2030s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft2030s6m = pd.DataFrame(golf_ft2030s6.loc[golf_ft2030s6.Result_7 == 'Made'])
golf_fG20s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 >= 21])
golf_f2030s7 = pd.DataFrame(golf_fG20s7[golf_fG20s7.To_Hole7 <= 30])
golf_ft2030s7 = pd.DataFrame(golf_f2030s7.loc[golf_f2030s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft2030s7m = pd.DataFrame(golf_ft2030s7.loc[golf_ft2030s7.Result_8 == 'Made'])
print("21-30 foot make percentage", (len(golf_ft2030s1m) + len(golf_ft2030s2m) + len(golf_ft2030s3m) + len(golf_ft2030s4m) + len(golf_ft2030s5m) + len(golf_ft2030s6m) + len(golf_ft2030s7m))/(len(golf_ft2030s1) + len(golf_ft2030s2) +len(golf_ft2030s3) + len(golf_ft2030s4) + len(golf_ft2030s5) + len(golf_ft2030s6) + len(golf_ft2030s7)) * 100)

golf_fG30s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 31])
golf_f3040s1 = pd.DataFrame(golf_fG30s1[golf_fG30s1.To_Hole1 <= 40])
golf_ft3040s1 = pd.DataFrame(golf_f3040s1.loc[golf_f3040s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft3040s1m = pd.DataFrame(golf_ft3040s1.loc[golf_ft3040s1.Result_2 == 'Made'])
golf_fG30s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 31])
golf_f3040s2 = pd.DataFrame(golf_fG30s2[golf_fG30s2.To_Hole2 <= 40])
golf_ft3040s2 = pd.DataFrame(golf_f3040s2.loc[golf_f3040s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft3040s2m = pd.DataFrame(golf_ft3040s2.loc[golf_ft3040s2.Result_3 == 'Made'])
golf_fG30s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 31])
golf_f3040s3 = pd.DataFrame(golf_fG30s3[golf_fG30s3.To_Hole3 <= 40])
golf_ft3040s3 = pd.DataFrame(golf_f3040s3.loc[golf_f3040s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft3040s3m = pd.DataFrame(golf_ft3040s3.loc[golf_ft3040s3.Result_4 == 'Made'])
golf_fG30s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 31])
golf_f3040s4 = pd.DataFrame(golf_fG30s4[golf_fG30s4.To_Hole4 <= 40])
golf_ft3040s4 = pd.DataFrame(golf_f3040s4.loc[golf_f3040s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft3040s4m = pd.DataFrame(golf_ft3040s4.loc[golf_ft3040s4.Result_5 == 'Made'])
golf_fG30s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 31])
golf_f3040s5 = pd.DataFrame(golf_fG30s5[golf_fG30s5.To_Hole5 <= 40])
golf_ft3040s5 = pd.DataFrame(golf_f3040s5.loc[golf_f3040s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft3040s5m = pd.DataFrame(golf_ft3040s5.loc[golf_ft3040s5.Result_6 == 'Made'])
golf_fG30s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 31])
golf_f3040s6 = pd.DataFrame(golf_fG30s6[golf_fG30s6.To_Hole6 <= 40])
golf_ft3040s6 = pd.DataFrame(golf_f3040s6.loc[golf_f3040s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft3040s6m = pd.DataFrame(golf_ft3040s6.loc[golf_ft3040s6.Result_7 == 'Made'])
golf_fG30s7 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole7 >= 31])
golf_f3040s7 = pd.DataFrame(golf_fG30s7[golf_fG30s7.To_Hole7 <= 40])
golf_ft3040s7 = pd.DataFrame(golf_f3040s7.loc[golf_f3040s7.Unit_7 == 'FT'])
#print(golf_ft4s7)
golf_ft3040s7m = pd.DataFrame(golf_ft3040s7.loc[golf_ft3040s7.Result_8 == 'Made'])
print("31-40 foot make percentage", (len(golf_ft3040s1m) + len(golf_ft3040s2m) + len(golf_ft3040s3m) + len(golf_ft3040s4m) + len(golf_ft3040s5m) + len(golf_ft3040s6m) + len(golf_ft3040s7m))/(len(golf_ft3040s1) + len(golf_ft3040s2) +len(golf_ft3040s3) + len(golf_ft3040s4) + len(golf_ft3040s5) + len(golf_ft3040s6) + len(golf_ft3040s7)) * 100)

golf_fG20s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 20])
golf_f2025s1 = pd.DataFrame(golf_fG20s1[golf_fG20s1.To_Hole1 <= 25])
golf_ft2025s1 = pd.DataFrame(golf_f2025s1.loc[golf_f2025s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft2025s1mi = pd.DataFrame(golf_ft2025s1.loc[golf_ft2025s1.Result_3 == 'Miss'])
golf_fG20s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 20])
golf_f2025s2 = pd.DataFrame(golf_fG20s2[golf_fG20s2.To_Hole2 <= 25])
golf_ft2025s2 = pd.DataFrame(golf_f2025s2.loc[golf_f2025s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft2025s2mi = pd.DataFrame(golf_ft2025s2.loc[golf_ft2025s2.Result_4 == 'Miss'])
golf_fG20s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 20])
golf_f2025s3 = pd.DataFrame(golf_fG20s3[golf_fG20s3.To_Hole3 <= 25])
golf_ft2025s3 = pd.DataFrame(golf_f2025s3.loc[golf_f2025s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft2025s3mi = pd.DataFrame(golf_ft2025s3.loc[golf_ft2025s3.Result_5 == 'Miss'])
golf_fG20s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 20])
golf_f2025s4 = pd.DataFrame(golf_fG20s4[golf_fG20s4.To_Hole4 <= 25])
golf_ft2025s4 = pd.DataFrame(golf_f2025s4.loc[golf_f2025s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft2025s4mi = pd.DataFrame(golf_ft2025s4.loc[golf_ft2025s4.Result_6 == 'Miss'])
golf_fG20s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 20])
golf_f2025s5 = pd.DataFrame(golf_fG20s5[golf_fG20s5.To_Hole5 <= 25])
golf_ft2025s5 = pd.DataFrame(golf_f2025s5.loc[golf_f2025s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft2025s5mi = pd.DataFrame(golf_ft2025s5.loc[golf_ft2025s5.Result_7 == 'Miss'])
golf_fG20s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 20])
golf_f2025s6 = pd.DataFrame(golf_fG20s6[golf_fG20s6.To_Hole6 <= 25])
golf_ft2025s6 = pd.DataFrame(golf_f2025s6.loc[golf_f2025s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft2025s6mi = pd.DataFrame(golf_ft2025s6.loc[golf_ft2025s6.Result_8 == 'Miss'])
print("20-25 foot 3-putt percentage", (len(golf_ft2025s1mi) + len(golf_ft2025s2mi) + len(golf_ft2025s3mi) + len(golf_ft2025s4mi) + len(golf_ft2025s5mi) + len(golf_ft2025s6mi))/(len(golf_ft2025s1) + len(golf_ft2025s2) +len(golf_ft2025s3) + len(golf_ft2025s4) + len(golf_ft2025s5) + len(golf_ft2025s6)) * 100)

golf_fG25s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 26])
golf_f2530s1 = pd.DataFrame(golf_fG25s1[golf_fG25s1.To_Hole1 <= 30])
golf_ft2530s1 = pd.DataFrame(golf_f2530s1.loc[golf_f2530s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft2530s1mi = pd.DataFrame(golf_ft2530s1.loc[golf_ft2530s1.Result_3 == 'Miss'])
golf_fG25s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 26])
golf_f2530s2 = pd.DataFrame(golf_fG25s2[golf_fG25s2.To_Hole2 <= 30])
golf_ft2530s2 = pd.DataFrame(golf_f2530s2.loc[golf_f2530s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft2530s2mi = pd.DataFrame(golf_ft2530s2.loc[golf_ft2530s2.Result_4 == 'Miss'])
golf_fG25s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 26])
golf_f2530s3 = pd.DataFrame(golf_fG25s3[golf_fG25s3.To_Hole3 <= 30])
golf_ft2530s3 = pd.DataFrame(golf_f2530s3.loc[golf_f2530s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft2530s3mi = pd.DataFrame(golf_ft2530s3.loc[golf_ft2530s3.Result_5 == 'Miss'])
golf_fG25s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 26])
golf_f2530s4 = pd.DataFrame(golf_fG25s4[golf_fG25s4.To_Hole4 <= 30])
golf_ft2530s4 = pd.DataFrame(golf_f2530s4.loc[golf_f2530s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft2530s4mi = pd.DataFrame(golf_ft2530s4.loc[golf_ft2530s4.Result_6 == 'Miss'])
golf_fG25s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 26])
golf_f2530s5 = pd.DataFrame(golf_fG25s5[golf_fG25s5.To_Hole5 <= 30])
golf_ft2530s5 = pd.DataFrame(golf_f2530s5.loc[golf_f2530s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft2530s5mi = pd.DataFrame(golf_ft2530s5.loc[golf_ft2530s5.Result_7 == 'Miss'])
golf_fG25s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 26])
golf_f2530s6 = pd.DataFrame(golf_fG25s6[golf_fG25s6.To_Hole6 <= 30])
golf_ft2530s6 = pd.DataFrame(golf_f2530s6.loc[golf_f2530s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft2530s6mi = pd.DataFrame(golf_ft2530s6.loc[golf_ft2530s6.Result_8 == 'Miss'])
print("26-30 foot 3-putt percentage", (len(golf_ft2530s1mi) + len(golf_ft2530s2mi) + len(golf_ft2530s3mi) + len(golf_ft2530s4mi) + len(golf_ft2530s5mi) + len(golf_ft2530s6mi))/(len(golf_ft2530s1) + len(golf_ft2530s2) +len(golf_ft2530s3) + len(golf_ft2530s4) + len(golf_ft2530s5) + len(golf_ft2530s6)) * 100)

golf_fG30s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 31])
golf_f3035s1 = pd.DataFrame(golf_fG30s1[golf_fG30s1.To_Hole1 <= 35])
golf_ft3035s1 = pd.DataFrame(golf_f3035s1.loc[golf_f3035s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft3035s1mi = pd.DataFrame(golf_ft3035s1.loc[golf_ft3035s1.Result_3 == 'Miss'])
golf_fG30s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 31])
golf_f3035s2 = pd.DataFrame(golf_fG30s2[golf_fG30s2.To_Hole2 <= 35])
golf_ft3035s2 = pd.DataFrame(golf_f3035s2.loc[golf_f3035s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft3035s2mi = pd.DataFrame(golf_ft3035s2.loc[golf_ft3035s2.Result_4 == 'Miss'])
golf_fG30s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 31])
golf_f3035s3 = pd.DataFrame(golf_fG30s3[golf_fG30s3.To_Hole3 <= 35])
golf_ft3035s3 = pd.DataFrame(golf_f3035s3.loc[golf_f3035s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft3035s3mi = pd.DataFrame(golf_ft3035s3.loc[golf_ft3035s3.Result_5 == 'Miss'])
golf_fG30s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 31])
golf_f3035s4 = pd.DataFrame(golf_fG30s4[golf_fG30s4.To_Hole4 <= 35])
golf_ft3035s4 = pd.DataFrame(golf_f3035s4.loc[golf_f3035s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft3035s4mi = pd.DataFrame(golf_ft3035s4.loc[golf_ft3035s4.Result_6 == 'Miss'])
golf_fG30s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 31])
golf_f3035s5 = pd.DataFrame(golf_fG30s5[golf_fG30s5.To_Hole5 <= 35])
golf_ft3035s5 = pd.DataFrame(golf_f3035s5.loc[golf_f3035s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft3035s5mi = pd.DataFrame(golf_ft3035s5.loc[golf_ft3035s5.Result_7 == 'Miss'])
golf_fG30s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 31])
golf_f3035s6 = pd.DataFrame(golf_fG30s6[golf_fG30s6.To_Hole6 <= 35])
golf_ft3035s6 = pd.DataFrame(golf_f3035s6.loc[golf_f3035s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft3035s6mi = pd.DataFrame(golf_ft3035s6.loc[golf_ft3035s6.Result_8 == 'Miss'])
print("31-35 foot 3-putt percentage", (len(golf_ft3035s1mi) + len(golf_ft3035s2mi) + len(golf_ft3035s3mi) + len(golf_ft3035s4mi) + len(golf_ft3035s5mi) + len(golf_ft3035s6mi))/(len(golf_ft3035s1) + len(golf_ft3035s2) +len(golf_ft3035s3) + len(golf_ft3035s4) + len(golf_ft3035s5) + len(golf_ft3035s6)) * 100)

golf_fG35s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 36])
golf_f3540s1 = pd.DataFrame(golf_fG35s1[golf_fG35s1.To_Hole1 <= 40])
golf_ft3540s1 = pd.DataFrame(golf_f3540s1.loc[golf_f3540s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft3540s1mi = pd.DataFrame(golf_ft3540s1.loc[golf_ft3540s1.Result_3 == 'Miss'])
golf_fG35s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 36])
golf_f3540s2 = pd.DataFrame(golf_fG35s2[golf_fG35s2.To_Hole2 <= 40])
golf_ft3540s2 = pd.DataFrame(golf_f3540s2.loc[golf_f3540s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft3540s2mi = pd.DataFrame(golf_ft3540s2.loc[golf_ft3540s2.Result_4 == 'Miss'])
golf_fG35s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 36])
golf_f3540s3 = pd.DataFrame(golf_fG35s3[golf_fG35s3.To_Hole3 <= 40])
golf_ft3540s3 = pd.DataFrame(golf_f3540s3.loc[golf_f3540s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft3540s3mi = pd.DataFrame(golf_ft3540s3.loc[golf_ft3540s3.Result_5 == 'Miss'])
golf_fG35s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 36])
golf_f3540s4 = pd.DataFrame(golf_fG35s4[golf_fG35s4.To_Hole4 <=40])
golf_ft3540s4 = pd.DataFrame(golf_f3540s4.loc[golf_f3540s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft3540s4mi = pd.DataFrame(golf_ft3540s4.loc[golf_ft3540s4.Result_6 == 'Miss'])
golf_fG35s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 36])
golf_f3540s5 = pd.DataFrame(golf_fG35s5[golf_fG35s5.To_Hole5 <= 40])
golf_ft3540s5 = pd.DataFrame(golf_f3540s5.loc[golf_f3540s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft3540s5mi = pd.DataFrame(golf_ft3540s5.loc[golf_ft3540s5.Result_7 == 'Miss'])
golf_fG35s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 36])
golf_f3540s6 = pd.DataFrame(golf_fG35s6[golf_fG35s6.To_Hole6 <= 40])
golf_ft3540s6 = pd.DataFrame(golf_f3540s6.loc[golf_f3540s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft3540s6mi = pd.DataFrame(golf_ft3540s6.loc[golf_ft3540s6.Result_8 == 'Miss'])
print("36-40 3-putt percentage", (len(golf_ft3540s1mi) + len(golf_ft3540s2mi) + len(golf_ft3540s3mi) + len(golf_ft3540s4mi) + len(golf_ft3540s5mi) + len(golf_ft3540s6mi))/(len(golf_ft3540s1) + len(golf_ft3540s2) +len(golf_ft3540s3) + len(golf_ft3540s4) + len(golf_ft3540s5) + len(golf_ft3540s6)) * 100)

golf_fG40s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 41])
golf_f4050s1 = pd.DataFrame(golf_fG40s1[golf_fG40s1.To_Hole1 <= 50])
golf_ft4050s1 = pd.DataFrame(golf_f4050s1.loc[golf_f4050s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ft4050s1mi = pd.DataFrame(golf_ft3540s1.loc[golf_ft3540s1.Result_3 == 'Miss'])
golf_fG40s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 41])
golf_f4050s2 = pd.DataFrame(golf_fG40s2[golf_fG40s2.To_Hole2 <= 50])
golf_ft4050s2 = pd.DataFrame(golf_f4050s2.loc[golf_f4050s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ft4050s2mi = pd.DataFrame(golf_ft4050s2.loc[golf_ft4050s2.Result_4 == 'Miss'])
golf_fG40s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 41])
golf_f4050s3 = pd.DataFrame(golf_fG40s3[golf_fG40s3.To_Hole3 <= 50])
golf_ft4050s3 = pd.DataFrame(golf_f4050s3.loc[golf_f4050s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ft4050s3mi = pd.DataFrame(golf_ft4050s3.loc[golf_ft4050s3.Result_5 == 'Miss'])
golf_fG40s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 41])
golf_f4050s4 = pd.DataFrame(golf_fG40s4[golf_fG40s4.To_Hole4 <=50])
golf_ft4050s4 = pd.DataFrame(golf_f4050s4.loc[golf_f4050s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ft4050s4mi = pd.DataFrame(golf_ft4050s4.loc[golf_ft4050s4.Result_6 == 'Miss'])
golf_fG40s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 41])
golf_f4050s5 = pd.DataFrame(golf_fG40s5[golf_fG40s5.To_Hole5 <= 50])
golf_ft4050s5 = pd.DataFrame(golf_f4050s5.loc[golf_f4050s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ft4050s5mi = pd.DataFrame(golf_ft4050s5.loc[golf_ft4050s5.Result_7 == 'Miss'])
golf_fG40s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 41])
golf_f4050s6 = pd.DataFrame(golf_fG40s6[golf_fG40s6.To_Hole6 <= 50])
golf_ft4050s6 = pd.DataFrame(golf_f4050s6.loc[golf_f4050s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ft4050s6mi = pd.DataFrame(golf_ft4050s6.loc[golf_ft4050s6.Result_8 == 'Miss'])
print("41-50 foot 3-putt percentage", (len(golf_ft4050s1mi) + len(golf_ft4050s2mi) + len(golf_ft4050s3mi) + len(golf_ft4050s4mi) + len(golf_ft4050s5mi) + len(golf_ft4050s6mi))/(len(golf_ft4050s1) + len(golf_ft4050s2) +len(golf_ft4050s3) + len(golf_ft4050s4) + len(golf_ft4050s5) + len(golf_ft4050s6)) * 100)

golf_fG50s1 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole1 >= 50])
golf_ftG50s1 = pd.DataFrame(golf_fG50s1.loc[golf_fG50s1.Unit_1 == 'FT'])
#print(golf_ft4s1)
golf_ftG50s1mi = pd.DataFrame(golf_ftG50s1.loc[golf_ftG50s1.Result_3 == 'Miss'])
golf_fG50s2 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole2 >= 50])
golf_ftG50s2 = pd.DataFrame(golf_fG50s2.loc[golf_fG50s2.Unit_2 == 'FT'])
#print(golf_ft4s2)
golf_ftG50s2mi = pd.DataFrame(golf_ftG50s2.loc[golf_ftG50s2.Result_4 == 'Miss'])
golf_fG50s3 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole3 >= 50])
golf_ftG50s3 = pd.DataFrame(golf_fG50s3.loc[golf_fG50s3.Unit_3 == 'FT'])
#print(golf_ft4s3)
golf_ftG50s3mi = pd.DataFrame(golf_ftG50s3.loc[golf_ftG50s3.Result_5 == 'Miss'])
golf_fG50s4 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole4 >= 50])
golf_ftG50s4 = pd.DataFrame(golf_fG50s4.loc[golf_fG50s4.Unit_4 == 'FT'])
#print(golf_ft4s4)
golf_ftG50s4mi = pd.DataFrame(golf_ftG50s4.loc[golf_ftG50s4.Result_6 == 'Miss'])
golf_fG50s5 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole5 >= 50])
golf_ftG50s5 = pd.DataFrame(golf_fG50s5.loc[golf_fG50s5.Unit_5 == 'FT'])
#print(golf_ft4s5)
golf_ftG50s5mi = pd.DataFrame(golf_ftG50s5.loc[golf_ftG50s5.Result_7 == 'Miss'])
golf_fG50s6 = pd.DataFrame(golf_ft.loc[golf_ft.To_Hole6 >= 50])
golf_ftG50s6 = pd.DataFrame(golf_fG50s6.loc[golf_fG50s6.Unit_6 == 'FT'])
#print(golf_ft4s6)
golf_ftG50s6mi = pd.DataFrame(golf_ftG50s6.loc[golf_ftG50s6.Result_8 == 'Miss'])
print("50+ foot 3-putt percentage", (len(golf_ftG50s1mi) + len(golf_ftG50s2mi) + len(golf_ftG50s3mi) + len(golf_ftG50s4mi) + len(golf_ftG50s5mi) + len(golf_ftG50s6mi))/(len(golf_ftG50s1) + len(golf_ftG50s2) +len(golf_ftG50s3) + len(golf_ftG50s4) + len(golf_ftG50s5) + len(golf_ftG50s6)) * 100)

golf_3L125 = pd.DataFrame(golf_3.loc[golf_3.Yard <= 125])
golf_3125150s = pd.DataFrame(golf_3.loc[golf_3.Yard >= 125])
golf_3150175s = pd.DataFrame(golf_3.loc[golf_3.Yard >= 150])
golf_3175200s = pd.DataFrame(golf_3.loc[golf_3.Yard >= 175])
golf_3G200 = pd.DataFrame(golf_3.loc[golf_3.Yard >= 200])

golf_4L325 = pd.DataFrame(golf_4.loc[golf_4.Yard <= 325])
golf_4325350s = pd.DataFrame(golf_4.loc[golf_4.Yard >= 325])
golf_4350375s = pd.DataFrame(golf_4.loc[golf_4.Yard >= 350])
golf_4375400s = pd.DataFrame(golf_4.loc[golf_4.Yard >= 375])
golf_4400425s = pd.DataFrame(golf_4.loc[golf_4.Yard >= 400])
golf_4G425 = pd.DataFrame(golf_4.loc[golf_4.Yard >= 425])

golf_5L450 = pd.DataFrame(golf_5.loc[golf_5.Yard <= 450])
golf_5450475s = pd.DataFrame(golf_5.loc[golf_5.Yard >= 450])
golf_5475500s = pd.DataFrame(golf_5.loc[golf_5.Yard >= 475])
golf_5500525s = pd.DataFrame(golf_5.loc[golf_5.Yard >= 500])
golf_5525550s = pd.DataFrame(golf_5.loc[golf_5.Yard >= 525])
golf_5G550 = pd.DataFrame(golf_5.loc[golf_5.Yard >= 550])

golf_3125150 = pd.DataFrame(golf_3125150s.loc[golf_3125150s.Yard <= 150])
golf_3150175 = pd.DataFrame(golf_3150175s.loc[golf_3150175s.Yard <= 175])
golf_3175200 = pd.DataFrame(golf_3175200s.loc[golf_3175200s.Yard <= 200])

golf_4325350 = pd.DataFrame(golf_4325350s.loc[golf_4325350s.Yard <= 350])
golf_4350375 = pd.DataFrame(golf_4350375s.loc[golf_4350375s.Yard <= 375])
golf_4375400 = pd.DataFrame(golf_4375400s.loc[golf_4375400s.Yard <= 400])
golf_4400425 = pd.DataFrame(golf_4400425s.loc[golf_4400425s.Yard <= 425])

golf_5450475 = pd.DataFrame(golf_5450475s.loc[golf_5450475s.Yard <= 475])
golf_5475500 = pd.DataFrame(golf_5475500s.loc[golf_5475500s.Yard <= 500])
golf_5500525 = pd.DataFrame(golf_5500525s.loc[golf_5500525s.Yard <= 525])
golf_5525550 = pd.DataFrame(golf_5525550s.loc[golf_5525550s.Yard <= 550])

golf_3L125sc = np.array(golf_3L125.Score)
golf_3L125yd = np.array(golf_3L125.Yard)
golf_3L125m = np.mean(golf_3L125sc)
golf_3125150sc = np.array(golf_3125150.Score)
golf_3125150yd = np.array(golf_3125150.Yard)
golf_3125150m = np.mean(golf_3125150sc)
golf_3150175sc = np.array(golf_3150175.Score)
golf_3150175yd = np.array(golf_3150175.Yard)
golf_3150175m = np.mean(golf_3150175sc)
golf_3175200sc = np.array(golf_3175200.Score)
golf_3175200yd = np.array(golf_3175200.Yard)
golf_3175200m = np.mean(golf_3175200sc)
golf_3G200sc = np.array(golf_3G200.Score)
golf_3G200yd = np.array(golf_3G200.Yard)
golf_3G200m = np.mean(golf_3G200sc)

golf_4L325sc = np.array(golf_4L325.Score)
golf_4L325m = np.mean(golf_4L325sc)
golf_4325350sc = np.array(golf_4325350.Score)
golf_4325350m = np.mean(golf_4325350sc)
golf_4350375sc = np.array(golf_4350375.Score)
golf_4350375m = np.mean(golf_4350375sc)
golf_4375400sc = np.array(golf_4375400.Score)
golf_4375400m = np.mean(golf_4375400sc)
golf_4400425sc = np.array(golf_4400425.Score)
golf_4400425m = np.mean(golf_4400425sc)
golf_4G425sc = np.array(golf_4G425.Score)
golf_4G425m = np.mean(golf_4G425sc)

golf_5L450sc = np.array(golf_5L450.Score)
golf_5L450m = np.mean(golf_5L450sc)
golf_5450475sc = np.array(golf_5450475.Score)
golf_5450475m = np.mean(golf_5450475sc)
golf_5475500sc = np.array(golf_5475500.Score)
golf_5475500m = np.mean(golf_5475500sc)
golf_5500525sc = np.array(golf_5500525.Score)
golf_5500525m = np.mean(golf_5500525sc)
golf_5G550sc = np.array(golf_5G550.Score)
golf_5G550m = np.mean(golf_5G550sc)

npf_3L125p = pd.DataFrame(golf_3L125.loc[golf_3L125.Unit_1 == "FT"])
npy_3L125p = pd.DataFrame(golf_3L125.loc[golf_3L125.Unit_1 == "Yard"])
feet_3L125p = np.array(npf_3L125p.To_Hole1)
yard_3L125p = np.array(npy_3L125p.To_Hole1)
yard_3L125pcl = yard_3L125p * 3
golf_3L125p = np.append(yard_3L125pcl, feet_3L125p)
golf_3L125pm = np.mean(golf_3L125p)
print('Proximity on par 3s < 125 yards', golf_3L125pm)

npf_3175200p = pd.DataFrame(golf_3175200.loc[golf_3175200.Unit_1 == "FT"])
npy_3175200p = pd.DataFrame(golf_3175200.loc[golf_3175200.Unit_1 == "Yard"])
feet_3175200p = np.array(npf_3175200p.To_Hole1)
yard_3175200p = np.array(npy_3175200p.To_Hole1)
yard_3175200pcl = yard_3175200p * 3
golf_3175200p = np.append(yard_3175200pcl, feet_3175200p)
golf_3175200pm = np.mean(golf_3175200p)
print('Proximity on par 3s 175-200 yards', golf_3175200pm)

npf_3G200p = pd.DataFrame(golf_3G200.loc[golf_3G200.Unit_1 == "FT"])
npy_3G200p = pd.DataFrame(golf_3G200.loc[golf_3G200.Unit_1 == "Yard"])
feet_3G200p = np.array(npf_3G200p.To_Hole1)
yard_3G200p = np.array(npy_3G200p.To_Hole1)
yard_3G200pcl = yard_3G200p * 3
golf_3G200p = np.append(yard_3G200pcl, feet_3G200p)
golf_3G200pm = np.mean(golf_3G200p)
print('Proximity on par 3s > 200 yards', golf_3G200pm)

npf_4L325p = pd.DataFrame(golf_4L325.loc[golf_4L325.Unit_2 == "FT"])
npy_4L325p = pd.DataFrame(golf_4L325.loc[golf_4L325.Unit_2 == "Yard"])
feet_4L325p = np.array(npf_4L325p.To_Hole2)
yard_4L325p = np.array(npy_4L325p.To_Hole2)
yard_4L325pcl = yard_4L325p * 3
golf_4L325p = np.append(yard_4L325pcl, feet_4L325p)
golf_4L325pm = np.mean(golf_4L325p)
print('Proximity on par 4s < 325 yards', golf_4L325pm)

npf_4325350p = pd.DataFrame(golf_4325350.loc[golf_4325350.Unit_2 == "FT"])
npy_4325350p = pd.DataFrame(golf_4325350.loc[golf_4325350.Unit_2 == "Yard"])
feet_4325350p = np.array(npf_4325350p.To_Hole2)
yard_4325350p = np.array(npy_4325350p.To_Hole2)
yard_4325350pcl = yard_4325350p * 3
golf_4325350p = np.append(yard_4325350pcl, feet_4325350p)
golf_4325350pm = np.mean(golf_4325350p)
print('Proximity on par 4s 325-350 yards', golf_4325350pm)

npf_4350375p = pd.DataFrame(golf_4350375.loc[golf_4350375.Unit_2 == "FT"])
npy_4350375p = pd.DataFrame(golf_4350375.loc[golf_4350375.Unit_2 == "Yard"])
feet_4350375p = np.array(npf_4350375p.To_Hole2)
yard_4350375p = np.array(npy_4350375p.To_Hole2)
yard_4350375pcl = yard_4350375p * 3
golf_4350375p = np.append(yard_4350375pcl, feet_4350375p)
golf_4350375pm = np.mean(golf_4350375p)
print('Proximity on par 4s 350-375 yards', golf_4350375pm)

npf_4375400p = pd.DataFrame(golf_4375400.loc[golf_4375400.Unit_2 == "FT"])
npy_4375400p = pd.DataFrame(golf_4375400.loc[golf_4375400.Unit_2 == "Yard"])
feet_4375400p = np.array(npf_4375400p.To_Hole2)
yard_4375400p = np.array(npy_4375400p.To_Hole2)
yard_4375400pcl = yard_4375400p * 3
golf_4375400p = np.append(yard_4375400pcl, feet_4325350p)
golf_4375400pm = np.mean(golf_4375400p)
print('Proximity on par 4s 375-400 yards', golf_4375400pm)

npf_4400425p = pd.DataFrame(golf_4400425.loc[golf_4400425.Unit_2 == "FT"])
npy_4400425p = pd.DataFrame(golf_4400425.loc[golf_4400425.Unit_2 == "Yard"])
feet_4400425p = np.array(npf_4400425p.To_Hole2)
yard_4400425p = np.array(npy_4400425p.To_Hole2)
yard_4400425pcl = yard_4400425p * 3
golf_4400425p = np.append(yard_4400425pcl, feet_4400425p)
golf_4400425pm = np.mean(golf_4400425p)
print('Proximity on par 4s 400-425 yards', golf_4400425pm)

npf_4G425p = pd.DataFrame(golf_4G425.loc[golf_4G425.Unit_2 == "FT"])
npy_4G425p = pd.DataFrame(golf_4G425.loc[golf_4G425.Unit_2 == "Yard"])
feet_4G425p = np.array(npf_4G425p.To_Hole2)
yard_4G425p = np.array(npy_4G425p.To_Hole2)
yard_4G425pcl = yard_4G425p * 3
golf_4G425p = np.append(yard_4G425pcl, feet_4G425p)
golf_4G425pm = np.mean(golf_4G425p)
print('Proximity on par 4s > 425 yards', golf_4G425pm)

npf_5L450p = pd.DataFrame(golf_5L450.loc[golf_5L450.Unit_3 == "FT"])
npy_5L450p = pd.DataFrame(golf_5L450.loc[golf_5L450.Unit_3 == "Yard"])
feet_5L450p = np.array(npf_5L450p.To_Hole3)
yard_5L450p = np.array(npy_5L450p.To_Hole3)
yard_5L450pcl = yard_5L450p * 3
golf_5L450p = np.append(yard_5L450pcl, feet_5L450p)
golf_5L450pm = np.mean(golf_5L450p)
print('Proximity on par 5s < 450 yards', golf_5L450pm)

npf_5450475p = pd.DataFrame(golf_5450475.loc[golf_5450475.Unit_3 == "FT"])
npy_5450475p = pd.DataFrame(golf_5450475.loc[golf_5450475.Unit_3 == "Yard"])
feet_5450475p = np.array(npf_5450475p.To_Hole3)
yard_5450475p = np.array(npy_5450475p.To_Hole3)
yard_5450475pcl = yard_5450475p * 3
golf_5450475p = np.append(yard_5450475pcl, feet_5450475p)
golf_5450475pm = np.mean(golf_5450475p)
print('Proximity on pr 5s 450-475 yards', golf_5450475pm)

npf_5475500p = pd.DataFrame(golf_5475500.loc[golf_5475500.Unit_3 == "FT"])
npy_5475500p = pd.DataFrame(golf_5475500.loc[golf_5475500.Unit_3 == "Yard"])
feet_5475500p = np.array(npf_5475500p.To_Hole3)
yard_5475500p = np.array(npy_5475500p.To_Hole3)
yard_5475500pcl = yard_5475500p * 3
golf_5475500p = np.append(yard_5475500pcl, feet_5475500p)
golf_5475500pm = np.mean(golf_5475500p)
print('Proximity on par 5s 475-500 yards', golf_5475500pm)

npf_5500525p = pd.DataFrame(golf_5500525.loc[golf_5500525.Unit_3 == "FT"])
npy_5500525p = pd.DataFrame(golf_5500525.loc[golf_5500525.Unit_3 == "Yard"])
feet_5500525p = np.array(npf_5500525p.To_Hole3)
yard_5500525p = np.array(npy_5500525p.To_Hole3)
yard_5500525pcl = yard_5500525p * 3
golf_5500525p = np.append(yard_5500525pcl, feet_5500525p)
golf_5500525pm = np.mean(golf_5500525p)
print('Proximity on par 5s 500-525 yards', golf_5500525pm)

npf_5525550p = pd.DataFrame(golf_5525550.loc[golf_5525550.Unit_3 == "FT"])
npy_5525550p = pd.DataFrame(golf_5525550.loc[golf_5525550.Unit_3 == "Yard"])
feet_5525550p = np.array(npf_5525550p.To_Hole3)
yard_5525550p = np.array(npy_5525550p.To_Hole3)
yard_5525550pcl = yard_5525550p * 3
golf_5525550p = np.append(yard_5525550pcl, feet_5525550p)
golf_5525550pm = np.mean(golf_5525550p)
print("Proximity on par 5s 525-550 yards", golf_5525550pm)

npf_5G550p = pd.DataFrame(golf_5G550.loc[golf_5G550.Unit_3 == "FT"])
npy_5G550p = pd.DataFrame(golf_5G550.loc[golf_5G550.Unit_3 == "Yard"])
feet_5G550p = np.array(npf_5G550p.To_Hole3)
yard_5G550p = np.array(npy_5G550p.To_Hole3)
yard_5G550pcl = yard_5G550p * 3
golf_5G550p = np.append(yard_5G550pcl, feet_5G550p)
golf_5G550pm = np.mean(golf_5G550p)
print("Proximity on par 5s > 550 yards", golf_5G550pm)

golf_312yd = np.append(golf_3L125yd, golf_3125150yd)
golf_3123yd = np.append(golf_312yd, golf_3150175yd)
golf_31234yd = np.append(golf_3123yd, golf_3175200yd)
golf_3yd = np.append(golf_31234yd, golf_3G200yd)
golf_312p = np.append(golf_3L125p, golf_3125150p)
golf_3123p = np.append(golf_312p, golf_3150175p)
golf_31234p = np.append(golf_3123p, golf_3175200p)
golf_3pt = np.append(golf_31234p, golf_3G200p)
print(np.count_nonzero(golf_3yd))
print(np.count_nonzero(golf_3pt))
#(np.corrcoef(golf_3yd, golf_3pt))
#plt.scatter(golf_3yd, golf_3pt)
#slope, intercept, r_value, p_value, std_err = stats.linregress(golf_3yd, golf_3pt)
#line = slope*golf_3yd+intercept
#plt.plot(golf_3yd, golf_3pt, golf_3yd, line)
#plt.show()

golf_52W1r = pd.DataFrame(golf.loc[golf.Club_1 == "52 Wedge"])
golf_52W1 = pd.DataFrame(golf_52W1r.loc[golf_52W1r.Yard <= 100])
golf_54W1r = pd.DataFrame(golf.loc[golf.Club_1 == "54 Wedge"])
golf_54W1 = pd.DataFrame(golf_54W1r.loc[golf_54W1r.Yard <= 100])
golf_5254W1 = golf_52W1.append(golf_54W1)

golf_52W2r = pd.DataFrame(golf.loc[golf.Club_2 == "52 Wedge"])
golf_52W2c = pd.DataFrame(golf_52W2r.loc[golf_52W2r.To_Hole1 <= 100])
golf_52W2 = pd.DataFrame(golf_52W2c.loc[golf_52W2c.To_Hole1 >= 40])
golf_54W2r = pd.DataFrame(golf.loc[golf.Club_2 == "54 Wedge"])
golf_54W2c = pd.DataFrame(golf_54W2r.loc[golf_54W2r.To_Hole1 <= 100])
golf_54W2 = pd.DataFrame(golf_54W2r.loc[golf_54W2r.To_Hole1 >= 40])
golf_5254W2 = golf_52W2.append(golf_54W2)

golf_52W3r = pd.DataFrame(golf.loc[golf.Club_3 == "52 Wedge"])
golf_52W3c = pd.DataFrame(golf_52W3r.loc[golf_52W3r.To_Hole2 <= 100])
golf_52W3 = pd.DataFrame(golf_52W3c.loc[golf_52W3c.To_Hole2 >= 40])
golf_54W3r = pd.DataFrame(golf.loc[golf.Club_3 == "54 Wedge"])
golf_54W3c = pd.DataFrame(golf_54W3r.loc[golf_54W3r.To_Hole2 <= 100])
golf_54W3 = pd.DataFrame(golf_54W3r.loc[golf_54W3r.To_Hole2 >= 40])
golf_5254W3 = golf_52W3.append(golf_54W3)

golf_48W1r = pd.DataFrame(golf.loc[golf.Club_1 == "48 Wedge"])
golf_48W1 = pd.DataFrame(golf_48W1r.loc[golf_48W1r.Yard <= 115])
golf_49W1r = pd.DataFrame(golf.loc[golf.Club_1 == "49 Wedge"])
golf_49W1 = pd.DataFrame(golf_49W1r.loc[golf_49W1r.Yard <= 115])
golf_4849W1 = golf_48W1.append(golf_49W1)

golf_48W2r = pd.DataFrame(golf.loc[golf.Club_2 == "48 Wedge"])
golf_48W2 = pd.DataFrame(golf_48W2r.loc[golf_48W2r.To_Hole1 <= 115])
golf_49W2r = pd.DataFrame(golf.loc[golf.Club_2 == "49 Wedge"])
golf_49W2 = pd.DataFrame(golf_49W2r.loc[golf_49W2r.To_Hole1 <= 115])
golf_4849W2 = golf_48W2.append(golf_49W2)

golf_48W3r = pd.DataFrame(golf.loc[golf.Club_3 == "48 Wedge"])
golf_48W3 = pd.DataFrame(golf_48W3r.loc[golf_48W3r.To_Hole2 <= 115])
golf_49W3r = pd.DataFrame(golf.loc[golf.Club_3 == "49 Wedge"])
golf_49W3 = pd.DataFrame(golf_49W3r.loc[golf_49W3r.To_Hole2 <= 115])
golf_4849W3 = golf_48W3.append(golf_49W3)

golf_PW1r = pd.DataFrame(golf.loc[golf.Club_1 == "P Wedge"])
golf_PW1 = pd.DataFrame(golf_PW1r.loc[golf_PW1r.Yard <= 125])
golf_PW2r = pd.DataFrame(golf.loc[golf.Club_2 == "P Wedge"])
golf_PW2 = pd.DataFrame(golf_PW2r.loc[golf_PW2r.To_Hole1 <= 125])
golf_PW3r = pd.DataFrame(golf.loc[golf.Club_3 == "P Wedge"])
golf_PW3 = pd.DataFrame(golf_PW3r.loc[golf_PW3r.To_Hole2 <= 125])
golf_9i1r = pd.DataFrame(golf.loc[golf.Club_1 == "9 Iron"])
golf_9i1 = pd.DataFrame(golf_9i1r.loc[golf_9i1r.Yard <= 140])
golf_9i2r = pd.DataFrame(golf.loc[golf.Club_2 == "9 Iron"])
golf_9i2 = pd.DataFrame(golf_9i2r.loc[golf_9i2r.To_Hole1 <= 140])
golf_9i3r = pd.DataFrame(golf.loc[golf.Club_3 == "9 Iron"])
golf_9i3 = pd.DataFrame(golf_9i3r.loc[golf_9i3r.To_Hole2 <= 140])

golf_8i1r = pd.DataFrame(golf.loc[golf.Club_1 == "8 Iron"])
golf_8i1 = pd.DataFrame(golf_8i1r.loc[golf_8i1r.Yard <= 155])
golf_8i2r = pd.DataFrame(golf.loc[golf.Club_2 == "8 Iron"])
golf_8i2 = pd.DataFrame(golf_8i2r.loc[golf_8i2r.To_Hole1 <= 155])
golf_8i3r = pd.DataFrame(golf.loc[golf.Club_3 == "8 Iron"])
golf_8i3 = pd.DataFrame(golf_8i3r.loc[golf_8i3r.To_Hole2 <= 155])

golf_7i1r = pd.DataFrame(golf.loc[golf.Club_1 == "7 Iron"])
golf_7i1 = pd.DataFrame(golf_7i1r.loc[golf_7i1r.Yard <= 165])
golf_7i2r = pd.DataFrame(golf.loc[golf.Club_2 == "7 Iron"])
golf_7i2 = pd.DataFrame(golf_7i2r.loc[golf_7i2r.To_Hole1 <= 165])
golf_7i3r = pd.DataFrame(golf.loc[golf.Club_3 == "7 Iron"])
golf_7i3 = pd.DataFrame(golf_7i3r.loc[golf_7i3r.To_Hole2 <= 165])

golf_6i1r = pd.DataFrame(golf.loc[golf.Club_1 == "6 Iron"])
golf_6i1 = pd.DataFrame(golf_6i1r.loc[golf_6i1r.Yard <= 175])
golf_6i2r = pd.DataFrame(golf.loc[golf.Club_2 == "6 Iron"])
golf_6i2 = pd.DataFrame(golf_6i2r.loc[golf_6i2r.To_Hole1 <= 175])
golf_6i3r = pd.DataFrame(golf.loc[golf.Club_3 == "6 Iron"])
golf_6i3 = pd.DataFrame(golf_6i3r.loc[golf_6i3r.To_Hole2 <= 175])

golf_5i1r = pd.DataFrame(golf.loc[golf.Club_1 == "5 Iron"])
golf_5i1 = pd.DataFrame(golf_5i1r.loc[golf_5i1r.Yard <= 185])
golf_5i2r = pd.DataFrame(golf.loc[golf.Club_2 == "5 Iron"])
golf_5i2 = pd.DataFrame(golf_5i2r.loc[golf_5i2r.To_Hole1 <= 185])
golf_5i3r = pd.DataFrame(golf.loc[golf.Club_3 == "5 Iron"])
golf_5i3 = pd.DataFrame(golf_5i3r.loc[golf_5i3r.To_Hole2 <= 185])

golf_4H1r = pd.DataFrame(golf.loc[golf.Club_1 == "Hybrid"])
golf_4H1 = pd.DataFrame(golf_4H1r.loc[golf_4H1r.Yard <= 200])
golf_4i1r = pd.DataFrame(golf.loc[golf.Club_1 == "4 Iron"])
golf_4i1 = pd.DataFrame(golf_4i1r.loc[golf_4i1r.Yard <= 200])
golf_4i4H1 = golf_4H1.append(golf_4i1)

golf_4H2r = pd.DataFrame(golf.loc[golf.Club_2 == "Hybrid"])
golf_4H2 = pd.DataFrame(golf_4H2r.loc[golf_4H2r.To_Hole1 <= 200])
golf_4i2r = pd.DataFrame(golf.loc[golf.Club_2 == "4 Iron"])
golf_4i2 = pd.DataFrame(golf_4i2r.loc[golf_4i2r.To_Hole1 <= 200])
golf_4i4H2 = golf_4H2.append(golf_4i2)

golf_4H3r = pd.DataFrame(golf.loc[golf.Club_3 == "Hybrid"])
golf_4H3 = pd.DataFrame(golf_4H3r.loc[golf_4H3r.To_Hole2 <= 200])
golf_4i3r = pd.DataFrame(golf.loc[golf.Club_3 == "4 Iron"])
golf_4i3 = pd.DataFrame(golf_4i3r.loc[golf_4i3r.To_Hole2 <= 200])
golf_4i4H3 = golf_4H3.append(golf_4i3)

golf_3H1r = pd.DataFrame(golf.loc[golf.Club_1 == "3 Hybrid"])
golf_3H1 = pd.DataFrame(golf_3H1r.loc[golf_3H1r.Yard <= 210])
golf_3H2r = pd.DataFrame(golf.loc[golf.Club_2 == "3 Hybrid"])
golf_3H2 = pd.DataFrame(golf_3H2r.loc[golf_3H2r.To_Hole1 <= 210])
golf_3H3r = pd.DataFrame(golf.loc[golf.Club_3 == "3 Hybrid"])
golf_3H3 = pd.DataFrame(golf_3H3r.loc[golf_3H3r.To_Hole2 <= 210])

golf_3W1r = pd.DataFrame(golf.loc[golf.Club_1 == "3 Wood"])
golf_3W1 = pd.DataFrame(golf_3W1r.loc[golf_3W1r.Yard <= 225])
golf_3W2r = pd.DataFrame(golf.loc[golf.Club_2 == "3 Wood"])
golf_3W2 = pd.DataFrame(golf_3W2r.loc[golf_3W2r.To_Hole1 <= 225])
golf_3W3r = pd.DataFrame(golf.loc[golf.Club_3 == "3 Wood"])
golf_3W3 = pd.DataFrame(golf_3W3r.loc[golf_3W3r.To_Hole2 <= 225])


npf_5254W1p = pd.DataFrame(golf_5254W1.loc[golf_5254W1.Unit_1 == "FT"])
npy_5254W1p = pd.DataFrame(golf_5254W1.loc[golf_5254W1.Unit_1 == "Yard"])
feet_5254W1p = np.array(npf_5254W1p.To_Hole1)
yard_5254W1p = np.array(npy_5254W1p.To_Hole1)
yard_5254W1pcl = yard_5254W1p * 3
golf_5254W1p = np.append(yard_5254W1pcl, feet_5254W1p)
golf_5254W1pm = np.mean(golf_5254W1p)

npf_5254W2p = pd.DataFrame(golf_5254W2.loc[golf_5254W2.Unit_2 == "FT"])
npy_5254W2p = pd.DataFrame(golf_5254W2.loc[golf_5254W2.Unit_2 == "Yard"])
feet_5254W2p = np.array(npf_5254W2p.To_Hole2)
yard_5254W2p = np.array(npy_5254W2p.To_Hole2)
yard_5254W2pcl = yard_5254W2p * 3
golf_5254W2p = np.append(yard_5254W2pcl, feet_5254W2p)
golf_5254W2pm = np.mean(golf_5254W2p)

npf_5254W3p = pd.DataFrame(golf_5254W3.loc[golf_5254W3.Unit_3 == "FT"])
npy_5254W3p = pd.DataFrame(golf_5254W3.loc[golf_5254W3.Unit_3 == "Yard"])
feet_5254W3p = np.array(npf_5254W3p.To_Hole3)
yard_5254W3p = np.array(npy_5254W3p.To_Hole3)
yard_5254W3pcl = yard_5254W3p * 3
golf_5254W3p = np.append(yard_5254W3pcl, feet_5254W3p)
golf_5254W3pm = np.mean(golf_5254W3p)

golf_5254op = np.append(golf_5254W3p, golf_5254W2p)
golf_5254o = np.append(golf_5254op, golf_5254W1p)
print('54 degree wedge proximity', np.mean(golf_5254o))

npf_4849W1p = pd.DataFrame(golf_4849W1.loc[golf_4849W1.Unit_1 == "FT"])
npy_4849W1p = pd.DataFrame(golf_4849W1.loc[golf_4849W1.Unit_1 == "Yard"])
feet_4849W1p = np.array(npf_4849W1p.To_Hole1)
yard_4849W1p = np.array(npy_4849W1p.To_Hole1)
yard_4849W1pcl = yard_4849W1p * 3
golf_4849W1p = np.append(yard_4849W1pcl, feet_4849W1p)
golf_4849W1pm = np.mean(golf_4849W1p)

npf_4849W2p = pd.DataFrame(golf_4849W2.loc[golf_4849W2.Unit_2 == "FT"])
npy_4849W2p = pd.DataFrame(golf_4849W2.loc[golf_4849W2.Unit_2 == "Yard"])
feet_4849W2p = np.array(npf_4849W2p.To_Hole2)
yard_4849W2p = np.array(npy_4849W2p.To_Hole2)
yard_4849W2pcl = yard_4849W2p * 3
golf_4849W2p = np.append(yard_4849W2pcl, feet_4849W2p)
golf_4849W2pm = np.mean(golf_4849W2p)

npf_4849W3p = pd.DataFrame(golf_4849W3.loc[golf_4849W3.Unit_3 == "FT"])
npy_4849W3p = pd.DataFrame(golf_4849W3.loc[golf_4849W3.Unit_3 == "Yard"])
feet_4849W3p = np.array(npf_4849W3p.To_Hole3)
yard_4849W3p = np.array(npy_4849W3p.To_Hole3)
yard_4849W3pcl = yard_4849W3p * 3
golf_4849W3p = np.append(yard_4849W3pcl, feet_4849W3p)
golf_4849W3pm = np.mean(golf_4849W3p)

golf_4849op = np.append(golf_4849W3p, golf_4849W2p)
golf_4849o = np.append(golf_4849op, golf_4849W1p)
print('49 degree wedge proximity', np.mean(golf_4849o))

npf_PW1p = pd.DataFrame(golf_PW1.loc[golf_PW1.Unit_1 == "FT"])
npy_PW1p = pd.DataFrame(golf_PW1.loc[golf_PW1.Unit_1 == "Yard"])
feet_PW1p = np.array(npf_PW1p.To_Hole1)
yard_PW1p = np.array(npy_PW1p.To_Hole1)
yard_PW1pcl = yard_PW1p * 3
golf_PW1p = np.append(yard_PW1pcl, feet_PW1p)
golf_PW1pm = np.mean(golf_PW1p)

npf_PW2p = pd.DataFrame(golf_PW2.loc[golf_PW2.Unit_2 == "FT"])
npy_PW2p = pd.DataFrame(golf_PW2.loc[golf_PW2.Unit_2 == "Yard"])
feet_PW2p = np.array(npf_PW2p.To_Hole2)
yard_PW2p = np.array(npy_PW1p.To_Hole2)
yard_PW2pcl = yard_PW2p * 3
golf_PW2p = np.append(yard_PW2pcl, feet_PW2p)
golf_PW2pm = np.mean(golf_PW2p)

npf_PW3p = pd.DataFrame(golf_PW3.loc[golf_PW3.Unit_3 == "FT"])
npy_PW3p = pd.DataFrame(golf_PW3.loc[golf_PW3.Unit_3 == "Yard"])
feet_PW3p = np.array(npf_PW3p.To_Hole3)
yard_PW3p = np.array(npy_PW3p.To_Hole3)
yard_PW3pcl = yard_PW3p * 3
golf_PW3p = np.append(yard_PW3pcl, feet_PW3p)
golf_PW3pm = np.mean(golf_PW3p)

golf_PWop = np.append(golf_PW3p, golf_PW2p)
golf_PWo = np.append(golf_PWop, golf_PW1p)

npf_9i1p = pd.DataFrame(golf_9i1.loc[golf_9i1.Unit_1 == "FT"])
npy_9i1p = pd.DataFrame(golf_9i1.loc[golf_9i1.Unit_1 == "Yard"])
feet_9i1p = np.array(npf_9i1p.To_Hole1)
yard_9i1p = np.array(npy_9i1p.To_Hole1)
yard_9i1pcl = yard_9i1p * 3
golf_9i1p = np.append(yard_9i1pcl, feet_9i1p)
golf_9i1pm = np.mean(golf_9i1p)

npf_9i2p = pd.DataFrame(golf_9i2.loc[golf_9i2.Unit_2 == "FT"])
npy_9i2p = pd.DataFrame(golf_9i2.loc[golf_9i2.Unit_2 == "Yard"])
feet_9i2p = np.array(npf_9i2p.To_Hole2)
yard_9i2p = np.array(npy_9i2p.To_Hole2)
yard_9i2pcl = yard_9i2p * 3
golf_9i2p = np.append(yard_9i2pcl, feet_9i2p)
golf_9i2pm = np.mean(golf_9i2p)

npf_9i3p = pd.DataFrame(golf_9i3.loc[golf_9i3.Unit_3 == "FT"])
npy_9i3p = pd.DataFrame(golf_9i3.loc[golf_9i3.Unit_3 == "Yard"])
feet_9i3p = np.array(npf_9i3p.To_Hole3)
yard_9i3p = np.array(npy_9i3p.To_Hole3)
yard_9i3pcl = yard_9i3p * 3
golf_9i3p = np.append(yard_9i3pcl, feet_9i3p)
golf_9i3pm = np.mean(golf_9i3p)

golf_9iop = np.append(golf_9i3p, golf_9i2p)
golf_9io = np.append(golf_9iop, golf_9i1p)

npf_8i1p = pd.DataFrame(golf_8i1.loc[golf_8i1.Unit_1 == "FT"])
npy_8i1p = pd.DataFrame(golf_8i1.loc[golf_8i1.Unit_1 == "Yard"])
feet_8i1p = np.array(npf_8i1p.To_Hole1)
yard_8i1p = np.array(npy_8i1p.To_Hole1)
yard_8i1pcl = yard_8i1p * 3
golf_8i1p = np.append(yard_8i1pcl, feet_8i1p)
golf_8i1pm = np.mean(golf_8i1p)

npf_8i2p = pd.DataFrame(golf_8i2.loc[golf_8i2.Unit_2 == "FT"])
npy_8i2p = pd.DataFrame(golf_8i2.loc[golf_8i2.Unit_2 == "Yard"])
feet_8i2p = np.array(npf_8i2p.To_Hole2)
yard_8i2p = np.array(npy_8i2p.To_Hole2)
yard_8i2pcl = yard_8i2p * 3
golf_8i2p = np.append(yard_8i2pcl, feet_8i2p)
golf_8i2pm = np.mean(golf_8i2p)

npf_8i3p = pd.DataFrame(golf_8i3.loc[golf_8i3.Unit_3 == "FT"])
npy_8i3p = pd.DataFrame(golf_8i3.loc[golf_8i3.Unit_3 == "Yard"])
feet_8i3p = np.array(npf_8i3p.To_Hole3)
yard_8i3p = np.array(npy_8i3p.To_Hole3)
yard_8i3pcl = yard_8i3p * 3
golf_8i3p = np.append(yard_8i3pcl, feet_8i3p)
golf_8i3pm = np.mean(golf_8i3p)

golf_8iop = np.append(golf_8i3p, golf_8i2p)
golf_8io = np.append(golf_8iop, golf_8i1p)

npf_7i1p = pd.DataFrame(golf_7i1.loc[golf_7i1.Unit_1 == "FT"])
npy_7i1p = pd.DataFrame(golf_7i1.loc[golf_7i1.Unit_1 == "Yard"])
feet_7i1p = np.array(npf_7i1p.To_Hole1)
yard_7i1p = np.array(npy_7i1p.To_Hole1)
yard_7i1pcl = yard_7i1p * 3
golf_7i1p = np.append(yard_7i1pcl, feet_7i1p)
golf_7i1pm = np.mean(golf_7i1p)

npf_7i2p = pd.DataFrame(golf_7i2.loc[golf_7i2.Unit_2 == "FT"])
npy_7i2p = pd.DataFrame(golf_7i2.loc[golf_7i2.Unit_2 == "Yard"])
feet_7i2p = np.array(npf_7i2p.To_Hole2)
yard_7i2p = np.array(npy_7i2p.To_Hole2)
yard_7i2pcl = yard_7i2p * 3
golf_7i2p = np.append(yard_7i2pcl, feet_7i2p)
golf_7i2pm = np.mean(golf_7i2p)

npf_7i3p = pd.DataFrame(golf_7i3.loc[golf_7i3.Unit_3 == "FT"])
npy_7i3p = pd.DataFrame(golf_7i3.loc[golf_7i3.Unit_3 == "Yard"])
feet_7i3p = np.array(npf_7i3p.To_Hole3)
yard_7i3p = np.array(npy_7i3p.To_Hole3)
yard_7i3pcl = yard_7i3p * 3
golf_7i3p = np.append(yard_7i3pcl, feet_7i3p)
golf_7i3pm = np.mean(golf_7i3p)

golf_7iop = np.append(golf_7i3p, golf_7i2p)
golf_7io = np.append(golf_7iop, golf_7i1p)

npf_6i1p = pd.DataFrame(golf_6i1.loc[golf_6i1.Unit_1 == "FT"])
npy_6i1p = pd.DataFrame(golf_6i1.loc[golf_6i1.Unit_1 == "Yard"])
feet_6i1p = np.array(npf_6i1p.To_Hole1)
yard_6i1p = np.array(npy_6i1p.To_Hole1)
yard_6i1pcl = yard_6i1p * 3
golf_6i1p = np.append(yard_6i1pcl, feet_6i1p)
golf_6i1pm = np.mean(golf_6i1p)

npf_6i2p = pd.DataFrame(golf_6i2.loc[golf_6i2.Unit_2 == "FT"])
npy_6i2p = pd.DataFrame(golf_6i2.loc[golf_6i2.Unit_2 == "Yard"])
feet_6i2p = np.array(npf_6i2p.To_Hole2)
yard_6i2p = np.array(npy_6i2p.To_Hole2)
yard_6i2pcl = yard_6i2p * 3
golf_6i2p = np.append(yard_6i2pcl, feet_6i2p)
golf_6i2pm = np.mean(golf_6i2p)

npf_6i3p = pd.DataFrame(golf_6i3.loc[golf_6i3.Unit_3 == "FT"])
npy_6i3p = pd.DataFrame(golf_6i3.loc[golf_6i3.Unit_3 == "Yard"])
feet_6i3p = np.array(npf_6i3p.To_Hole3)
yard_6i3p = np.array(npy_6i3p.To_Hole3)
yard_6i3pcl = yard_6i3p * 3
golf_6i3p = np.append(yard_6i3pcl, feet_6i3p)
golf_6i3pm = np.mean(golf_6i3p)

golf_6iop = np.append(golf_6i3p, golf_6i2p)
golf_6io = np.append(golf_6iop, golf_6i1p)

npf_5i1p = pd.DataFrame(golf_5i1.loc[golf_5i1.Unit_1 == "FT"])
npy_5i1p = pd.DataFrame(golf_5i1.loc[golf_5i1.Unit_1 == "Yard"])
feet_5i1p = np.array(npf_5i1p.To_Hole1)
yard_5i1p = np.array(npy_5i1p.To_Hole1)
yard_5i1pcl = yard_5i1p * 3
golf_5i1p = np.append(yard_5i1pcl, feet_5i1p)
golf_5i1pm = np.mean(golf_5i1p)

npf_5i2p = pd.DataFrame(golf_5i2.loc[golf_5i2.Unit_2 == "FT"])
npy_5i2p = pd.DataFrame(golf_5i2.loc[golf_5i2.Unit_2 == "Yard"])
feet_5i2p = np.array(npf_5i2p.To_Hole2)
yard_5i2p = np.array(npy_5i2p.To_Hole2)
yard_5i2pcl = yard_5i2p * 3
golf_5i2p = np.append(yard_5i2pcl, feet_5i2p)
golf_5i2pm = np.mean(golf_5i2p)

npf_5i3p = pd.DataFrame(golf_5i3.loc[golf_5i3.Unit_3 == "FT"])
npy_5i3p = pd.DataFrame(golf_5i3.loc[golf_5i3.Unit_3 == "Yard"])
feet_5i3p = np.array(npf_5i3p.To_Hole3)
yard_5i3p = np.array(npy_5i3p.To_Hole3)
yard_5i3pcl = yard_5i3p * 3
golf_5i3p = np.append(yard_5i3pcl, feet_5i3p)
golf_5i3pm = np.mean(golf_5i3p)

golf_5iop = np.append(golf_5i3p, golf_5i2p)
golf_5io = np.append(golf_5iop, golf_5i1p)

npf_4i4H1p = pd.DataFrame(golf_4i4H1.loc[golf_4i4H1.Unit_1 == "FT"])
npy_4i4H1p = pd.DataFrame(golf_4i4H1.loc[golf_4i4H1.Unit_1 == "Yard"])
feet_4i4H1p = np.array(npf_4i4H1p.To_Hole1)
yard_4i4H1p = np.array(npy_4i4H1p.To_Hole1)
yard_4i4H1pcl = yard_4i4H1p * 3
golf_4i4H1p = np.append(yard_4i4H1pcl, feet_4i4H1p)
golf_4i4H1pm = np.mean(golf_4i4H1p)

npf_4i4H2p = pd.DataFrame(golf_4i4H2.loc[golf_4i4H2.Unit_2 == "FT"])
npy_4i4H2p = pd.DataFrame(golf_4i4H2.loc[golf_4i4H2.Unit_2 == "Yard"])
feet_4i4H2p = np.array(npf_4i4H2p.To_Hole2)
yard_4i4H2p = np.array(npy_4i4H2p.To_Hole2)
yard_4i4H2pcl = yard_4i4H2p * 3
golf_4i4H2p = np.append(yard_4i4H2pcl, feet_4i4H2p)
golf_4i4H2pm = np.mean(golf_4i4H2p)

npf_4i4H3p = pd.DataFrame(golf_4i4H3.loc[golf_4i4H3.Unit_3 == "FT"])
npy_4i4H3p = pd.DataFrame(golf_4i4H3.loc[golf_4i4H3.Unit_3 == "Yard"])
feet_4i4H3p = np.array(npf_4i4H3p.To_Hole3)
yard_4i4H3p = np.array(npy_4i4H3p.To_Hole3)
yard_4i4H3pcl = yard_4i4H3p * 3
golf_4i4H3p = np.append(yard_4i4H3pcl, feet_4i4H3p)
golf_4i4H3pm = np.mean(golf_4i4H3p)

golf_4i4Hop = np.append(golf_4i4H3p, golf_4i4H2p)
golf_4i4Ho = np.append(golf_4i4Hop, golf_4i4H1p)

npf_3H1p = pd.DataFrame(golf_3H1.loc[golf_3H1.Unit_1 == "FT"])
npy_3H1p = pd.DataFrame(golf_3H1.loc[golf_3H1.Unit_1 == "Yard"])
feet_3H1p = np.array(npf_3H1p.To_Hole1)
yard_3H1p = np.array(npy_3H1p.To_Hole1)
yard_3H1pcl = yard_3H1p * 3
golf_3H1p = np.append(yard_3H1pcl, feet_3H1p)
golf_3H1pm = np.mean(golf_3H1p)

npf_3H2p = pd.DataFrame(golf_3H2.loc[golf_3H2.Unit_2 == "FT"])
npy_3H2p = pd.DataFrame(golf_3H2.loc[golf_3H2.Unit_2 == "Yard"])
feet_3H2p = np.array(npf_3H2p.To_Hole2)
yard_3H2p = np.array(npy_3H2p.To_Hole2)
yard_3H2pcl = yard_3H2p * 3
golf_3H2p = np.append(yard_3H2pcl, feet_3H2p)
golf_3H2pm = np.mean(golf_3H2p)

npf_3H3p = pd.DataFrame(golf_3H3.loc[golf_3H3.Unit_3 == "FT"])
npy_3H3p = pd.DataFrame(golf_3H3.loc[golf_3H3.Unit_3 == "Yard"])
feet_3H3p = np.array(npf_3H3p.To_Hole3)
yard_3H3p = np.array(npy_3H3p.To_Hole3)
yard_3H3pcl = yard_3H3p * 3
golf_3H3p = np.append(yard_3H3pcl, feet_3H3p)
golf_3H3pm = np.mean(golf_3H3p)

golf_3Hop = np.append(golf_3H3p, golf_3H2p)
golf_3Ho = np.append(golf_3Hop, golf_3H1p)

npf_3W1p = pd.DataFrame(golf_3W1.loc[golf_3W1.Unit_1 == "FT"])
npy_3W1p = pd.DataFrame(golf_3W1.loc[golf_3W1.Unit_1 == "Yard"])
feet_3W1p = np.array(npf_3W1p.To_Hole1)
yard_3W1p = np.array(npy_3W1p.To_Hole1)
yard_3W1pcl = yard_3W1p * 3
golf_3W1p = np.append(yard_3W1pcl, feet_3W1p)
golf_3W1pm = np.mean(golf_3W1p)

npf_3W2p = pd.DataFrame(golf_3W2.loc[golf_3W2.Unit_2 == "FT"])
npy_3W2p = pd.DataFrame(golf_3W2.loc[golf_3W2.Unit_2 == "Yard"])
feet_3W2p = np.array(npf_3W2p.To_Hole2)
yard_3W2p = np.array(npy_3W2p.To_Hole2)
yard_3W2pcl = yard_3W2p * 3
golf_3W2p = np.append(yard_3W2pcl, feet_3W2p)
golf_3W2pm = np.mean(golf_3W2p)

npf_3W3p = pd.DataFrame(golf_3W3.loc[golf_3W3.Unit_3 == "FT"])
npy_3W3p = pd.DataFrame(golf_3W3.loc[golf_3W3.Unit_3 == "Yard"])
feet_3W3p = np.array(npf_3W3p.To_Hole3)
yard_3W3p = np.array(npy_3W3p.To_Hole3)
yard_3W3pcl = yard_3W3p * 3
golf_3W3p = np.append(yard_3W3pcl, feet_3W3p)
golf_3W3pm = np.mean(golf_3W3p)

golf_3Wop = np.append(golf_3W3p, golf_3W2p)
golf_3Wo = np.append(golf_3Wop, golf_3W1p)
print(golf_3Wo, 'OG')


golf_approach = [golf_5254o, golf_4849o, golf_PWo, golf_9io, golf_8io, golf_7io, golf_6io, golf_5io, golf_4i4Ho, golf_3Ho, golf_3Wo]
approach_pie = ["54 degree wedge proximity", "49 degree wedge proximity", "Pitching wedge proximity", "9 Iron proximity", "8 Iron proximity", "7 Iron proximity", "6 Iron Proximity", "5 Iron proximity", "4 Iron proximity", "3 Hybrid proximity", "3 Wood proximity"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def pie(a, b):
	golf_xoof = pd.DataFrame(a, columns = ['proximity'])
	golf_x8 = pd.DataFrame(golf_xoof.loc[golf_xoof.proximity <= 8])
	golf_x20 = pd.DataFrame(golf_xoof.loc[golf_xoof.proximity <= 20])
	golf_x820 = pd.DataFrame(golf_x20.loc[golf_x20.proximity > 8])
	golf_x40 = pd.DataFrame(golf_xoof.loc[golf_xoof.proximity <= 40])
	golf_x2040 = pd.DataFrame(golf_x40.loc[golf_x40.proximity > 20])
	golf_x100 = pd.DataFrame(golf_xoof.loc[golf_xoof.proximity > 40])
	labels_1 = '0-8 feet', '9-20 feet', '21-40 feet', '40 feet and beyond'
	sizes_1 = [len(golf_x8), len(golf_x820), len(golf_x2040), len(golf_x100)]
	colors_1 = ['darkviolet', 'royalblue', 'lawngreen', 'cyan']
	explode_1 = (0.1, 0, 0, 0)
	plt.pie(sizes_1, explode = explode_1, labels = labels_1, colors = colors_1, autopct = '%.2f', shadow = True)
	plt.title(b)
	plt.show()

def bellcurve(a,b):
	a.sort()
	amean = np.mean(a)
	astd = np.std(a)
	pdf = stats.norm.pdf(a, amean, astd)
	plt.plot(a, pdf)
	plt.title(b)
	plt.show()
	
for x in num:
	a = golf_approach[x]
	b = approach_pie[x]
	#pie(a, b)
	#bellcurve(a,b)
	
def pie_2(a, b):
	golf_aoof = pd.DataFrame(a, columns = ['proximity'])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 5])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 8])
	golf_a68 = pd.DataFrame(golf_a8.loc[golf_a8.proximity > 5])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 12])
	golf_a912 = pd.DataFrame(golf_a12.loc[golf_a12.proximity > 8])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1317 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 12])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a1825 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 17])
	golf_a35 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 35])
	golf_a2635 = pd.DataFrame(golf_a35.loc[golf_a35.proximity > 25])
	golf_a45 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 45])
	golf_a3645 = pd.DataFrame(golf_a45.loc[golf_a45.proximity > 35])
	golf_a55 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 60])
	golf_a4660 = pd.DataFrame(golf_a55.loc[golf_a55.proximity > 45])
	golf_a5665 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 65])
	labels_2 = ['0-5 feet', '6-8 feet', '9-12 feet', '13-17 feet', '18-25 feet', '26-35 feet', '36-45 feet', '46-55 feet', ' > 55 feet']
	sizes_2 = [len(golf_a5), len(golf_a68), len(golf_a912), len(golf_a1317), len(golf_a1825), len(golf_a2635), len(golf_a3645), len(golf_a4660), len(golf_a65)]
	colors_2 = ['thistle', 'steelblue', 'cyan', 'lime', 'lightsalmon', 'blueviolet', 'indigo', 'peachpuff', 'firebrick']
	explode_2 = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)
	plt.pie(sizes_2, explode = explode_2, labels = labels_2, colors = colors_2, autopct = '%.2f', shadow = True)
	plt.title(b)
	#plt.show()
	

for x in num:
	a = golf_approach[x]
	b = approach_pie[x]
	#pie_2(a, b)

def golf_approachpercentage(a):
	golf_aoof = pd.DataFrame(a, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_shotrange = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_shotrange

golf_54pct = np.array([])
golf_49pct = np.array([])
golf_PWpct = np.array([])
golf_9ipct = np.array([])
golf_8ipct = np.array([])
golf_7ipct = np.array([])
golf_6ipct = np.array([])
golf_5ipct = np.array([])
golf_4ipct = np.array([])
golf_3Hpct = np.array([])
golf_3Wpct = np.array([])	
golf_ap = [golf_54pct, golf_49pct, golf_PWpct, golf_9ipct, golf_8ipct, golf_7ipct, golf_6ipct, golf_5ipct, golf_4ipct, golf_3Hpct, golf_3Wpct]

for x in num:
	a = golf_approach[x]
	golf_shotrange = golf_approachpercentage(a)
	golf_ap[x] = np.append(golf_ap[x], golf_shotrange)
	#print('text message', golf_ap[x])

golf_54pct = golf_ap[0]
golf_49pct = golf_ap[1]
golf_PWpct = golf_ap[2]
golf_9ipct = golf_ap[3]
golf_8ipct = golf_ap[4]
golf_7ipct = golf_ap[5]
golf_6ipct = golf_ap[6]
golf_5ipct = golf_ap[7]
golf_4ipct = golf_ap[8]
golf_3Hpct = golf_ap[9]
golf_3Wpct = golf_ap[10]

def approach_change(a):
	golf_approachimp = a
	golf_approachimprovementb = a * .9
	golf_approachimprovement = np.around(golf_approachimprovementb)
	golf_aoof = pd.DataFrame(golf_approachimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof)  
	golf_approachimprovement1 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_approachimprovement1

golf_54pct1 = np.array([])
golf_49pct1 = np.array([])
golf_PWpct1 = np.array([])
golf_9ipct1 = np.array([])
golf_8ipct1 = np.array([])
golf_7ipct1 = np.array([])
golf_6ipct1 = np.array([])
golf_5ipct1 = np.array([])
golf_4ipct1 = np.array([])
golf_3Hpct1 = np.array([])
golf_3Wpct1 = np.array([])	
	
golf_api1 = [golf_54pct1, golf_49pct1, golf_PWpct1, golf_9ipct1, golf_8ipct1, golf_7ipct1, golf_6ipct1, golf_5ipct1, golf_4ipct1, golf_3Hpct1, golf_3Wpct1]
	
for x in num:
	a = golf_approach[x]
	golf_approachimprovement1 = approach_change(a)
	golf_api1[x] = np.append(golf_api1[x], golf_approachimprovement1)
	
golf_54pct1 = golf_api1[0]
golf_49pct1 = golf_api1[1]
golf_PWpct1 = golf_api1[2]
golf_9ipct1 = golf_api1[3]
golf_8ipct1 = golf_api1[4]
golf_7ipct1 = golf_api1[5]
golf_6ipct1 = golf_api1[6]
golf_5ipct1 = golf_api1[7]
golf_4ipct1 = golf_api1[8]
golf_3Hpct1 = golf_api1[9]
golf_3Wpct1 = golf_api1[10]

def approach_change2(a):
	golf_approachimp = a
	golf_approachimprovementb = a * .8
	golf_approachimprovement = np.around(golf_approachimprovementb)
	golf_aoof = pd.DataFrame(golf_approachimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_approachimprovement2 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_approachimprovement2

golf_54pct2 = np.array([])
golf_49pct2 = np.array([])
golf_PWpct2 = np.array([])
golf_9ipct2 = np.array([])
golf_8ipct2 = np.array([])
golf_7ipct2 = np.array([])
golf_6ipct2 = np.array([])
golf_5ipct2 = np.array([])
golf_4ipct2 = np.array([])
golf_3Hpct2 = np.array([])
golf_3Wpct2 = np.array([])	
	
golf_api2 = [golf_54pct2, golf_49pct2, golf_PWpct2, golf_9ipct2, golf_8ipct2, golf_7ipct2, golf_6ipct2, golf_5ipct2, golf_4ipct2, golf_3Hpct2, golf_3Wpct2]
	
for x in num:
	a = golf_approach[x]
	golf_approachimprovement2 = approach_change2(a)
	golf_api2[x] = np.append(golf_api2[x], golf_approachimprovement2)
	
golf_54pct2 = golf_api2[0]
golf_49pct2 = golf_api2[1]
golf_PWpct2 = golf_api2[2]
golf_9ipct2 = golf_api2[3]
golf_8ipct2 = golf_api2[4]
golf_7ipct2 = golf_api2[5]
golf_6ipct2 = golf_api2[6]
golf_5ipct2 = golf_api2[7]
golf_4ipct2 = golf_api2[8]
golf_3Hpct2 = golf_api2[9]
golf_3Wpct2 = golf_api2[10]

def approach_change3(a):
	golf_approachimp = a
	golf_approachimprovementb = a * .7
	golf_approachimprovement = np.around(golf_approachimprovementb)
	golf_aoof = pd.DataFrame(golf_approachimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_approachimprovement3 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_approachimprovement3

golf_54pct3 = np.array([])
golf_49pct3 = np.array([])
golf_PWpct3 = np.array([])
golf_9ipct3 = np.array([])
golf_8ipct3 = np.array([])
golf_7ipct3 = np.array([])
golf_6ipct3 = np.array([])
golf_5ipct3 = np.array([])
golf_4ipct3 = np.array([])
golf_3Hpct3 = np.array([])
golf_3Wpct3 = np.array([])	
	
golf_api3 = [golf_54pct3, golf_49pct3, golf_PWpct3, golf_9ipct3, golf_8ipct3, golf_7ipct3, golf_6ipct3, golf_5ipct3, golf_4ipct3, golf_3Hpct3, golf_3Wpct3]
	
for x in num:
	a = golf_approach[x]
	golf_approachimprovement3 = approach_change3(a)
	golf_api3[x] = np.append(golf_api3[x], golf_approachimprovement3)
	
golf_54pct3 = golf_api3[0]
golf_49pct3 = golf_api3[1]
golf_PWpct3 = golf_api3[2]
golf_9ipct3 = golf_api3[3]
golf_8ipct3 = golf_api3[4]
golf_7ipct3 = golf_api3[5]
golf_6ipct3 = golf_api3[6]
golf_5ipct3 = golf_api3[7]
golf_4ipct3 = golf_api3[8]
golf_3Hpct3 = golf_api3[9]
golf_3Wpct3 = golf_api3[10]

def approach_change4(a):
	golf_approachimp = a
	golf_approachimprovementb = a * .6
	golf_approachimprovement = np.around(golf_approachimprovementb)
	golf_aoof = pd.DataFrame(golf_approachimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_approachimprovement4 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_approachimprovement4

golf_54pct4 = np.array([])
golf_49pct4 = np.array([])
golf_PWpct4 = np.array([])
golf_9ipct4 = np.array([])
golf_8ipct4 = np.array([])
golf_7ipct4 = np.array([])
golf_6ipct4 = np.array([])
golf_5ipct4 = np.array([])
golf_4ipct4 = np.array([])
golf_3Hpct4 = np.array([])
golf_3Wpct4 = np.array([])	
	
golf_api4 = [golf_54pct4, golf_49pct4, golf_PWpct4, golf_9ipct4, golf_8ipct4, golf_7ipct4, golf_6ipct4, golf_5ipct4, golf_4ipct4, golf_3Hpct4, golf_3Wpct4]
	
for x in num:
	a = golf_approach[x]
	golf_approachimprovement4 = approach_change4(a)
	golf_api4[x] = np.append(golf_api4[x], golf_approachimprovement4)
	
golf_54pct4 = golf_api4[0]
golf_49pct4 = golf_api4[1]
golf_PWpct4 = golf_api4[2]
golf_9ipct4 = golf_api4[3]
golf_8ipct4 = golf_api4[4]
golf_7ipct4 = golf_api4[5]
golf_6ipct4 = golf_api4[6]
golf_5ipct4 = golf_api4[7]
golf_4ipct4 = golf_api4[8]
golf_3Hpct4 = golf_api4[9]
golf_3Wpct4 = golf_api4[10]

golf_u1y = pd.DataFrame(golf.loc[golf.Unit_1 == 'Yard'])
golf_u2y = pd.DataFrame(golf.loc[golf.Unit_2 == 'Yard'])
golf_u3y = pd.DataFrame(golf.loc[golf.Unit_3 == 'Yard'])
golf_u4y = pd.DataFrame(golf.loc[golf.Unit_4 == 'Yard'])
golf_u5y = pd.DataFrame(golf.loc[golf.Unit_5 == 'Yard'])
golf_12y = golf_u1y.append(golf_u2y)
golf_123y = golf_12y.append(golf_u3y)
golf_1234y = golf_123y.append(golf_u4y)
golf_ydd = golf_1234y.append(golf_u5y)
golf_yd = golf_ydd.drop_duplicates()

def chipping_fairwaybins(a, b):
	golf_chippingbin1s1 = pd.DataFrame(golf_yd.loc[golf_yd.To_Hole1 >= a])
	golf_chippingbin2s1b = pd.DataFrame(golf_chippingbin1s1.loc[golf_chippingbin1s1.To_Hole1 < b])
	golf_chippingbin2s1 = pd.DataFrame(golf_chippingbin2s1b.loc[golf_chippingbin2s1b.Unit_1 == 'Yard'])
	golf_chippingbinfeets1 = pd.DataFrame(golf_chippingbin2s1.loc[golf_chippingbin2s1.Unit_2 == 'FT'])
	golf_chippingbinyards1 = pd.DataFrame(golf_chippingbin2s1.loc[golf_chippingbin2s1.Unit_2 == 'Yard'])
	feet_chippings1 = np.array(golf_chippingbinfeets1.To_Hole2)
	yard_chipping1 = np.array(golf_chippingbinyards1.To_Hole2)
	yard_chippings1 = yard_chipping1 * 3
	golf_chippings1 = np.append(yard_chippings1, feet_chippings1)
	golf_chippingbin1s2 = pd.DataFrame(golf_yd.loc[golf_yd.To_Hole2 >= a])
	golf_chippingbin2s2b = pd.DataFrame(golf_chippingbin1s2.loc[golf_chippingbin1s2.To_Hole2 < b])
	golf_chippingbin2s2 = pd.DataFrame(golf_chippingbin2s2b.loc[golf_chippingbin2s2b.Unit_2 == 'Yard'])
	golf_chippingbinfeets2 = pd.DataFrame(golf_chippingbin2s2.loc[golf_chippingbin2s2.Unit_3 == 'FT'])
	golf_chippingbinyards2 = pd.DataFrame(golf_chippingbin2s2.loc[golf_chippingbin2s2.Unit_3 == 'Yard'])
	feet_chippings2 = np.array(golf_chippingbinfeets2.To_Hole3)
	yard_chipping2 = np.array(golf_chippingbinyards2.To_Hole3)
	yard_chippings2 = yard_chipping2 * 3
	golf_chippings2 = np.append(yard_chippings2, feet_chippings2)
	golf_chippingbin1s3 = pd.DataFrame(golf_yd.loc[golf_yd.To_Hole3 >= a])
	golf_chippingbin2s3b = pd.DataFrame(golf_chippingbin1s3.loc[golf_chippingbin1s3.To_Hole3 < b])
	golf_chippingbin2s3 = pd.DataFrame(golf_chippingbin2s3b.loc[golf_chippingbin2s3b.Unit_3 == 'Yard'])
	golf_chippingbinfeets3 = pd.DataFrame(golf_chippingbin2s3.loc[golf_chippingbin2s3.Unit_4 == 'FT'])
	golf_chippingbinyards3 = pd.DataFrame(golf_chippingbin2s3.loc[golf_chippingbin2s3.Unit_4 == 'Yard'])
	feet_chippings3 = np.array(golf_chippingbinfeets3.To_Hole4)
	yard_chipping3 = np.array(golf_chippingbinyards3.To_Hole4)
	yard_chippings3 = yard_chipping3 * 3
	golf_chippings3 = np.append(yard_chippings3, feet_chippings3)
	golf_chippingbin1s4 = pd.DataFrame(golf_yd.loc[golf_yd.To_Hole4 >= a])
	golf_chippingbin2s4b = pd.DataFrame(golf_chippingbin1s4.loc[golf_chippingbin1s4.To_Hole4 < b])
	golf_chippingbin2s4 = pd.DataFrame(golf_chippingbin2s4b.loc[golf_chippingbin2s4b.Unit_4 == 'Yard'])
	golf_chippingbinfeets4 = pd.DataFrame(golf_chippingbin2s4.loc[golf_chippingbin2s4.Unit_5 == 'FT'])
	golf_chippingbinyards4 = pd.DataFrame(golf_chippingbin2s4.loc[golf_chippingbin2s4.Unit_5 == 'Yard'])
	feet_chippings4 = np.array(golf_chippingbinfeets4.To_Hole5)
	yard_chipping4 = np.array(golf_chippingbinyards4.To_Hole5)
	yard_chippings4 = yard_chipping4 * 3
	golf_chippings4 = np.append(yard_chippings4, feet_chippings4)
	golf_chippings12 = np.append(golf_chippings1, golf_chippings2)
	golf_chippings123 = np.append(golf_chippings12, golf_chippings3)
	golf_chipping = np.append(golf_chippings123, golf_chippings4)
	return golf_chipping

#golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p
chipping_num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
chipping_bin1 = (16, 17, 19, 21, 23, 25, 27, 30, 33, 36, 40, 44, 49, 54, 60)
chipping_bin2 = (17, 19, 21, 23, 25, 27, 30, 33, 36, 40, 44, 49, 54, 60, 66)
chipping_1617yf = np.array([])
chipping_1719yf = np.array([])
chipping_1921yf = np.array([])
chipping_2123yf = np.array([])
chipping_2325yf = np.array([])
chipping_2527yf = np.array([])
chipping_2730yf = np.array([])
chipping_3033yf = np.array([])
chipping_3336yf = np.array([])
chipping_3640yf = np.array([])
chipping_4044yf = np.array([])
chipping_4449yf = np.array([])
chipping_4954yf = np.array([])
chipping_5460yf = np.array([])
chipping_6066yf = np.array([])
chipping_pp = [chipping_1617yf, chipping_1719yf, chipping_1921yf, chipping_2123yf, chipping_2325yf, chipping_2527yf, chipping_2730yf, chipping_3033yf, chipping_3336yf, chipping_3640yf, chipping_4044yf, chipping_4449yf, chipping_4954yf, chipping_5460yf, chipping_6066yf]
for x in chipping_num:
	a = chipping_bin1[x]
	b = chipping_bin2[x]
	golf_chipping = chipping_fairwaybins(a, b)
	chipping_pp[x] = np.append(chipping_pp[x], golf_chipping)

chipping_1617yf = chipping_pp[0]
chipping_1719yf = chipping_pp[1]
chipping_1921yf = chipping_pp[2]
chipping_2123yf = chipping_pp[3]
chipping_2325yf = chipping_pp[4]
chipping_2527yf = chipping_pp[5]
chipping_2730yf = chipping_pp[6]
chipping_3033yf = chipping_pp[7]
chipping_3336yf = chipping_pp[8]
chipping_3640yf = chipping_pp[9]
chipping_4044yf = chipping_pp[10]
chipping_4449yf = chipping_pp[11]
chipping_4954yf = chipping_pp[12]
chipping_5459yf = chipping_pp[13]
chipping_6066yf = chipping_pp[14]

chipping_ranges = [chipping_1617yf, chipping_1719yf, chipping_1921yf, chipping_2123yf, chipping_2325yf, chipping_2527yf, chipping_2730yf, chipping_3033yf, chipping_3336yf, chipping_3640yf, chipping_4044yf, chipping_4449yf, chipping_4954yf, chipping_5460yf]
	
def chipping_percentage(a):
	golf_aoof = pd.DataFrame(a, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_chiprange = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p])
	return golf_chiprange

chipping_1617yp = np.array([])
chipping_1719yp = np.array([])
chipping_1921yp = np.array([])
chipping_2123yp = np.array([])
chipping_2325yp = np.array([])
chipping_2527yp = np.array([])
chipping_2730yp = np.array([])
chipping_3033yp = np.array([])
chipping_3336yp = np.array([])
chipping_3640yp = np.array([])
chipping_4044yp = np.array([])
chipping_4449yp = np.array([])
chipping_4954yp = np.array([])
chipping_5460yp = np.array([])
chipping_6066yp = np.array([])
chip_percentage = [chipping_1617yp, chipping_1719yp, chipping_1921yp, chipping_2123yp, chipping_2325yp, chipping_2527yp, chipping_2730yp, chipping_3033yp, chipping_3336yp, chipping_3640yp, chipping_4044yp, chipping_4449yp, chipping_4954yp, chipping_5460yp, chipping_6066yp]
chipping_numt = (0,1,2,3,4,5,6,7,8,9,10,11,12)
for x in chipping_numt:
	a = chipping_ranges[x]
	y = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(a, 'a')
	if len(a) == 0:
		chip_percentage[x] = np.append(chip_percentage[x], y)
	else:
		golf_chiprange = chipping_percentage(a)
		print('text message', golf_chiprange)
		chip_percentage[x] = np.append(chip_percentage[x], golf_chiprange)

chipping_1617yp = chip_percentage[0]
chipping_1719yp = chip_percentage[1]
chipping_1921yp = chip_percentage[2]
chipping_2123yp = chip_percentage[3]
chipping_2325yp = chip_percentage[4]
chipping_2527yp = chip_percentage[5]
chipping_2730yp = chip_percentage[6]
chipping_3033yp = chip_percentage[7]
chipping_3336yp = chip_percentage[8]
chipping_3640yp = chip_percentage[9]
chipping_4044yp = chip_percentage[10]
chipping_4449yp = chip_percentage[11]
chipping_4954yp = chip_percentage[12]
chipping_5460yp = chip_percentage[13]
chipping_6066yp = chip_percentage[14]

def chip_change(a):
	golf_chipimp = a
	golf_chipimprovementb = a * .9
	golf_chipimprovement = np.around(golf_chipimprovementb)
	golf_aoof = pd.DataFrame(golf_chipimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_chipimprovement1 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p])
	return golf_chipimprovement1
	
chipping_1617yp1 = np.array([])
chipping_1719yp1 = np.array([])
chipping_1921yp1 = np.array([])
chipping_2123yp1 = np.array([])
chipping_2325yp1 = np.array([])
chipping_2527yp1 = np.array([])
chipping_2730yp1 = np.array([])
chipping_3033yp1 = np.array([])
chipping_3336yp1 = np.array([])
chipping_3640yp1 = np.array([])
chipping_4044yp1 = np.array([])
chipping_4449yp1 = np.array([])
chipping_4954yp1 = np.array([])
chipping_5460yp1 = np.array([])
chipping_6066yp1 = np.array([])
chip_percentage1 = [chipping_1617yp1, chipping_1719yp1, chipping_1921yp1, chipping_2123yp1, chipping_2325yp1, chipping_2527yp1, chipping_2730yp1, chipping_3033yp1, chipping_3336yp1, chipping_3640yp1, chipping_4044yp1, chipping_4449yp1, chipping_4954yp1, chipping_5460yp1, chipping_6066yp1]

for x in chipping_numt:
	a = chipping_ranges[x]
	y = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(a, 'a')
	if len(a) == 0:
		chip_percentage1[x] = np.append(chip_percentage1[x], y)
	else:
		golf_chipimprovement1 = chip_change(a)
		chip_percentage1[x] = np.append(chip_percentage1[x], golf_chipimprovement1)

chipping_1617yp1 = chip_percentage1[0]
chipping_1719yp1 = chip_percentage1[1]
chipping_1921yp1 = chip_percentage1[2]
chipping_2123yp1 = chip_percentage1[3]
chipping_2325yp1 = chip_percentage1[4]
chipping_2527yp1 = chip_percentage1[5]
chipping_2730yp1 = chip_percentage1[6]
chipping_3033yp1 = chip_percentage1[7]
chipping_3336yp1 = chip_percentage1[8]
chipping_3640yp1 = chip_percentage1[9]
chipping_4044yp1 = chip_percentage1[10]
chipping_4449yp1 = chip_percentage1[11]
chipping_4954yp1 = chip_percentage1[12]
chipping_5460yp1 = chip_percentage1[13]
chipping_6066yp1 = chip_percentage1[14]

def chip_change2(a):
	golf_chipimp = a
	golf_chipimprovementb = a * .8
	golf_chipimprovement = np.around(golf_chipimprovementb)
	golf_aoof = pd.DataFrame(golf_chipimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_chipimprovement2 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p])
	return golf_chipimprovement2
	
chipping_1617yp2 = np.array([])
chipping_1719yp2 = np.array([])
chipping_1921yp2 = np.array([])
chipping_2123yp2 = np.array([])
chipping_2325yp2 = np.array([])
chipping_2527yp2 = np.array([])
chipping_2730yp2 = np.array([])
chipping_3033yp2 = np.array([])
chipping_3336yp2 = np.array([])
chipping_3640yp2 = np.array([])
chipping_4044yp2 = np.array([])
chipping_4449yp2 = np.array([])
chipping_4954yp2 = np.array([])
chipping_5460yp2 = np.array([])
chipping_6066yp2 = np.array([])
chip_percentage2 = [chipping_1617yp2, chipping_1719yp2, chipping_1921yp2, chipping_2123yp2, chipping_2325yp2, chipping_2527yp2, chipping_2730yp2, chipping_3033yp2, chipping_3336yp2, chipping_3640yp2, chipping_4044yp2, chipping_4449yp2, chipping_4954yp2, chipping_5460yp2, chipping_6066yp2]

for x in chipping_numt:
	a = chipping_ranges[x]
	y = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(a, 'a')
	if len(a) == 0:
		chip_percentage2[x] = np.append(chip_percentage2[x], y)
	else:
		golf_chipimprovement2 = chip_change2(a)
		chip_percentage2[x] = np.append(chip_percentage2[x], golf_chipimprovement2)

chipping_1617yp2 = chip_percentage2[0]
chipping_1719yp2 = chip_percentage2[1]
chipping_1921yp2 = chip_percentage2[2]
chipping_2123yp2 = chip_percentage2[3]
chipping_2325yp2 = chip_percentage2[4]
chipping_2527yp2 = chip_percentage2[5]
chipping_2730yp2 = chip_percentage2[6]
chipping_3033yp2 = chip_percentage2[7]
chipping_3336yp2 = chip_percentage2[8]
chipping_3640yp2 = chip_percentage2[9]
chipping_4044yp2 = chip_percentage2[10]
chipping_4449yp2 = chip_percentage2[11]
chipping_4954yp2 = chip_percentage2[12]
chipping_5460yp2 = chip_percentage2[13]
chipping_6066yp2 = chip_percentage2[14]

def chip_change3(a):
	golf_chipimp = a
	golf_chipimprovementb = a * .7
	golf_chipimprovement = np.around(golf_chipimprovementb)
	golf_aoof = pd.DataFrame(golf_chipimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_chipimprovement3 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_chipimprovement3
	
chipping_1617yp3 = np.array([])
chipping_1719yp3 = np.array([])
chipping_1921yp3 = np.array([])
chipping_2123yp3 = np.array([])
chipping_2325yp3 = np.array([])
chipping_2527yp3 = np.array([])
chipping_2730yp3 = np.array([])
chipping_3033yp3 = np.array([])
chipping_3336yp3 = np.array([])
chipping_3640yp3 = np.array([])
chipping_4044yp3 = np.array([])
chipping_4449yp3 = np.array([])
chipping_4954yp3 = np.array([])
chipping_5460yp3 = np.array([])
chipping_6066yp3 = np.array([])
chip_percentage3 = [chipping_1617yp3, chipping_1719yp3, chipping_1921yp3, chipping_2123yp3, chipping_2325yp3, chipping_2527yp3, chipping_2730yp3, chipping_3033yp3, chipping_3336yp3, chipping_3640yp3, chipping_4044yp3, chipping_4449yp3, chipping_4954yp3, chipping_5460yp3, chipping_6066yp3]

for x in chipping_numt:
	a = chipping_ranges[x]
	y = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(a, 'a')
	if len(a) == 0:
		chip_percentage3[x] = np.append(chip_percentage3[x], y)
	else:
		golf_chipimprovement3 = chip_change3(a)
		chip_percentage3[x] = np.append(chip_percentage3[x], golf_chipimprovement3)

chipping_1617yp3 = chip_percentage3[0]
chipping_1719yp3 = chip_percentage3[1]
chipping_1921yp3 = chip_percentage3[2]
chipping_2123yp3 = chip_percentage3[3]
chipping_2325yp3 = chip_percentage3[4]
chipping_2527yp3 = chip_percentage3[5]
chipping_2730yp3 = chip_percentage3[6]
chipping_3033yp3 = chip_percentage3[7]
chipping_3336yp3 = chip_percentage3[8]
chipping_3640yp3 = chip_percentage3[9]
chipping_4044yp3 = chip_percentage3[10]
chipping_4449yp3 = chip_percentage3[11]
chipping_4954yp3 = chip_percentage3[12]
chipping_5460yp3 = chip_percentage3[13]
chipping_6066yp3 = chip_percentage3[14]

def chip_change4(a):
	golf_chipimp = a
	golf_chipimprovementb = a * .6
	golf_chipimprovement = np.around(golf_chipimprovementb)
	golf_aoof = pd.DataFrame(golf_chipimprovement, columns = ['proximity'])
	golf_a1 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 1])
	golf_a2 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 2])
	golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 3])
	golf_a4 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 4])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 5])
	golf_a6 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 6])
	golf_a7 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 7])
	golf_a8 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 8])
	golf_a9 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 9])
	golf_a10 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 10])
	golf_a11 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 11])
	golf_a12 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 12])
	golf_a13 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 13])
	golf_a14 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 14])
	golf_a15 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity == 15])
	golf_a17 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 17])
	golf_a1617 = pd.DataFrame(golf_a17.loc[golf_a17.proximity > 15])
	golf_a19 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 19])
	golf_a1819 = pd.DataFrame(golf_a19.loc[golf_a19.proximity > 17])
	golf_a21 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 21])
	golf_a2021 = pd.DataFrame(golf_a21.loc[golf_a21.proximity > 19])
	golf_a23 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 23])
	golf_a2223 = pd.DataFrame(golf_a23.loc[golf_a23.proximity > 21])
	golf_a25 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 25])
	golf_a2425 = pd.DataFrame(golf_a25.loc[golf_a25.proximity > 23])
	golf_a28 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 28])
	golf_a2628 = pd.DataFrame(golf_a28.loc[golf_a28.proximity > 25])
	golf_a31 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 31])
	golf_a2931 = pd.DataFrame(golf_a31.loc[golf_a31.proximity > 28])
	golf_a34 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 34])
	golf_a3234 = pd.DataFrame(golf_a34.loc[golf_a34.proximity > 31])
	golf_a38 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 38])
	golf_a3538 = pd.DataFrame(golf_a38.loc[golf_a38.proximity > 34])
	golf_a42 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 42])
	golf_a3942 = pd.DataFrame(golf_a42.loc[golf_a42.proximity > 38])
	golf_a46 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 47])
	golf_a4347 = pd.DataFrame(golf_a46.loc[golf_a46.proximity > 42])
	golf_a51 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 50])
	golf_a4850 = pd.DataFrame(golf_a51.loc[golf_a51.proximity > 47])
	golf_a56 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 56])
	golf_a5156 = pd.DataFrame(golf_a56.loc[golf_a56.proximity > 50])
	golf_a62 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 62])
	golf_a5762 = pd.DataFrame(golf_a62.loc[golf_a62.proximity > 56])
	golf_a68 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 68])
	golf_a6368 = pd.DataFrame(golf_a68.loc[golf_a68.proximity > 62])
	golf_a74 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 74])
	golf_a6974 = pd.DataFrame(golf_a74.loc[golf_a74.proximity > 68])
	golf_a80 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 80])
	golf_a7580 = pd.DataFrame(golf_a80.loc[golf_a80.proximity > 74])
	golf_a89 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 89])
	golf_a8189 = pd.DataFrame(golf_a89.loc[golf_a89.proximity > 80])
	golf_a98 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 98])
	golf_a9098 = pd.DataFrame(golf_a98.loc[golf_a98.proximity > 89])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 107])
	golf_a99107 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 98])
	golf_a109 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 119])
	golf_a108119 = pd.DataFrame(golf_a109.loc[golf_a109.proximity > 107])
	golf_a131 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 131])
	golf_a120131 = pd.DataFrame(golf_a131.loc[golf_a131.proximity > 119])
	golf_a146 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 146])
	golf_a132146 = pd.DataFrame(golf_a146.loc[golf_a146.proximity > 131])
	golf_a107 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 161])
	golf_a147161 = pd.DataFrame(golf_a107.loc[golf_a107.proximity > 146])
	golf_a179 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 179])
	golf_a162179 = pd.DataFrame(golf_a179.loc[golf_a179.proximity > 161])
	golf_a197 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 197])
	golf_a180197 = pd.DataFrame(golf_a197.loc[golf_a197.proximity > 179])
	golf_a1p = len(golf_a1)/len(golf_aoof)
	golf_a2p = len(golf_a2)/len(golf_aoof)
	golf_a3p = len(golf_a3)/len(golf_aoof)
	golf_a4p = len(golf_a4)/len(golf_aoof)
	golf_a5p = len(golf_a5)/len(golf_aoof)
	golf_a6p = len(golf_a6)/len(golf_aoof)
	golf_a7p = len(golf_a7)/len(golf_aoof) 
	golf_a8p = len(golf_a8)/len(golf_aoof)
	golf_a9p = len(golf_a9)/len(golf_aoof) 
	golf_a10p = len(golf_a10)/len(golf_aoof) 
	golf_a11p = len(golf_a11)/len(golf_aoof) 
	golf_a12p = len(golf_a12)/len(golf_aoof) 
	golf_a13p = len(golf_a13)/len(golf_aoof)
	golf_a14p = len(golf_a14)/len(golf_aoof)
	golf_a15p = len(golf_a15)/len(golf_aoof)
	golf_a1617p = len(golf_a1617)/len(golf_aoof)
	golf_a1819p = len(golf_a1819)/len(golf_aoof)
	golf_a2021p = len(golf_a2021)/len(golf_aoof)
	golf_a2223p = len(golf_a2223)/len(golf_aoof)
	golf_a2425p = len(golf_a2425)/len(golf_aoof)
	golf_a2628p = len(golf_a2628)/len(golf_aoof)
	golf_a2931p = len(golf_a2931)/len(golf_aoof) 
	golf_a3234p = len(golf_a3234)/len(golf_aoof)
	golf_a3538p = len(golf_a3538)/len(golf_aoof) 
	golf_a3942p = len(golf_a3942)/len(golf_aoof) 
	golf_a4347p = len(golf_a4347)/len(golf_aoof) 
	golf_a4850p = len(golf_a4850)/len(golf_aoof) 
	golf_a5156p = len(golf_a5156)/len(golf_aoof)
	golf_a5762p = len(golf_a5762)/len(golf_aoof)
	golf_a6368p = len(golf_a6368)/len(golf_aoof)
	golf_a6974p = len(golf_a6974)/len(golf_aoof)
	golf_a7580p = len(golf_a7580)/len(golf_aoof)
	golf_a8189p = len(golf_a8189)/len(golf_aoof)
	golf_a9098p = len(golf_a9098)/len(golf_aoof)
	golf_a99107p = len(golf_a99107)/len(golf_aoof)
	golf_a108119p = len(golf_a108119)/len(golf_aoof)
	golf_a120131p = len(golf_a120131)/len(golf_aoof) 
	golf_a132146p = len(golf_a132146)/len(golf_aoof)
	golf_a147161p = len(golf_a147161)/len(golf_aoof) 
	golf_a162179p = len(golf_a162179)/len(golf_aoof) 
	golf_a180197p = len(golf_a180197)/len(golf_aoof) 
	golf_chipimprovement4 = np.array([golf_a1p, golf_a2p, golf_a3p, golf_a4p, golf_a5p, golf_a6p, golf_a7p, golf_a8p, golf_a9p, golf_a10p, golf_a11p, golf_a12p, golf_a13p, golf_a14p, golf_a15p, golf_a1617p, golf_a1819p, golf_a2021p, golf_a2223p, golf_a2425p, golf_a2628p, golf_a2931p, golf_a3234p, golf_a3538p, golf_a3942p, golf_a4347p, golf_a4850p, golf_a5156p, golf_a5762p, golf_a6368p, golf_a6974p, golf_a7580p, golf_a8189p, golf_a9098p, golf_a99107p, golf_a108119p, golf_a120131p, golf_a132146p, golf_a147161p, golf_a162179p, golf_a180197p])
	return golf_chipimprovement4
	
chipping_1617yp4 = np.array([])
chipping_1719yp4 = np.array([])
chipping_1921yp4 = np.array([])
chipping_2123yp4 = np.array([])
chipping_2325yp4 = np.array([])
chipping_2527yp4 = np.array([])
chipping_2730yp4 = np.array([])
chipping_3033yp4 = np.array([])
chipping_3336yp4 = np.array([])
chipping_3640yp4 = np.array([])
chipping_4044yp4 = np.array([])
chipping_4449yp4 = np.array([])
chipping_4954yp4 = np.array([])
chipping_5460yp4 = np.array([])
chipping_6066yp4 = np.array([])
chip_percentage4 = [chipping_1617yp4, chipping_1719yp4, chipping_1921yp4, chipping_2123yp4, chipping_2325yp4, chipping_2527yp4, chipping_2730yp4, chipping_3033yp4, chipping_3336yp4, chipping_3640yp4, chipping_4044yp4, chipping_4449yp4, chipping_4954yp4, chipping_5460yp4, chipping_6066yp4]

for x in chipping_numt:
	a = chipping_ranges[x]
	y = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(a, 'a')
	if len(a) == 0:
		chip_percentage4[x] = np.append(chip_percentage4[x], y)
	else:
		golf_chipimprovement4 = chip_change4(a)
		chip_percentage4[x] = np.append(chip_percentage4[x], golf_chipimprovement4)

chipping_1617yp4 = chip_percentage4[0]
chipping_1719yp4 = chip_percentage4[1]
chipping_1921yp4 = chip_percentage4[2]
chipping_2123yp4 = chip_percentage4[3]
chipping_2325yp4 = chip_percentage4[4]
chipping_2527yp4 = chip_percentage4[5]
chipping_2730yp4 = chip_percentage4[6]
chipping_3033yp4 = chip_percentage4[7]
chipping_3336yp4 = chip_percentage4[8]
chipping_3640yp4 = chip_percentage4[9]
chipping_4044yp4 = chip_percentage4[10]
chipping_4449yp4 = chip_percentage4[11]
chipping_4954yp4 = chip_percentage4[12]
chipping_5460yp4 = chip_percentage4[13]
chipping_6066yp4 = chip_percentage4[14]


random_proximity5i = random.choice(golf_5io)
print('random proximity:', random_proximity5i)
#if random_proximity5i <= 3:	
#golf_ft03, golf_ft45, golf_ft68, golf_ft912, golf_ft1317, golf_ft1825, golf_ft2635, golf_ft3645, golf_ft4655, golf_ft5665
#chipping_1520yp, chipping_2025yp, chipping_2530yp, chipping_3035yp, chipping_3540yp
green_scoreb = golf_5ipct[0] * golf_ft03 * 100 + golf_5ipct[1] * golf_ft45 * 100 + golf_5ipct[2] * golf_ft68 * 100 + golf_5ipct[3] * golf_ft912 * 100 + golf_5ipct[4] * golf_ft1317 * 100 + golf_5ipct[5] * golf_ft1825 * 100 + golf_5ipct[6] * golf_ft2635 * 100 + golf_5ipct[7] * golf_ft3645 * 100
green_score = np.append(green_scoreb, 0)
offgreen_score1519 = golf_5ipct[8] * chipping_1520yp[0] * golf_ft03 * 100 + golf_5ipct[8] * chipping_1520yp[1] * golf_ft45 * 100 + golf_5ipct[8] * chipping_1520yp[2] * golf_ft68 * 100 + golf_5ipct[8] * chipping_1520yp[3] * golf_ft912 * 100 + golf_5ipct[8] * chipping_1520yp[4] * golf_ft1317 * 100 + golf_5ipct[8] * chipping_1520yp[5] * golf_ft1825 * 100 + golf_5ipct[8] * chipping_1520yp[6] * golf_ft2635 * 100 + golf_5ipct[8] * chipping_1520yp[7] * golf_ft3645 * 100
print(offgreen_score1519, '1519')
offgreen_score2024 = golf_5ipct[9] * chipping_2025yp[0] * golf_ft03 * 100 + golf_5ipct[9] * chipping_2025yp[1] * golf_ft45 * 100 + golf_5ipct[9] * chipping_2025yp[2] * golf_ft68 * 100 + golf_5ipct[9] * chipping_2025yp[3] * golf_ft912 * 100 + golf_5ipct[9] * chipping_2025yp[4] * golf_ft1317 * 100 + golf_5ipct[9] * chipping_2025yp[5] * golf_ft1825 * 100 + golf_5ipct[9] * chipping_2025yp[6] * golf_ft2635 * 100 + golf_5ipct[9] * chipping_2025yp[7] * golf_ft3645 * 100
print(offgreen_score2024, '2024')
offgreen_score2529 = golf_5ipct[10] * chipping_2530yp[0] * golf_ft03 * 100 + golf_5ipct[10] * chipping_2530yp[1] * golf_ft45 * 100 + golf_5ipct[10] * chipping_2530yp[2] * golf_ft68 * 100 + golf_5ipct[10] * chipping_2530yp[3] * golf_ft912 * 100 + golf_5ipct[10] * chipping_2530yp[4] * golf_ft1317 * 100 + golf_5ipct[10] * chipping_2530yp[5] * golf_ft1825 * 100 + golf_5ipct[10] * chipping_2530yp[6] * golf_ft2635 * 100 + golf_5ipct[10] * chipping_2530yp[7] * golf_ft3645 * 100
print(offgreen_score2529, '2529')
offgreen_score3034 = golf_5ipct[11] * chipping_3035yp[0] * golf_ft03 * 100 + golf_5ipct[11] * chipping_3035yp[1] * golf_ft45 * 100 + golf_5ipct[11] * chipping_3035yp[2] * golf_ft68 * 100 + golf_5ipct[11] * chipping_3035yp[3] * golf_ft912 * 100 + golf_5ipct[11] * chipping_3035yp[4] * golf_ft1317 * 100 + golf_5ipct[11] * chipping_3035yp[5] * golf_ft1825 * 100 + golf_5ipct[11] * chipping_3035yp[6] * golf_ft2635 * 100 + golf_5ipct[11] * chipping_3035yp[7] * golf_ft3645 * 100
print(offgreen_score3034, '3034')
offgreen_score3539 = golf_5ipct[12] * chipping_3540yp[0] * golf_ft03 * 100 + golf_5ipct[12] * chipping_3540yp[1] * golf_ft45 * 100 + golf_5ipct[12] * chipping_3540yp[2] * golf_ft68 * 100 + golf_5ipct[12] * chipping_3540yp[3] * golf_ft912 * 100 + golf_5ipct[12] * chipping_3540yp[4] * golf_ft1317 * 100 + golf_5ipct[12] * chipping_3540yp[5] * golf_ft1825 * 100 + golf_5ipct[12] * chipping_3540yp[6] * golf_ft2635 * 100 + golf_5ipct[12] * chipping_3540yp[7] * golf_ft3645 * 100
print(offgreen_score3539, '3539')
offgreen_score4049 = golf_5ipct[13] * chipping_4050yp[0] * golf_ft03 * 100 + golf_5ipct[13] * chipping_4050yp[1] * golf_ft45 * 100 + golf_5ipct[13] * chipping_4050yp[2] * golf_ft68 * 100 + golf_5ipct[13] * chipping_4050yp[3] * golf_ft912 * 100 + golf_5ipct[13] * chipping_4050yp[4] * golf_ft1317 * 100 + golf_5ipct[13] * chipping_4050yp[5] * golf_ft1825 * 100 + golf_5ipct[13] * chipping_4050yp[6] * golf_ft2635 * 100 + golf_5ipct[13] * chipping_4050yp[7] * golf_ft3645 * 100
print(offgreen_score4049, '4049')
offgreen_score5059 = golf_5ipct[14] * chipping_5060yp[0] * golf_ft03 * 100 + golf_5ipct[14] * chipping_5060yp[1] * golf_ft45 * 100 + golf_5ipct[14] * chipping_5060yp[2] * golf_ft68 * 100 + golf_5ipct[14] * chipping_5060yp[3] * golf_ft912 * 100 + golf_5ipct[14] * chipping_5060yp[4] * golf_ft1317 * 100 + golf_5ipct[14] * chipping_5060yp[5] * golf_ft1825 * 100 + golf_5ipct[14] * chipping_5060yp[6] * golf_ft2635 * 100 + golf_5ipct[14] * chipping_5060yp[7] * golf_ft3645 * 100
print(offgreen_score5059, '5059' )
offgreen_scoreb = offgreen_score1519 + offgreen_score2024 + offgreen_score2529 + offgreen_score3034 + offgreen_score3539 + offgreen_score4049 + offgreen_score5059
offgreen_score = np.append(0, offgreen_scoreb)
cool_score = green_score + offgreen_score
print(cool_score)
print(np.sum(cool_score))

golfaverage_array5i = np.array([])

golf_ft03 = np.array([])
golf_ft45 = np.array([])
golf_ft68 = np.array([])
golf_ft912 = np.array([])
golf_ft1317 = np.array([])
golf_ft1825 = np.array([])
golf_ft2635 = np.array([])
golf_ft3645 = np.array([])
golf_ft4655 = np.array([])
golf_ft5665 = np.array([])
putt_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
golf_puttbins = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28, 31, 34, 38, 42, 47)
golf_puttbins2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 21, 23, 25, 28, 31, 34, 38, 42)
def putting_distances(f, a, b):
	golf_putt1 = pd.DataFrame(f.loc[f.To_Hole1 <= a])
	golf_puttd1 = pd.DataFrame(golf_putt1.loc[golf_putt1.To_Hole1 > b])
	golf_puttdistance1 = pd.DataFrame(golf_puttd1.loc[golf_puttd1.Unit_1 == 'FT'])
	golf_puttdistance1m = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_2 == 'Made'])
	golf_puttdistance1mi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_3 == 'Made'])
	golf_puttdistance1mimi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_4 == 'Made'])
	golf_puttdistance1mimimi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_5 == 'Made'])
	golf_putt2 = pd.DataFrame(f.loc[f.To_Hole2 <= a])
	golf_puttd2 = pd.DataFrame(golf_putt2.loc[golf_putt2.To_Hole2 > b])
	golf_puttdistance2 = pd.DataFrame(golf_puttd2.loc[golf_puttd2.Unit_2 == 'FT'])
	golf_puttdistance2m = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_3 == 'Made'])
	golf_puttdistance2mi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_4 == 'Made'])
	golf_puttdistance2mimi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_5 == 'Made'])
	golf_puttdistance2mimimi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_6 == 'Made'])
	golf_putt3 = pd.DataFrame(f.loc[f.To_Hole3 <= a])
	golf_puttd3 = pd.DataFrame(golf_putt3.loc[golf_putt3.To_Hole3 > b])
	golf_puttdistance3 = pd.DataFrame(golf_puttd3.loc[golf_puttd3.Unit_3 == 'FT'])
	golf_puttdistance3m = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_4 == 'Made'])
	golf_puttdistance3mi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_5 == 'Made'])
	golf_puttdistance3mimi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_6 == 'Made'])
	golf_puttdistance3mimimi = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_7 == 'Made'])
	golf_putt4 = pd.DataFrame(f.loc[f.To_Hole4 <= a])
	golf_puttd4 = pd.DataFrame(golf_putt4.loc[golf_putt4.To_Hole4 > b])
	golf_puttdistance4 = pd.DataFrame(golf_puttd4.loc[golf_puttd4.Unit_4 == 'FT'])
	golf_puttdistance4m = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_5 == 'Made'])
	golf_puttdistance4mi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_6 == 'Made'])
	golf_puttdistance4mimi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_7 == 'Made'])
	golf_puttdistance4mimimi = pd.DataFrame(golf_puttdistance4.loc[golf_puttdistance4.Result_8 == 'Made'])
	golf_putt5 = pd.DataFrame(f.loc[f.To_Hole5 <= a])
	golf_puttd5 = pd.DataFrame(golf_putt5.loc[golf_putt5.To_Hole5 > b])
	golf_puttdistance5 = pd.DataFrame(golf_puttd5.loc[golf_puttd5.Unit_5 == 'FT'])
	golf_puttdistance5m = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_6 == 'Made'])
	golf_puttdistance5mi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_7 == 'Made'])
	golf_puttdistance5mimi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_8 == 'Made'])
	golf_puttdistance5mimimi = pd.DataFrame(golf_puttdistance5.loc[golf_puttdistance5.Result_9 == 'Made'])
	golf_putt6 = pd.DataFrame(f.loc[f.To_Hole6 <= a])
	golf_puttd6 = pd.DataFrame(golf_putt6.loc[golf_putt6.To_Hole6 > b])
	golf_puttdistance6 = pd.DataFrame(golf_puttd6.loc[golf_puttd6.Unit_6 == 'FT'])
	golf_puttdistance6m = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_7 == 'Made'])
	golf_puttdistance6mi = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_8 == 'Made'])
	golf_puttdistance6mimi = pd.DataFrame(golf_puttdistance6.loc[golf_puttdistance6.Result_9 == 'Made'])
	golf_putt7 = pd.DataFrame(f.loc[f.To_Hole7 <= a])
	golf_puttd7 = pd.DataFrame(golf_putt7.loc[golf_putt7.To_Hole7 > b])
	golf_puttdistance7 = pd.DataFrame(golf_puttd7.loc[golf_puttd7.Unit_7 == 'FT'])
	golf_puttdistance7m = pd.DataFrame(golf_puttdistance7.loc[golf_puttdistance7.Result_8 == 'Made'])
	golf_puttdistance7mi = pd.DataFrame(golf_puttdistance7.loc[golf_puttdistance7.Result_9 == 'Made'])
	golf_puttlength = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) + len(golf_puttdistance6) + len(golf_puttdistance7)
	print(golf_puttlength, 'puttlength')
	golf_puttlength2 = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) + len(golf_puttdistance6) 
	golf_puttlength3 = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) + len(golf_puttdistance4) + len(golf_puttdistance5) 
	golf_1putt = len(golf_puttdistance1m) + len(golf_puttdistance2m) + len(golf_puttdistance3m) + len(golf_puttdistance4m) + len(golf_puttdistance5m) + len(golf_puttdistance6m) + len(golf_puttdistance7m)
	golf_2putt = len(golf_puttdistance1mi) + len(golf_puttdistance2mi) + len(golf_puttdistance3mi) + len(golf_puttdistance4mi) + len(golf_puttdistance5mi) + len(golf_puttdistance6mi) + len(golf_puttdistance7mi)
	golf_3putt = len(golf_puttdistance1mimi) + len(golf_puttdistance2mimi) + len(golf_puttdistance3mimi) + len(golf_puttdistance4mimi) + len(golf_puttdistance5mimi) + len(golf_puttdistance6mimi)
	golf_4putt = len(golf_puttdistance1mimimi) + len(golf_puttdistance2mimimi) + len(golf_puttdistance3mimimi) + len(golf_puttdistance4mimimi) + len(golf_puttdistance5mimimi)
	golf_1puttp = golf_1putt/golf_puttlength
	golf_2puttp = golf_2putt/golf_puttlength 
	golf_3puttp = golf_3putt/golf_puttlength
	golf_4puttp = golf_4putt/golf_puttlength
	#print('1 putt percentage:', golf_1putt/golf_puttlength)
	#print('2 putt percentage:', golf_2putt/golf_puttlength)
	#print('3 putt percentage:', golf_3putt/golf_puttlength)
	golf_puttrange = np.array([golf_1puttp, golf_2puttp, golf_3puttp, golf_4puttp])
	return golf_puttrange
	
golf_ft1 = np.array([])
golf_ft2 = np.array([])
golf_ft3 = np.array([])
golf_ft4 = np.array([])
golf_ft5 = np.array([])
golf_ft6 = np.array([])
golf_ft7 = np.array([])
golf_ft8 = np.array([])
golf_ft9 = np.array([])
golf_ft10 = np.array([])
golf_ft11 = np.array([])
golf_ft12 = np.array([])
golf_ft13 = np.array([])
golf_ft14 = np.array([])
golf_ft15 = np.array([])
golf_ft1617 = np.array([])
golf_ft1819 = np.array([])
golf_ft2021 = np.array([])
golf_ft2223 = np.array([])
golf_ft2425 = np.array([])	
golf_ft2628 = np.array([])
golf_ft2931 = np.array([])
golf_ft3234 = np.array([])
golf_ft3538 = np.array([])
golf_ft3942 = np.array([])
golf_ft4347 = np.array([])
	
	
golf_pp = [golf_ft1, golf_ft2, golf_ft3, golf_ft4, golf_ft5, golf_ft6, golf_ft7, golf_ft8, golf_ft9, golf_ft10, golf_ft11, golf_ft12, golf_ft13, golf_ft14, golf_ft15, golf_ft1617, golf_ft1819, golf_ft2021, golf_ft2223, golf_ft2425, golf_ft2628, golf_ft2931, golf_ft3234, golf_ft3538, golf_ft3942, golf_ft4347]
for x in putt_num:
	f = golf_ft
	a = golf_puttbins[x]
	b = golf_puttbins2[x]
	golf_puttrange = putting_distances(f, a, b)
	golf_pp[x] = np.append(golf_pp[x], golf_puttrange)

golf_ft1 = golf_pp[0]
golf_ft2 = golf_pp[1]
golf_ft3 = golf_pp[2]
golf_ft4 = golf_pp[3]
golf_ft5 = golf_pp[4]
golf_ft6 = golf_pp[5]
golf_ft7 = golf_pp[6]
golf_ft8 = golf_pp[7]
golf_ft9 = golf_pp[8]
golf_ft10 = golf_pp[9]
golf_ft11 = golf_pp[10]
golf_ft12 = golf_pp[11]
golf_ft13 = golf_pp[12]
golf_ft14 = golf_pp[13]
golf_ft15 = golf_pp[14]
golf_ft1617 = golf_pp[15]
golf_ft1819 = golf_pp[16]
golf_ft2021 = golf_pp[17]
golf_ft2223 = golf_pp[18]
golf_ft2425 = golf_pp[19]
golf_ft2628 = golf_pp[20]
golf_ft2931 = golf_pp[21]
golf_ft3234 = golf_pp[22]
golf_ft3538 = golf_pp[23]
golf_ft3942 = golf_pp[24]
golf_ft4347 = golf_pp[25]

def score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z, b2, c2, d2, e2, f2, g2, h2, i2, k2, l2, m2, n2, o2, p2, q2, r2):
	green_score1 = a[0] * i * 100 
	green_score2 = a[1] * j * 100
	green_score3 = a[2] * k * 100
	green_score4 = a[3] * l * 100
	green_score5 = a[4] * m * 100
	green_score6 = a[5] * n * 100
	green_score7 = a[6] * o * 100
	green_score8 = a[7] * p * 100
	green_score9 = a[8] * q * 100
	green_score10 = a[9] * r * 100
	green_score11 = a[10] * s * 100
	green_score12 = a[11] * t * 100
	green_score13 = a[12] * u * 100
	green_score14 = a[13] * v * 100
	green_score15 = a[14] * w * 100
	green_score16 = a[15] * x * 100
	green_score17 = a[16] * i2 * 100
	green_score18 = a[17] * j2 * 100
	green_score19 = a[18] * k2 * 100
	green_score20 = a[19] * l2 * 100
	green_score21 = a[20] * m2 * 100
	green_score22 = a[21] * n2 * 100
	green_score23 = a[22] * o2 * 100
	green_score24 = a[23] * p2 * 100
	green_score25 = a[24] * q2 * 100
	green_score26 = a[25] * r2 * 100
	green_score = np.append(green_scoreb, 0)
	offgreen_score1617 = a[26] * b[0] * i * 100 + a[26] * b[1] * j * 100 + a[26] * b[2] * k * 100 + a[26] * b[3] * l * 100 + a[26] * b[4] * m * 100 + a[26] * b[5] * n * 100 + a[26] * b[6] * o * 100 + a[26] * b[7] * p * 100 + a[26] * b[8] * q * 100 + a[26] * b[9] * r * 100 + a[26] * b[10] * s * 100 + a[26] * b[11] * t * 100 + a[26] * b[12] * u * 100 + a[26] * b[13] * v * 100 + a[26] * b[14] * w * 100 + a[26] * b[15] * x * 100 + a[26] * b[16] * i2 * 100 + a[26] * b[17] * j2 * 100 + a[26] * b[18] * k2 * 100 + a[26] * b[19] * l2 * 100 + a[26] * b[20] * m2 * 100 + a[26] * b[21] * n2 * 100 + a[26] * b[22] * o2 * 100 + a[26] * b[23] * p2 * 100 + a[26] * b[24] * q2 * 100 + a[26] * b[25] * r2 * 100
	offgreen_score1719 = a[27] * c[0] * i * 100 + a[27] * c[1] * j * 100 + a[27] * c[2] * k * 100 + a[27] * c[3] * l * 100 + a[27] * c[4] * m * 100 + a[27] * c[5] * n * 100 + a[27] * c[6] * o * 100 + a[27] * c[7] * p * 100 + a[27] * c[8] * q * 100 + a[27] * c[9] * r * 100 + a[27] * c[10] * s * 100 + a[27] * c[11] * t * 100 + a[27] * c[12] * u * 100 + a[27] * c[13] * v * 100 + a[27] * c[14] * w * 100 + a[27] * c[15] * x * 100 + a[27] * c[16] * i2 * 100 + a[27] * c[17] * j2 * 100 + a[27] * c[18] * k2 * 100 + a[27] * c[19] * l2 * 100 + a[27] * c[20] * m2 * 100 + a[27] * c[21] * n2 * 100 + a[27] * c[22] * o2 * 100 + a[27] * c[23] * p2 * 100 + a[27] * c[24] * q2 * 100 + a[27] * c[25] * r2 * 100
	offgreen_score1921 = a[28] * d[0] * i * 100 + a[28] * d[1] * j * 100 + a[28] * d[2] * k * 100 + a[28] * d[3] * l * 100 + a[28] * d[4] * m * 100 + a[28] * d[5] * n * 100 + a[28] * d[6] * o * 100 + a[28] * d[7] * p * 100 + a[28] * d[8] * q * 100 + a[28] * d[9] * r * 100 + a[28] * d[10] * s * 100 + a[28] * d[11] * t * 100 + a[28] * d[12] * u * 100 + a[28] * d[13] * v * 100 + a[28] * d[14] * w * 100 + a[28] * d[15] * x * 100 + a[28] * d[16] * i2 * 100 + a[28] * d[17] * j2 * 100 + a[28] * d[18] * k2 * 100 + a[28] * d[19] * l2 * 100 + a[28] * d[20] * m2 * 100 + a[28] * d[21] * n2 * 100 + a[28] * d[22] * o2 * 100 + a[28] * d[23] * p2 * 100 + a[28] * d[24] * q2 * 100 + a[28] * d[25] * r2 * 100
	offgreen_score2123 = a[29] * e[0] * i * 100 + a[29] * e[1] * j * 100 + a[29] * e[2] * k * 100 + a[29] * e[3] * l * 100 + a[29] * e[4] * m * 100 + a[29] * e[5] * n * 100 + a[29] * e[6] * o * 100 + a[29] * e[7] * p * 100 + a[29] * e[8] * q * 100 + a[29] * e[9] * r * 100 + a[29] * e[10] * s * 100 + a[29] * e[11] * t * 100 + a[29] * e[12] * u * 100 + a[29] * e[13] * v * 100 + a[29] * e[14] * w * 100 + a[29] * e[15] * x * 100 + a[29] * e[16] * i2 * 100 + a[29] * e[17] * j2 * 100 + a[29] * e[18] * k2 * 100 + a[29] * e[19] * l2 * 100 + a[29] * e[20] * m2 * 100 + a[29] * e[21] * n2 * 100 + a[29] * e[22] * o2 * 100 + a[29] * e[23] * p2 * 100 + a[29] * e[24] * q2 * 100 + a[29] * e[25] * r2 * 100
	offgreen_score2325 = a[30] * f[0] * i * 100 + a[30] * f[1] * j * 100 + a[30] * f[2] * k * 100 + a[30] * f[3] * l * 100 + a[30] * f[4] * m * 100 + a[30] * f[5] * n * 100 + a[30] * f[6] * o * 100 + a[30] * f[7] * p * 100 + a[30] * f[8] * q * 100 + a[30] * f[9] * r * 100 + a[30] * f[10] * s * 100 + a[30] * f[11] * t * 100 + a[30] * f[12] * u * 100 + a[30] * f[13] * v * 100 + a[30] * f[14] * w * 100 + a[30] * f[15] * x * 100 + a[30] * f[16] * i2 * 100 + a[30] * f[17] * j2 * 100 + a[30] * f[18] * k2 * 100 + a[30] * f[19] * l2 * 100 + a[30] * f[20] * m2 * 100 + a[30] * f[21] * n2 * 100 + a[30] * f[22] * o2 * 100 + a[30] * f[23] * p2 * 100 + a[30] * f[24] * q2 * 100 + a[30] * f[25] * r2 * 100
	offgreen_score2527 = a[31] * g[0] * i * 100 + a[31] * g[1] * j * 100 + a[31] * g[2] * k * 100 + a[31] * g[3] * l * 100 + a[31] * g[4] * m * 100 + a[31] * g[5] * n * 100 + a[31] * g[6] * o * 100 + a[31] * g[7] * p * 100 + a[31] * g[8] * q * 100 + a[31] * g[9] * r * 100 + a[31] * g[10] * s * 100 + a[31] * g[11] * t * 100 + a[31] * g[12] * u * 100 + a[31] * g[13] * v * 100 + a[31] * g[14] * w * 100 + a[31] * g[15] * x * 100 + a[31] * g[16] * i2 * 100 + a[31] * g[17] * j2 * 100 + a[31] * g[18] * k2 * 100 + a[31] * g[19] * l2 * 100 + a[31] * g[20] * m2 * 100 + a[31] * g[21] * n2 * 100 + a[31] * g[22] * o2 * 100 + a[31] * g[23] * p2 * 100 + a[31] * g[24] * q2 * 100 + a[31] * g[25] * r2 * 100
	offgreen_score2730 = a[32] * h[0] * i * 100 + a[32] * h[1] * j * 100 + a[32] * h[2] * k * 100 + a[32] * h[3] * l * 100 + a[32] * h[4] * m * 100 + a[32] * h[5] * n * 100 + a[32] * h[6] * o * 100 + a[32] * h[7] * p * 100 + a[32] * h[8] * q * 100 + a[32] * h[9] * r * 100 + a[32] * h[10] * s * 100 + a[32] * h[11] * t * 100 + a[32] * h[12] * u * 100 + a[32] * h[13] * v * 100 + a[32] * h[14] * w * 100 + a[32] * h[15] * x * 100 + a[32] * h[16] * i2 * 100 + a[32] * h[17] * j2 * 100 + a[32] * h[18] * k2 * 100 + a[32] * h[19] * l2 * 100 + a[32] * h[20] * m2 * 100 + a[32] * h[21] * n2 * 100 + a[32] * h[22] * o2 * 100 + a[32] * h[23] * p2 * 100 + a[32] * h[24] * q2 * 100 + a[32] * h[25] * r2 * 100
	offgreen_score3033 = a[33] * b2[0] * i * 100 + a[33] * b2[1] * j * 100 + a[33] * b2[2] * k * 100 + a[33] * b2[3] * l * 100 + a[33] * b2[4] * m * 100 + a[33] * b2[5] * n * 100 + a[33] * b2[6] * o * 100 + a[33] * b2[7] * p * 100 + a[33] * b2[8] * q * 100 + a[33] * b2[9] * r * 100 + a[33] * b2[10] * s * 100 + a[33] * b2[11] * t * 100 + a[33] * b2[12] * u * 100 + a[33] * b2[13] * v * 100 + a[33] * b2[14] * w * 100 + a[33] * b2[15] * x * 100 + a[33] * b2[16] * i2 * 100 + a[33] * b2[17] * j2 * 100 + a[33] * b2[18] * k2 * 100 + a[33] * b2[19] * l2 * 100 + a[33] * b2[20] * m2 * 100 + a[33] * b2[21] * n2 * 100 + a[33] * b2[22] * o2 * 100 + a[33] * b2[23] * p2 * 100 + a[33] * b2[24] * q2 * 100 + a[33] * b2[25] * r2 * 100
	offgreen_score3336 = a[34] * c2[0] * i * 100 + a[34] * c2[1] * j * 100 + a[34] * c2[2] * k * 100 + a[34] * c2[3] * l * 100 + a[34] * c2[4] * m * 100 + a[34] * c2[5] * n * 100 + a[34] * c2[6] * o * 100 + a[34] * c2[7] * p * 100 + a[34] * c2[8] * q * 100 + a[34] * c2[9] * r * 100 + a[34] * c2[10] * s * 100 + a[34] * c2[11] * t * 100 + a[34] * c2[12] * u * 100 + a[34] * c2[13] * v * 100 + a[34] * c2[14] * w * 100 + a[34] * c2[15] * x * 100 + a[34] * c2[16] * i2 * 100 + a[34] * c2[17] * j2 * 100 + a[34] * c2[18] * k2 * 100 + a[34] * c2[19] * l2 * 100 + a[34] * c2[20] * m2 * 100 + a[34] * c2[21] * n2 * 100 + a[34] * c2[22] * o2 * 100 + a[34] * c2[23] * p2 * 100 + a[34] * c2[24] * q2 * 100 + a[34] * c2[25] * r2 * 100
	offgreen_score3640 = a[35] * d2[0] * i * 100 + a[35] * d2[1] * j * 100 + a[35] * d2[2] * k * 100 + a[35] * d2[3] * l * 100 + a[35] * d2[4] * m * 100 + a[35] * d2[5] * n * 100 + a[35] * d2[6] * o * 100 + a[35] * d2[7] * p * 100 + a[35] * d2[8] * q * 100 + a[35] * d2[9] * r * 100 + a[35] * d2[10] * s * 100 + a[35] * d2[11] * t * 100 + a[35] * d2[12] * u * 100 + a[35] * d2[13] * v * 100 + a[35] * d2[14] * w * 100 + a[35] * d2[15] * x * 100 + a[35] * d2[16] * i2 * 100 + a[35] * d2[17] * j2 * 100 + a[35] * d2[18] * k2 * 100 + a[35] * d2[19] * l2 * 100 + a[35] * d2[20] * m2 * 100 + a[35] * d2[21] * n2 * 100 + a[35] * d2[22] * o2 * 100 + a[35] * d2[23] * p2 * 100 + a[35] * d2[24] * q2 * 100 + a[35] * d2[25] * r2 * 100
	offgreen_score4044 = a[36] * e2[0] * i * 100 + a[36] * e2[1] * j * 100 + a[36] * e2[2] * k * 100 + a[36] * e2[3] * l * 100 + a[36] * e2[4] * m * 100 + a[36] * e2[5] * n * 100 + a[36] * e2[6] * o * 100 + a[36] * e2[7] * p * 100 + a[36] * e2[8] * q * 100 + a[36] * e2[9] * r * 100 + a[36] * e2[10] * s * 100 + a[36] * e2[11] * t * 100 + a[36] * e2[12] * u * 100 + a[36] * e2[13] * v * 100 + a[36] * e2[14] * w * 100 + a[36] * e2[15] * x * 100 + a[36] * e2[16] * i2 * 100 + a[36] * e2[17] * j2 * 100 + a[36] * e2[18] * k2 * 100 + a[36] * e2[19] * l2 * 100 + a[36] * e2[20] * m2 * 100 + a[36] * e2[21] * n2 * 100 + a[36] * e2[22] * o2 * 100 + a[36] * e2[23] * p2 * 100 + a[36] * e2[24] * q2 * 100 + a[36] * e2[25] * r2 * 100
	offgreen_score4449 = a[37] * f2[0] * i * 100 + a[37] * f2[1] * j * 100 + a[37] * f2[2] * k * 100 + a[37] * f2[3] * l * 100 + a[37] * f2[4] * m * 100 + a[37] * f2[5] * n * 100 + a[37] * f2[6] * o * 100 + a[37] * f2[7] * p * 100 + a[37] * f2[8] * q * 100 + a[37] * f2[9] * r * 100 + a[37] * f2[10] * s * 100 + a[37] * f2[11] * t * 100 + a[37] * f2[12] * u * 100 + a[37] * f2[13] * v * 100 + a[37] * f2[14] * w * 100 + a[37] * f2[15] * x * 100 + a[37] * f2[16] * i2 * 100 + a[37] * f2[17] * j2 * 100 + a[37] * f2[18] * k2 * 100 + a[37] * f2[19] * l2 * 100 + a[37] * f2[20] * m2 * 100 + a[37] * f2[21] * n2 * 100 + a[37] * f2[22] * o2 * 100 + a[37] * f2[23] * p2 * 100 + a[37] * f2[24] * q2 * 100 + a[37] * f2[25] * r2 * 100
	offgreen_score4954 = a[38] * g2[0] * i * 100 + a[38] * g2[1] * j * 100 + a[38] * g2[2] * k * 100 + a[38] * g2[3] * l * 100 + a[38] * g2[4] * m * 100 + a[38] * g2[5] * n * 100 + a[38] * g2[6] * o * 100 + a[38] * g2[7] * p * 100 + a[38] * g2[8] * q * 100 + a[38] * g2[9] * r * 100 + a[38] * g2[10] * s * 100 + a[38] * g2[11] * t * 100 + a[38] * g2[12] * u * 100 + a[38] * g2[13] * v * 100 + a[38] * g2[14] * w * 100 + a[38] * g2[15] * x * 100 + a[38] * g2[16] * i2 * 100 + a[38] * g2[17] * j2 * 100 + a[38] * g2[18] * k2 * 100 + a[38] * g2[19] * l2 * 100 + a[38] * g2[20] * m2 * 100 + a[38] * g2[21] * n2 * 100 + a[38] * g2[22] * o2 * 100 + a[38] * g2[23] * p2 * 100 + a[38] * g2[24] * q2 * 100 + a[38] * g2[25] * r2 * 100
	#offgreen_score5460 = a[39] * h2[0] * i * 100 + a[39] * h2[1] * j * 100 + a[39] * h2[2] * k * 100 + a[39] * h2[3] * l * 100 + a[39] * h2[4] * m * 100 + a[39] * h2[5] * n * 100 + a[39] * h2[6] * o * 100 + a[39] * h2[7] * p * 100 + a[39] * h2[8] * q * 100 + a[39] * h2[9] * r * 100 + a[39] * h2[10] * s * 100 + a[39] * h2[11] * t * 100 + a[39] * h2[12] * u * 100 + a[39] * h2[13] * v * 100 + a[39] * h2[14] * w * 100 + a[39] * h2[15] * x * 100 + a[39] * h2[16] * i2 * 100 + a[39] * h2[17] * j2 * 100 + a[39] * h2[18] * k2 * 100 + a[39] * h2[19] * l2 * 100 + a[39] * h2[20] * m2 * 100 + a[39] * h2[21] * n2 * 100 + a[39] * h2[22] * o2 * 100 + a[39] * h2[23] * p2 * 100 + a[39] * h2[24] * q2 * 100 + a[39] * h2[25] * r2 * 100
	#offgreen_score6066 = a[40] * z[0] * i * 100 + a[40] * z[1] * j * 100 + a[40] * z[2] * k * 100 + a[40] * z[3] * l * 100 + a[40] * z[4] * m * 100 + a[40] * z[5] * n * 100 + a[40] * z[6] * o * 100 + a[40] * z[7] * p * 100 + a[40] * z[8] * q * 100 + a[40] * z[9] * r * 100 + a[40] * z[10] * s * 100 + a[40] * z[11] * t * 100 + a[40] * z[12] * u * 100 + a[40] * z[13] * v * 100 + a[40] * z[14] * w * 100 + a[40] * z[15] * x * 100 + a[40] * z[16] * i2 * 100 + a[40] * z[17] * j2 * 100 + a[40] * z[18] * k2 * 100 + a[40] * z[19] * l2 * 100 + a[40] * z[20] * m2 * 100 + a[40] * z[21] * n2 * 100 + a[40] * z[22] * o2 * 100 + a[40] * z[23] * p2 * 100 + a[40] * z[24] * q2 * 100 + a[40] * z[25] * r2 * 100
	offgreen_scoreb = offgreen_score1617 + offgreen_score1719 + offgreen_score1921 + offgreen_score2123 + offgreen_score2325 + offgreen_score2527 + offgreen_score2730 + offgreen_score3033 + offgreen_score3336 + offgreen_score3640 + offgreen_score4044 + offgreen_score4449 + offgreen_score4954# + offgreen_score5460 + offgreen_score6066
	offgreen_score = np.append(0, offgreen_scoreb)
	golf_score = green_score + offgreen_score
	golf_sum = golf_score * ([2, 3, 4, 5, 6])
	golf_average = np.sum(golf_sum)/np.sum(golf_score)
	z = np.append(z, golf_average)
	return z
	
golf_5iimprovement = [golf_5ipct, golf_5ipct1, golf_5ipct2, golf_5ipct3, golf_5ipct4]
score_5i1 = np.array([])
score_5i2 = np.array([])
score_5i3 = np.array([])
score_5i4 = np.array([])
score_5i5 = np.array([])
golf_score = [score_5i1, score_5i2, score_5i3, score_5i4, score_5i5]
game_num = (0, 1, 2, 3, 4)
#chipping_1617yp4, chipping_1719yp4, chipping_1921yp4, chipping_2123yp4, chipping_2325yp4, chipping_2527yp4, chipping_2730yp4, chipping_3033yp4, chipping_3336yp4, chipping_3640yp4, chipping_4044yp4, chipping_4449yp4, chipping_4954yp4, chipping_5460yp4, chipping_6066yp4
for x in game_num:
	a = golf_5iimprovement[x]
	b = chipping_1617yp
	c = chipping_1719yp
	d = chipping_1921yp
	e = chipping_2123yp
	f = chipping_2325yp
	g = chipping_2527yp
	h = chipping_2730yp
	b2 = chipping_3033yp
	c2 = chipping_3336yp
	d2 = chipping_3640yp
	e2 = chipping_4044yp
	f2 = chipping_4449yp
	g2 = chipping_4954yp
	h2 = chipping_5460yp
	z = chipping_6066yp
	i = golf_ft1
	j = golf_ft2
	k = golf_ft3
	l = golf_ft4
	m = golf_ft5
	n = golf_ft6
	o = golf_ft7
	p = golf_ft8
	q = golf_ft9
	r = golf_ft10
	s = golf_ft11
	t = golf_ft12
	u = golf_ft13
	v = golf_ft14
	w = golf_ft15
	x = golf_ft1617
	i2 = golf_ft1819
	j2 = golf_ft2021
	k2 = golf_ft2223
	l2 = golf_ft2425
	m2 = golf_ft2628
	n2 = golf_ft2931
	o2 = golf_ft3234
	p2 = golf_ft3538
	q2 = golf_ft3942
	r2 = golf_ft4347
	z = golfaverage_array5i
	golfaverage_array5i = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z, b2, c2, d2, e2, f2, g2, h2, i2, k2, l2, m2, n2, o2, p2, q2, r2)

print(golfaverage_array5i, '5i')
	

chipping_1617improvement = [chipping_1617yp, chipping_1617yp1, chipping_1617yp2, chipping_1617yp3, chipping_1617yp4]
chipping_1719improvement = [chipping_1719yp, chipping_1719yp1, chipping_1719yp2, chipping_1719yp3, chipping_1719yp4]
chipping_1921improvement = [chipping_1921yp, chipping_1921yp1, chipping_1921yp2, chipping_1921yp3, chipping_1921yp4]
chipping_2123improvement = [chipping_2123yp, chipping_2123yp1, chipping_2123yp2, chipping_2123yp3, chipping_2123yp4]
chipping_2325improvement = [chipping_2325yp, chipping_2325yp1, chipping_2325yp2, chipping_2325yp3, chipping_2325yp4]
chipping_2527improvement = [chipping_2527yp, chipping_2527yp1, chipping_2527yp2, chipping_2527yp3, chipping_2527yp4]
chipping_2730improvement = [chipping_2730yp, chipping_2730yp1, chipping_2730yp2, chipping_2730yp3, chipping_2730yp4]
chipping_3033improvement = [chipping_3033yp, chipping_3033yp1, chipping_3033yp2, chipping_3033yp3, chipping_3033yp4]
chipping_3336improvement = [chipping_3336yp, chipping_3336yp1, chipping_3336yp2, chipping_3336yp3, chipping_3336yp4]
chipping_3640improvement = [chipping_3640yp, chipping_3640yp1, chipping_3640yp2, chipping_3640yp3, chipping_3640yp4]
chipping_4044improvement = [chipping_4044yp, chipping_4044yp1, chipping_4044yp2, chipping_4044yp3, chipping_4044yp4]
chipping_4449improvement = [chipping_4449yp, chipping_4449yp1, chipping_4449yp2, chipping_4449yp3, chipping_4449yp4]
chipping_4954improvement = [chipping_4954yp, chipping_4954yp1, chipping_4954yp2, chipping_4954yp3, chipping_4954yp4]
chipping_5460improvement = [chipping_5460yp, chipping_5460yp1, chipping_5460yp2, chipping_5460yp3, chipping_5460yp4]
chipping_6066improvement = [chipping_6066yp, chipping_6066yp1, chipping_6066yp2, chipping_6066yp3, chipping_6066yp4]
score_5i1chp1 = np.array([])
score_5i1chp2 = np.array([])
score_5i1chp3 = np.array([])
score_5i1chp4 = np.array([])
score_5i1chp5 = np.array([])
score_5i2chp1 = np.array([])
score_5i2chp2 = np.array([])
score_5i2chp3 = np.array([])
score_5i2chp4 = np.array([])
score_5i2chp5 = np.array([])
score_5i3chp1 = np.array([])
score_5i3chp2 = np.array([])
score_5i3chp3 = np.array([])
score_5i3chp4 = np.array([])
score_5i3chp5 = np.array([])
score_5i4chp1 = np.array([])
score_5i4chp2 = np.array([])
score_5i4chp3 = np.array([])
score_5i4chp4 = np.array([])
score_5i4chp5 = np.array([])
score_5i5chp1 = np.array([])
score_5i5chp2 = np.array([])
score_5i5chp3 = np.array([])
score_5i5chp4 = np.array([])
score_5i5chp5 = np.array([])
golf_score1 = [score_5i1chp1, score_5i1chp2, score_5i1chp3, score_5i1chp4, score_5i1chp5, score_5i2chp1, score_5i2chp2, score_5i2chp3, score_5i2chp4, score_5i2chp5, score_5i3chp1, score_5i3chp2, score_5i3chp3, score_5i3chp4, score_5i3chp5, score_5i4chp1, score_5i4chp2, score_5i4chp3, score_5i4chp4, score_5i4chp5, score_5i5chp1, score_5i5chp2, score_5i5chp3, score_5i5chp4, score_5i5chp5]
game_num = (0, 1, 2, 3, 4)
game_num2 = (0, 1, 2, 3, 4)
s = 0

for x in game_num:
	a = golf_5iimprovement[x]
	b = chipping_1617yp
	c = chipping_1719yp
	d = chipping_1921yp
	e = chipping_2123yp
	f = chipping_2325yp
	g = chipping_2527yp
	h = chipping_2730yp
	b2 = chipping_3033yp
	c2 = chipping_3336yp
	d2 = chipping_3640yp
	e2 = chipping_4044yp
	f2 = chipping_4449yp
	g2 = chipping_4954yp
	h2 = chipping_5460yp
	i = golf_ft1
	j = golf_ft2
	k = golf_ft3
	l = golf_ft4
	m = golf_ft5
	n = golf_ft6
	o = golf_ft7
	p = golf_ft8
	q = golf_ft9
	r = golf_ft10
	s = golf_ft11
	t = golf_ft12
	u = golf_ft13
	w = golf_ft14
	x = golf_ft15
	y = golf_ft1617
	i2 = golf_ft1819
	j2 = golf_ft2021
	k2 = golf_ft2223
	l2 = golf_ft2425
	m2 = golf_ft2628
	n2 = golf_ft2931
	o2 = golf_ft3234
	p2 = golf_ft3538
	q2 = golf_ft3942
	r2 = golf_ft4347
	golfaverage_array = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z, b2, c2, d2, e2, f2, g2, h2, i2, k2, l2, m2, n2, o2, p2, q2, r2)
		
golfaverage_arraychp = np.array([])
for x in game_num:
	a = golf_5ipct
	print(a)
	print(np.sum(a))
	b = chipping_1617improvement[x]
	c = chipping_1719improvement[x]
	d = chipping_1921improvement[x]
	e = chipping_2123improvement[x]
	f = chipping_2325improvement[x]
	g = chipping_2527improvement[x]
	h = chipping_2730improvement[x]
	b2 = chipping_3033improvement[x]
	c2 = chipping_3336improvement[x]
	d2 = chipping_3640improvement[x]
	e2 = chipping_4044improvement[x]
	f2 = chipping_4449improvement[x]
	g2 = chipping_4954improvement[x]
	h2 = chipping_5460improvement[x]
	i = golf_ft1
	j = golf_ft2
	k = golf_ft3
	l = golf_ft4
	m = golf_ft5
	n = golf_ft6
	o = golf_ft7
	p = golf_ft8
	q = golf_ft9
	r = golf_ft10
	s = golf_ft11
	t = golf_ft12
	u = golf_ft13
	w = golf_ft14
	x = golf_ft15
	y = golf_ft1617
	i2 = golf_ft1819
	j2 = golf_ft2021
	k2 = golf_ft2223
	l2 = golf_ft2425
	m2 = golf_ft2628
	n2 = golf_ft2931
	o2 = golf_ft3234
	p2 = golf_ft3538
	q2 = golf_ft3942
	r2 = golf_ft4347
	q = golfaverage_arraychp
	golfaverage_arraychp = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, z, b2, c2, d2, e2, f2, g2, h2, i2, k2, l2, m2, n2, o2, p2, q2, r2)

print(golfaverage_arraychp, 'chp')
	
	
		

golf_u1f = pd.DataFrame(golf.loc[golf.Unit_1 == 'FT'])
golf_u2f = pd.DataFrame(golf.loc[golf.Unit_2 == 'FT'])
golf_u3f = pd.DataFrame(golf.loc[golf.Unit_3 == 'FT'])
golf_u4f = pd.DataFrame(golf.loc[golf.Unit_4 == 'FT'])
golf_u5f = pd.DataFrame(golf.loc[golf.Unit_5 == 'FT'])
golf_u6f = pd.DataFrame(golf.loc[golf.Unit_6 == 'FT'])
golf_u7f = pd.DataFrame(golf.loc[golf.Unit_7 == 'FT'])
golf_u12f = golf_u1f.append(golf_u2f)
golf_u123f = golf_u12f.append(golf_u3f)
golf_u1234f = golf_u123f.append(golf_u4f)
golf_u12345f = golf_u1234f.append(golf_u5f)
golf_u123456f = golf_u12345f.append(golf_u6f)
golf_ftd = golf_u123456f.append(golf_u7f)
golf_ft = golf_ftd.drop_duplicates()


	
golf_pp = [golf_ft03, golf_ft45, golf_ft68, golf_ft912, golf_ft1317, golf_ft1825, golf_ft2635, golf_ft3645]
for x in putt_num:
	f = golf_ft
	a = golf_puttbins[x]
	b = golf_puttbins2[x]
	golf_puttrange = putting_distances(f, a, b)
	golf_pp[x] = np.append(golf_pp[x], golf_puttrange)

golf_ft03 = golf_pp[0]
golf_ft45 = golf_pp[1]
golf_ft68 = golf_pp[2]
golf_ft912 = golf_pp[3]
golf_ft1317 = golf_pp[4]
golf_ft1825 = golf_pp[5]
golf_ft2635 = golf_pp[6]
golf_ft3645 = golf_pp[7]
golf_ppc = [golf_ft45, golf_ft68, golf_ft912, golf_ft1317, golf_ft1825, golf_ft2635, golf_ft3645, golf_ft4655, golf_ft5665]
putt_numc = (0, 1, 2, 3, 4, 5, 6)
golf_ft031 = golf_ft03 + ([.02, -.02, 0, 0])
def putt_change1(a): 
	putt_aoof = a
	x = putt_aoof[0] * .1
	x2 = x * putt_aoof[2]/(putt_aoof[2] + putt_aoof[3])
	x3 = x * putt_aoof[3]/(putt_aoof[2] + putt_aoof[3])
	putt_imp = np.array([x, -x2, -x3, 0])
	putt_improvement1 = putt_aoof + putt_imp
	return putt_improvement1
	
golf_ft451 = np.array([])
golf_ft681 = np.array([])
golf_ft9121 = np.array([])
golf_ft13171 = np.array([])
golf_ft18251 = np.array([])
golf_ft26351 = np.array([])
golf_ft36451 = np.array([])


golf_pp1 = [golf_ft451, golf_ft681, golf_ft9121, golf_ft13171, golf_ft18251, golf_ft26351, golf_ft36451]

for x in putt_numc:
	a = golf_ppc[x]
	putt_improvement1 = putt_change1(a)
	golf_pp1[x] = np.append(golf_pp1[x], putt_improvement1)
	
golf_ft451 = golf_pp1[0]
golf_ft681 = golf_pp1[1]
golf_ft9121 = golf_pp1[2]
golf_ft13171 = golf_pp1[3]
golf_ft18251 = golf_pp1[4]
golf_ft26351 = golf_pp1[5]
golf_ft36451 = golf_pp1[6]
	
def putt_change2(a): 
	putt_aoof = a
	x = putt_aoof[0] * .15
	x2 = x * putt_aoof[2]/(putt_aoof[2] + putt_aoof[3])
	x3 = x * putt_aoof[3]/(putt_aoof[2] + putt_aoof[3])
	putt_imp = np.array([x, -x2, -x3, 0])
	putt_improvement2 = putt_aoof + putt_imp
	return putt_improvement2
	
golf_ft452 = np.array([])
golf_ft682 = np.array([])
golf_ft9122 = np.array([])
golf_ft13172 = np.array([])
golf_ft18252 = np.array([])
golf_ft26352 = np.array([])
golf_ft36452 = np.array([])

golf_pp2 = [golf_ft452, golf_ft682, golf_ft9122, golf_ft13172, golf_ft18252, golf_ft26352, golf_ft36452]

for x in putt_numc:
	a = golf_ppc[x]
	putt_improvement2 = putt_change2(a)
	golf_pp2[x] = np.append(golf_pp2[x], putt_improvement2)
	
golf_ft452 = golf_pp2[0]
golf_ft682 = golf_pp2[1]
golf_ft9122 = golf_pp2[2]
golf_ft13172 = golf_pp2[3]
golf_ft18252 = golf_pp2[4]
golf_ft26352 = golf_pp2[5]
golf_ft36452 = golf_pp2[6]

def putt_change3(a): 
	putt_aoof = a
	x = putt_aoof[0] * .2
	x2 = x * putt_aoof[2]/(putt_aoof[2] + putt_aoof[3])
	x3 = x * putt_aoof[3]/(putt_aoof[2] + putt_aoof[3])
	putt_imp = np.array([x, -x2, -x3, 0])
	putt_improvement3 = putt_aoof + putt_imp
	return putt_improvement3
	
golf_ft453 = np.array([])
golf_ft683 = np.array([])
golf_ft9123 = np.array([])
golf_ft13173 = np.array([])
golf_ft18253 = np.array([])
golf_ft26353 = np.array([])
golf_ft36453 = np.array([])

golf_pp3 = [golf_ft453, golf_ft683, golf_ft9123, golf_ft13173, golf_ft18253, golf_ft26353, golf_ft36453]

for x in putt_numc:
	a = golf_ppc[x]
	putt_improvement3 = putt_change3(a)
	golf_pp3[x] = np.append(golf_pp3[x], putt_improvement3)
	
golf_ft453 = golf_pp3[0]
golf_ft683 = golf_pp3[1]
golf_ft9123 = golf_pp3[2]
golf_ft13173 = golf_pp3[3]
golf_ft18253 = golf_pp3[4]
golf_ft26353 = golf_pp3[5]
golf_ft36453 = golf_pp3[6]

def putt_change4(a): 
	putt_aoof = a
	x = putt_aoof[0] * .25
	x2 = x * putt_aoof[2]/(putt_aoof[2] + putt_aoof[3])
	x3 = x * putt_aoof[3]/(putt_aoof[2] + putt_aoof[3])
	putt_imp = np.array([x, -x2, -x3, 0])
	putt_improvement4 = putt_aoof + putt_imp
	return putt_improvement4
	
golf_ft454 = np.array([])
golf_ft684 = np.array([])
golf_ft9124 = np.array([])
golf_ft13174 = np.array([])
golf_ft18254 = np.array([])
golf_ft26354 = np.array([])
golf_ft36454 = np.array([])

golf_pp4 = [golf_ft454, golf_ft684, golf_ft9124, golf_ft13174, golf_ft18254, golf_ft26354, golf_ft36454]

for x in putt_numc:
	a = golf_ppc[x]
	putt_improvement4 = putt_change4(a)
	golf_pp4[x] = np.append(golf_pp4[x], putt_improvement4)
	
golf_ft454 = golf_pp4[0]
golf_ft684 = golf_pp4[1]
golf_ft9124 = golf_pp4[2]
golf_ft13174 = golf_pp4[3]
golf_ft18254 = golf_pp4[4]
golf_ft26354 = golf_pp4[5]
golf_ft36454 = golf_pp4[6]

def putt_change5(a): 
	putt_aoof = a
	x = putt_aoof[0] * .3
	x2 = x * putt_aoof[2]/(putt_aoof[2] + putt_aoof[3])
	x3 = x * putt_aoof[3]/(putt_aoof[2] + putt_aoof[3])
	putt_imp = np.array([x, -x2, -x3, 0])
	putt_improvement5 = putt_aoof + putt_imp
	return putt_improvement5
	
golf_ft455 = np.array([])
golf_ft685 = np.array([])
golf_ft9125 = np.array([])
golf_ft13175 = np.array([])
golf_ft18255 = np.array([])
golf_ft26355 = np.array([])
golf_ft36455 = np.array([])

golf_pp5 = [golf_ft455, golf_ft685, golf_ft9125, golf_ft13175, golf_ft18255, golf_ft26355, golf_ft36455]

for x in putt_numc:
	a = golf_ppc[x]
	putt_improvement5 = putt_change5(a)
	golf_pp5[x] = np.append(golf_pp5[x], putt_improvement5)
	
golf_ft455 = golf_pp5[0]
golf_ft685 = golf_pp5[1]
golf_ft9125 = golf_pp5[2]
golf_ft13175 = golf_pp5[3]
golf_ft18255 = golf_pp5[4]
golf_ft26355 = golf_pp5[5]
golf_ft36455 = golf_pp5[6]

	

golf_ft45improvement = [golf_ft45, golf_ft451, golf_ft452, golf_ft453, golf_ft454, golf_ft455]
print(golf_ft45improvement, '45imp')
golf_ft68improvement = [golf_ft68, golf_ft681, golf_ft682, golf_ft683, golf_ft684, golf_ft685]
golf_ft912improvement = [golf_ft912, golf_ft9121, golf_ft9122, golf_ft9123, golf_ft9124, golf_ft9125]
golf_ft1317improvement = [golf_ft1317, golf_ft13171, golf_ft13172, golf_ft13173, golf_ft13174, golf_ft13175]
golf_ft1825improvement = [golf_ft1825, golf_ft18251, golf_ft18252, golf_ft18253, golf_ft18254, golf_ft18255]
golf_ft2635improvement = [golf_ft2635, golf_ft26351, golf_ft26352, golf_ft26353, golf_ft26354, golf_ft26355]
golf_ft3645improvement = [golf_ft3645, golf_ft36451, golf_ft36452, golf_ft36453, golf_ft36454, golf_ft36455]
golf_score = [score_5i1chp1, score_5i1chp2, score_5i1chp3, score_5i1chp4, score_5i1chp5, score_5i2chp1, score_5i2chp2, score_5i2chp3, score_5i2chp4, score_5i2chp5, score_5i3chp1, score_5i3chp2, score_5i3chp3, score_5i3chp4, score_5i3chp5, score_5i4chp1, score_5i4chp2, score_5i4chp3, score_5i4chp4, score_5i4chp5, score_5i5chp1, score_5i5chp2, score_5i5chp3, score_5i5chp4, score_5i5chp5]

game_num3 = (0, 1, 2, 3, 4, 5)
for x in game_num:
	for y in game_num2:
		for z in game_num3:
			a = golf_5iimprovement[x]
			b = chipping_1520improvement[y]
			c = chipping_2025improvement[y]
			d = chipping_2530improvement[y]
			e = chipping_3035improvement[y]
			f = chipping_3540improvement[y]
			g = chipping_4050improvement[y]
			h = chipping_5060improvement[y]
			i = golf_ft03
			j = golf_ft45improvement[z]
			k = golf_ft68improvement[z]
			l = golf_ft912improvement[z]
			m = golf_ft1317improvement[z]
			n = golf_ft1825improvement[z]
			o = golf_ft2635improvement[z]
			p = golf_ft3645improvement[z]
			q = golfaverage_array
			golfaverage_array = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
			
print(golfaverage_array)

game_num3 = (0, 1, 2, 3, 4, 5)
for z in game_num3:
	a = golf_5ipct
	b = chipping_1520yp
	c = chipping_2025yp
	d = chipping_2530yp
	e = chipping_3035yp
	f = chipping_3540yp
	g = chipping_yp
	h = chipping_yp
	i = golf_ft03
	j = golf_ft45improvement[z]
	k = golf_ft68improvement[z]
	l = golf_ft912improvement[z]
	m = golf_ft1317improvement[z]
	n = golf_ft1825improvement[z]
	o = golf_ft2635improvement[z]
	p = golf_ft3645improvement[z]
	q = golfaverage_array
	golfaverage_array = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
			
print(golfaverage_array)
			
	
