import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter

golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\ScoreSheet - Sheet1.csv')
expected_putts = pd.read_csv(r'C:\Users\Jon Wang\Downloads\Expected_Putts - Sheet1.csv')

golf_2nd_dist = golf.To_Hole1.tolist()
golf_2nd_dist.sort()
print(golf_2nd_dist)
#CALCULATE SCORES FOR EACH ROUND 
#make a dataframe that only contains tournament rounds
tournament_df = pd.DataFrame(golf.loc[golf.Tournament == 'Hurricane']).append(pd.DataFrame(golf.loc[golf.Tournament == 'FJT']))
tournament_df = tournament_df.append(pd.DataFrame(golf.loc[golf.Tournament == 'AJGA']))
print(tournament_df)

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
#make a dataframe to hold each round's date and score
score_df = pd.DataFrame(columns = ['date', 'score'])
n = 0
#input the dates and scores for each round into the dataframe
for x in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == x])
	if len(round) == 18:
		round_score = np.sum(round.Score)
		score_df.loc[n, 'score'] = round_score
		score_df.loc[n, 'date'] = x
		n = n + 1
	else:
		continue	

score_df['date']=pd.to_datetime(score_df['date'])
score_df.sort_values(by=['date'], inplace=True, ascending=True)	
writer = pd.ExcelWriter('GolfKPI.xlsx', engine = 'xlsxwriter')
score_df.to_excel(writer, sheet_name = 'Scores')


#CALCULATE GIR FOR EACH ROUND
gir_df = pd.DataFrame(columns = ['date', 'GIR'])
n=0
for x in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == x])
	if len(round) == 18:
		par3_df = pd.DataFrame(round.loc[round.Par == 3])
		par3_gir_df = pd.DataFrame(par3_df.loc[par3_df.Result_1 == 'Green'])
		par4_df = pd.DataFrame(round.loc[round.Par == 4])
		par4_gir_df = pd.DataFrame(par4_df.loc[par4_df.Result_2 == 'Green'])
		par5_df = pd.DataFrame(round.loc[round.Par == 5])
		par5_gir_df = pd.DataFrame(par5_df.loc[par5_df.Result_3 == 'Green']).append(pd.DataFrame(par5_df.loc[par5_df.Result_2 == 'Green']))
		gir = len(par3_gir_df) + len(par4_gir_df) + len(par5_gir_df)
		gir_df.loc[n, 'GIR'] = gir
		gir_df.loc[n, 'date'] = x
		n = n + 1
	else:
		continue

fwy_df = pd.DataFrame(columns = ['date', 'Fairways hit'])
n = 0
for x in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == x])
	if len(round) == 18:
		par45_df = pd.DataFrame(round.loc[round.Par != 3])
		par45_fwy_df = pd.DataFrame(par45_df.loc[par45_df.Result_1 == 'Fairway'])
		fwy = len(par45_fwy_df)
		fwy_df.loc[n, 'Fairways hit'] = fwy
		fwy_df.loc[n, 'date'] = x
		n = n + 1
	else:
		continue

#CALCULATE GIR FOR EACH ROUND
scrm_df = pd.DataFrame(columns = ['date', 'Scrambling %'])
n = 0
for x in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == x])
	if len(round) == 18:
		par3_df = pd.DataFrame(round.loc[round.Par == 3])
		par3_mgir_df = pd.DataFrame(par3_df.loc[par3_df.Result_1 != 'Green'])
		par4_df = pd.DataFrame(round.loc[round.Par == 4])
		par4_mgir_df = pd.DataFrame(par4_df.loc[par4_df.Result_2 != 'Green'])
		par5_df = pd.DataFrame(round.loc[round.Par == 5])
		par5_mgir_df = pd.DataFrame(par5_df.loc[par5_df.Result_3 != 'Green'])
		par3_scrm_df = pd.DataFrame(par3_mgir_df.loc[par3_mgir_df.Result_3 == 'Made'])
		par4_scrm_df = pd.DataFrame(par4_mgir_df.loc[par4_mgir_df.Result_4 == 'Made'])
		par5_scrm_df = pd.DataFrame(par5_mgir_df.loc[par5_mgir_df.Result_5 == 'Made'])
		scrm = ((len(par3_scrm_df) + len(par4_scrm_df) + len(par5_scrm_df))/(len(par3_mgir_df) + len(par4_mgir_df) + len(par5_mgir_df))) * 100
		scrm_df.loc[n, 'Scrambling %'] = scrm
		scrm_df.loc[n, 'date'] = x
		n = n + 1
	else:
		continue	

