import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pylab
import scipy.stats as stats
import random
import sys
#import xlrd


golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\ScoreSheet - Sheet1.csv')
expected_putts = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Putts - Sheet1.csv')
expected_rough = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Rough - Sheet1.csv')


golf_3 = pd.DataFrame(golf.loc[golf.Par == 3])
golf_4 = pd.DataFrame(golf.loc[golf.Par == 4])
golf_5 = pd.DataFrame(golf.loc[golf.Par == 5])


golf_3GIR = pd.DataFrame(golf_3.loc[golf_3.Result_1 == 'Green'])
golf_4GIR = pd.DataFrame(golf_4.loc[golf_4.Result_2 == 'Green'])
golf_5GIR = pd.DataFrame(golf_5.loc[golf_5.Result_3 == 'Green'])


GIR_list = [golf_3GIR, golf_4GIR, golf_5GIR]
ToHole_list = ["To_Hole1", "To_Hole2", "To_Hole3"]

GIR_df = pd.DataFrame(columns = ['Proximity'])
eGIR_df = pd.DataFrame(columns = ['Proximity'])
IP_df = pd.DataFrame(columns = ['Proximity'])
Blackjack_df = pd.DataFrame(columns = ['Proximity'])
n = 0

def GIRidentifier(GIR_list, ToHole_list, df, num, num2):
	n = 0
	for x1 in range(0, 3):
		GIR = GIR_list[x1]
		ToHole = ToHole_list[x1]
		proximity = GIR[ToHole]
		for x2 in range(0, len(proximity)):
			if float(proximity.iloc[x2]) <= num and float(proximity.iloc[x2]) > num2:
				df.loc[n, 'Proximity'] = float(proximity.iloc[x2])
				n = n + 1
			else:
				continue
	return df

GIRidentifier(GIR_list, ToHole_list, GIR_df, 120, 40)
GIRidentifier(GIR_list, ToHole_list, eGIR_df, 40, 20)
GIRidentifier(GIR_list, ToHole_list, IP_df, 20, 8)
GIRidentifier(GIR_list, ToHole_list, Blackjack_df, 8, 0)

def ExpectedPuttsbyGIR(df, expected_putts):
	expect_putt_df = pd.DataFrame(columns = ['Expected Putts'])
	n = 0
	for x1 in range(0, len(df)):
		proximity = float(df.iloc[x1])
		expect_putt = pd.DataFrame(expected_putts.loc[expected_putts.Distance == proximity])
		expect_putt = float(expect_putt.Shots)
		expect_putt_df.loc[n, 'Expected Putts'] = expect_putt
		n = n + 1
		if n == len(df):
			print(expect_putt_df['Expected Putts'].mean())
		else:
			continue

ExpectedPuttsbyGIR(GIR_df, expected_putts)
ExpectedPuttsbyGIR(eGIR_df, expected_putts)
ExpectedPuttsbyGIR(IP_df, expected_putts)
ExpectedPuttsbyGIR(Blackjack_df, expected_putts)


golf_3mGIR = pd.DataFrame(golf_3.loc[golf_3.Result_1 != 'Green'])
golf_4mGIR = pd.DataFrame(golf_4.loc[golf_4.Result_2 != 'Green'])
golf_5mGIR = pd.DataFrame(golf_5.loc[golf_5.Result_3 != 'Green'])


mGIR_list = [golf_3mGIR, golf_4mGIR, golf_5mGIR]
nextToHole_list = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4']
nextUnit_list = ['Unit_2', 'Unit_3', 'Unit_4']
P6_df = pd.DataFrame(columns = ['Proximity', 'Distance'])


def GIRidentifier(mGIR_list, nextToHole_list, nextUnit_list, df):
	n = 0
	for x1 in range(0, 3):
		mGIR = mGIR_list[x1]
		nextUnit = nextUnit_list[x1]
		distance = mGIR[nextToHole_list[x1]]
		predistance = mGIR[nextToHole_list[x1-1]]
		x1 = x1 + 1
		nextToHole = nextToHole_list[x1]
		proximity = mGIR[nextToHole]
		for x2 in range(0, len(proximity)):
			if float(proximity.iloc[x2]) <= 6 and str(mGIR[nextUnit].iloc[x2]) == "FT":
				df.loc[n, 'Proximity'] = float(proximity.iloc[x2])
				if np.isnan(distance.iloc[x2]) == False:
					df.loc[n, 'Distance'] = float(distance.iloc[x2])
					n = n + 1
				elif np.isnan(distance.iloc[x2]) == True:
					df.loc[n, 'Distance'] = float(predistance.iloc[x2])
					n = n + 1
			else:
				continue
	return df

GIRidentifier(mGIR_list, nextToHole_list, nextUnit_list, P6_df)


def P6processor(df, expected_putts, expected_rough):
	P6difference = pd.DataFrame(columns = ['Strokes Gained'])
	n = 0
	for x1 in range(0, len(df)):
		shot = df.iloc[x1]
		proximity = float(shot['Proximity'])
		expect_putt = pd.DataFrame(expected_putts.loc[expected_putts.Distance == proximity])
		expect_putt = float(expect_putt.Shots)
		distance = float(shot['Distance'])
		expect_rough = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance])
		expect_rough= float(expect_rough.Shots)
		P6difference.loc[n, 'Strokes Gained'] = expect_rough - 1 - expect_putt
		n = n + 1
		if n == len(df):
			print(P6difference['Strokes Gained'].mean())
		else:
			continue


P6processor(P6_df, expected_putts, expected_rough)
