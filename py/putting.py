import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\ScoreSheet - Sheet1.csv')
expected_putts = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Putts - Sheet1.csv')
expected_tee = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Tee - Sheet1.csv')
expected_fairway = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Fairway - Sheet1.csv')
expected_recovery = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Recovery - Sheet1.csv')
expected_rough = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Rough - Sheet1.csv')
expected_bunker = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Shots_from_Bunker - Sheet1.csv')

#CALCULATE SCORES FOR EACH ROUND 
#make a dataframe that only contains tournament rounds
tournament_df = pd.DataFrame(golf.loc[golf.Tournament == 'Hurricane']).append(pd.DataFrame(golf.loc[golf.Tournament == 'FJT']))
tournament_df = tournament_df.append(pd.DataFrame(golf.loc[golf.Tournament == 'AJGA']))


#make a list that contains all tournament dates
tournament_dates = tournament_df['Date'].dropna().unique()
tournament_dates = sorted(tournament_dates)
tournament_dates_list = []

for x in tournament_dates:
	round = pd.DataFrame(golf.loc[golf.Date == x])
	if len(round) == 18:
		tournament_dates_list.append(x)
	else:
		continue



n = 0
unit_list = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
distance_list = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70]
sgputting05 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting510 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting1015 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting1520 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting2025 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting2530 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting3040 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting4050 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting5060 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
sgputting6070 = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
puttingdf_list = [sgputting05, sgputting510, sgputting1015, sgputting1520, sgputting2025, sgputting2530, sgputting3040, sgputting4050, sgputting5060, sgputting6070]
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		for num in range(0, 18):
			hole = round.iloc[num]
			for x in unit_list:
				if hole[x] == 'FT':
					x = x.replace('Unit_', 'To_Hole')
					putt_length = int(hole[x])
					x = int(x.replace('To_Hole', ''))
					y = str(x + 1)
					a = 'Result_' + y
					b = 'To_Hole' + y
					for k in range(0,10):
						if putt_length > distance_list[k]:
							if putt_length <= distance_list[k+1]:
								expect_putt = pd.DataFrame(expected_putts.loc[expected_putts.Distance == putt_length])
								expect_putt = float(expect_putt.Shots)
								if hole[a] == 'Made':
									puttingdf_list[k].loc[n, 'Strokes Gained Putting'] = expect_putt - 1
									puttingdf_list[k].loc[n, 'date'] = date
									n = n + 1
								else:
									next_putt_length = hole[b]
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == next_putt_length])
									expect_next = float(expect_next.Shots)
									puttingdf_list[k].loc[n, 'Strokes Gained Putting'] = expect_putt - 1 - expect_next
									puttingdf_list[k].loc[n, 'date'] = date
									n = n + 1
							else:
								continue
						else:
							continue
				else:
					continue	
	else:
		continue

putting_by_distance = pd.DataFrame(columns = ['distance', 'Strokes Gained Putting'])
for x in range(0, 10):
	if len(puttingdf_list[x]) != 0:
		print(len(puttingdf_list[x]))
		print(puttingdf_list[x]['Strokes Gained Putting'].sum())
		putting = float((puttingdf_list[x]['Strokes Gained Putting'].sum())/(len(puttingdf_list[x])))
		putting_by_distance.loc[x, 'Strokes Gained Putting'] = putting
		putting_by_distance.loc[x, 'distance'] = str(distance_list[x]) + " feet to" + str(distance_list[x+1]) + " feet"
	else:
		continue

writer = pd.ExcelWriter('Putting.xlsx', engine = 'xlsxwriter')

putting_by_distance.sort_values(by=['distance'], inplace=True, ascending=True)	
putting_by_distance.to_excel(writer, sheet_name = 'SG Putting by Distance')