n = 0
shot_list = ['Club_1', 'Club_2', 'Club_3', 'Club_4', 'Club_5', 'Club_6', 'Club_7', 'Club_8', 'Club_9']
result_list = ['Result_1', 'Result_2', 'Result_3', 'Result_4', 'Result_5', 'Result_6', 'Result_7', 'Result_8', 'Result_9']
my_list = []
k = 0
sgputting_df = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		for num in range(0, 18):
			hole = round.iloc[num]
			for x in result_list:
				if hole[x] == 'Green':
					x = x.replace('Result_', 'To_Hole')
					putt_length = int(hole[x])
					expect_putt = pd.DataFrame(expected_putts.loc[expected_putts.Distance == putt_length])
					expect_putt = float(expect_putt.Expected_Strokes)
					x = int(x.replace('To_Hole', ''))
					a = str(x + 1)
					a = 'Result_' + a
					b = str(x + 2)
					b = 'Result_' + b
					c = str(x + 3)
					c = 'Result_' + c
					d = str(x + 4)
					d = 'Result_' + d
					if hole[a] == 'Made':
						sgputting_df.loc[n, 'Strokes Gained Putting'] = expect_putt - 1
						sgputting_df.loc[n, 'date'] = date
						n = n + 1
					elif hole[b] == 'Made':
						sgputting_df.loc[n, 'Strokes Gained Putting'] = expect_putt - 2
						sgputting_df.loc[n, 'date'] = date
						n = n + 1
					elif hole[c] == 'Made':
						sgputting_df.loc[n, 'Strokes Gained Putting'] = expect_putt - 3
						sgputting_df.loc[n, 'date'] = date
						n = n + 1
					else:
						sgputting_df.loc[n, 'Strokes Gained Putting'] = expect_putt - 4
						sgputting_df.loc[n, 'date'] = date
						n = n + 1
				else:
					continue	
	else:
		continue		

SGputt_df = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
n = 0
for date in tournament_dates_list:
	sgputting_round = pd.DataFrame(sgputting_df.loc[sgputting_df.date == date])
	sgputting_round = float(sgputting_round['Strokes Gained Putting'].sum())
	SGputt_df.loc[n, 'Strokes Gained Putting'] = sgputting_round
	SGputt_df.loc[n, 'date'] = date
	n = n + 1

#def CheckDuplicates(my_list):
#	if len(my_list) == len(set(my_list)):
#		return False
#	else:
#		return True

#result = CheckDuplicates(my_list)

#if result:
#	print('Duplicates')
#else:
#	print('No Duplicates')

score_df['date']=pd.to_datetime(score_df['date'])
score_df.sort_values(by=['date'], inplace=True, ascending=True)	
writer = pd.ExcelWriter('GolfKPI.xlsx', engine = 'xlsxwriter')
score_df.to_excel(writer, sheet_name = 'Scores')

gir_df['date']=pd.to_datetime(gir_df['date'])
gir_df.sort_values(by=['date'], inplace=True, ascending=True)	
gir_df.to_excel(writer, sheet_name = 'GIR')

fwy_df['date']=pd.to_datetime(fwy_df['date'])
fwy_df.sort_values(by=['date'], inplace=True, ascending=True)	
fwy_df.to_excel(writer, sheet_name = 'Fairways Hit')

scrm_df['date']=pd.to_datetime(scrm_df['date'])
scrm_df.sort_values(by=['date'], inplace=True, ascending=True)	
scrm_df.to_excel(writer, sheet_name = 'Scrambling %')

SGputt_df['date']=pd.to_datetime(SGputt_df['date'])
SGputt_df.sort_values(by=['date'], inplace=True, ascending=True)	
SGputt_df.to_excel(writer, sheet_name = 'Strokes Gained Putting')

sgputting_df['date']=pd.to_datetime(sgputting_df['date'])
sgputting_df.sort_values(by=['date'], inplace=True, ascending=True)	
sgputting_df.to_excel(writer, sheet_name = 'Strokes Gained Putting per hole')

writer.save()