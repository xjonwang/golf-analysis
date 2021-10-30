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
raw_input = input("What other tournaments do you want? ")
tournament_df = pd.DataFrame(golf.loc[golf.Tournament == 'Hurricane']).append(pd.DataFrame(golf.loc[golf.Tournament == 'FJT']))
tournament_df = tournament_df.append(pd.DataFrame(golf.loc[golf.Tournament == 'AJGA']))
tournament_df = tournament_df.append(pd.DataFrame(golf.loc[golf.Tournament == raw_input]))

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
					expect_putt = float(expect_putt.Shots)
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

print(sgputting_df)

SGputt_df = pd.DataFrame(columns = ['date', 'Strokes Gained Putting'])
n = 0
for date in tournament_dates_list:
	sgputting_round = pd.DataFrame(sgputting_df.loc[sgputting_df.date == date])
	sgputting_round = float(sgputting_round['Strokes Gained Putting'].sum())
	SGputt_df.loc[n, 'Strokes Gained Putting'] = sgputting_round
	SGputt_df.loc[n, 'date'] = date
	n = n + 1

n = 0
tohole_list = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4', 'To_Hole5', 'To_Hole6', 'To_Hole7', 'To_Hole8', 'To_Hole9']
unit_list = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
result_list = ['Result_1', 'Result_2', 'Result_3', 'Result_4', 'Result_5', 'Result_6', 'Result_7', 'Result_8', 'Result_9']
sgofftee_df = pd.DataFrame(columns = ['date', 'Strokes Gained Off the Tee'])
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		par45_df = pd.DataFrame(round.loc[round.Par != 3])
		for num in range (0, len(par45_df)):
			hole = par45_df.iloc[num]
			for num in range(-1,9):
				distance = float(hole['Yard'])
				expect_tee = pd.DataFrame(expected_tee.loc[expected_tee.Distance == distance])
				expect_tee = float(expect_tee.Shots)
				if num == -1:
					second_shot_distance = float(hole.To_Hole1)
					second_shot_condition = hole.Result_1
					if second_shot_condition == 'Made':
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Fairway':
						expect_2nd_fwy = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == second_shot_distance])
						expect_2nd_fwy = float(expect_2nd_fwy.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_fwy
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Green':
						expect_2nd_gr = pd.DataFrame(expected_putts.loc[expected_putts.Distance == second_shot_distance])
						expect_2nd_gr = float(expect_2nd_gr.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_gr
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Rough':
						expect_2nd_rgh = pd.DataFrame(expected_rough.loc[expected_rough.Distance == second_shot_distance])
						expect_2nd_rgh = float(expect_2nd_rgh.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_rgh
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Bunker':
						expect_2nd_bnk = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == second_shot_distance])
						expect_2nd_bnk = float(expect_2nd_bnk.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_bnk
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Trees':
						expect_2nd_rec = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == second_shot_distance])
						expect_2nd_rec = float(expect_2nd_rec.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_rec
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
					elif second_shot_condition == 'Water':
						if distance == second_shot_distance:
							expect_2nd_tee = pd.DataFrame(expected_tee.loc[expected_tee.Distance == second_shot_distance])
							expect_2nd_tee = float(expect_2nd_tee.Shots)
							sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_tee
							sgofftee_df.loc[n, 'date'] = date
							n = n + 1
						else:
							expect_2nd_rgh = pd.DataFrame(expected_rough.loc[expected_rough.Distance == second_shot_distance])
							expect_2nd_rgh = float(expect_2nd_rgh.Shots)
							sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_rgh
							sgofftee_df.loc[n, 'date'] = date
							n = n + 1
					elif second_shot_condition == 'OB':
						expect_2nd_tee = pd.DataFrame(expected_tee.loc[expected_tee.Distance == second_shot_distance])
						expect_2nd_tee = float(expect_2nd_tee.Shots)
						sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_tee
						sgofftee_df.loc[n, 'date'] = date
						n = n + 1
				else:
					yard = float(hole['Yard'])
					tohole = tohole_list[num]
					distance = float(hole[tohole])
					unit = unit_list[num]
					if distance == yard and hole[unit] == 'Yard':
						a = int(tohole.replace('To_Hole', ''))
						x = str(a + 1)
						y = str(a + 2)
						result2 = 'Result_' + x
						tohole2 = 'To_Hole' + x
						result3 = 'Result_' + y
						tohole3 = 'To_Hole' + y
						club2 = 'Club_' + x
						second_shot_distance = float(hole[tohole2])
						distance3 = float(hole[tohole3])
						second_shot_condition = hole[result2]
						if distance == yard and hole[unit] == 'Yard':
							if second_shot_condition == 'Made':
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Fairway':
								expect_2nd_fwy = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == second_shot_distance])
								expect_2nd_fwy = float(expect_2nd_fwy.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_fwy
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Green':
								expect_2nd_gr = pd.DataFrame(expected_putts.loc[expected_putts.Distance == second_shot_distance])
								expect_2nd_gr = float(expect_2nd_gr.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_gr
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Rough':
								expect_2nd_rgh = pd.DataFrame(expected_rough.loc[expected_rough.Distance == second_shot_distance])
								expect_2nd_rgh = float(expect_2nd_rgh.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_rgh
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Bunker':
								expect_2nd_bnk = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == second_shot_distance])
								expect_2nd_bnk = float(expect_2nd_bnk.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_bnk
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Trees':
								expect_2nd_rec = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == second_shot_distance])
								expect_2nd_rec = float(expect_2nd_rec.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_2nd_rec
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif second_shot_condition == 'Water':
								if distance == second_shot_distance:
									expect_2nd_tee = pd.DataFrame(expected_tee.loc[expected_tee.Distance == second_shot_distance])
									expect_2nd_tee = float(expect_2nd_tee.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_tee
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_2nd_rgh = pd.DataFrame(expected_rough.loc[expected_rough.Distance == second_shot_distance])
									expect_2nd_rgh = float(expect_2nd_rgh.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_rgh
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
							elif second_shot_condition == 'OB':
								expect_2nd_tee = pd.DataFrame(expected_tee.loc[expected_tee.Distance == second_shot_distance])
								expect_2nd_tee = float(expect_2nd_tee.Shots)
								sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_2nd_tee
								sgofftee_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[club2] == "Penalty":
								if hole[result3] == "Made":
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 1 - expect_next
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if distance3 == distance:
										sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = -2
										sgofftee_df.loc[n, 'date'] = date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = expect_tee - 2 - expect_next
										sgofftee_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgofftee_df.loc[n, 'Strokes Gained Off the Tee'] = -2
									sgofftee_df.loc[n, 'date'] = date
									n = n + 1
					else:
						continue
	else:
		continue

print(sgofftee_df)

SGofftee_df = pd.DataFrame(columns = ['date', 'Strokes Gained Off the Tee'])
n = 0
for date in tournament_dates_list:
	sgofftee_round = pd.DataFrame(sgofftee_df.loc[sgofftee_df.date == date])
	sgofftee_round = float(sgofftee_round['Strokes Gained Off the Tee'].sum())
	SGofftee_df.loc[n, 'Strokes Gained Off the Tee'] = sgofftee_round
	SGofftee_df.loc[n, 'date'] = date
	n = n + 1

n = 0
result_list = ['Result_1', 'Result_2', 'Result_3', 'Result_4', 'Result_5', 'Result_6', 'Result_7', 'Result_8', 'Result_9']
tohole_list = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4', 'To_Hole5', 'To_Hole6', 'To_Hole7', 'To_Hole8', 'To_Hole9']
unit_list = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
sgaroundgreen_df = pd.DataFrame(columns = ['date', 'Strokes Gained Around the Green'])
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		for num in range(0, 18):
			hole = round.iloc[num]
			for c in range(0,9):
				tohole = tohole_list[c]
				unit = unit_list[c]
				if hole[unit] == 'Yard':
					if float(hole[tohole]) <= 50:
						distance_around = float(hole[tohole])
						result = tohole.replace('To_Hole', 'Result_')
						a = int(result.replace('Result_', ''))
						x = str(a + 1)
						y = str(a + 2)
						result2 = 'Result_' + x
						tohole2 = 'To_Hole' + x
						result3 = 'Result_' + y
						tohole3 = 'To_Hole' + y
						club2 = 'Club_' + x
						nextdistance = float(hole[tohole2])
						distance3 = float(hole[tohole3])
						if hole[result] == 'Fairway':
							expect_around = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Water":
								if nextdistance == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result2] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[club2] == "Penalty":
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if distance3 == distance_around:
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
						elif hole[result] == 'Rough':
							expect_around = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Water":
								if nextdistance == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result2] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[club2] == "Penalty":
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if nextdistance == distance_around:
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
						elif hole[result] == 'Bunker':
							expect_around = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Water":
								if nextdistance == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result2] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[club2] == "Penalty":
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if nextdistance == distance_around:
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
						elif hole[result] == 'Trees':
							expect_around = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result2] == "Water":
								if nextdistance == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result2] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[club2] == "Penalty":
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if nextdistance == distance_around:
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
										sgaroundgreen_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
						elif hole[result] == 'Water':	
							expect_around = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Water":
								if distance3 == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result3] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
						elif hole[result] == 'OB':
							expect_around = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_around])
							expect_around = float(expect_around.Shots)
							if hole[result2] == "Made":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Green":
								expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Fairway":
								expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Rough":
								expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Bunker":
								expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Trees":
								expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
								expect_next = float(expect_next.Shots)
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 1 - expect_next
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
							elif hole[result3] == "Water":
								if distance3 == distance_around:
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
								else:
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = expect_around - 2 - expect_next
									sgaroundgreen_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result3] == "OB":
								sgaroundgreen_df.loc[n, 'Strokes Gained Around the Green'] = -2
								sgaroundgreen_df.loc[n, 'date'] = date
								n = n + 1
					else:
						continue
				else:
					continue

print(sgaroundgreen_df)

SGaround_df = pd.DataFrame(columns = ['date', 'Strokes Gained Around the Green'])
n = 0
for date in tournament_dates_list:
	sgaround_round = pd.DataFrame(sgaroundgreen_df.loc[sgaroundgreen_df.date == date])
	sgaround_round = float(sgaround_round['Strokes Gained Around the Green'].sum())
	SGaround_df.loc[n, 'Strokes Gained Around the Green'] = sgaround_round
	SGaround_df.loc[n, 'date'] = date
	n = n + 1

n = 0
result_list = ['Result_1', 'Result_2', 'Result_3', 'Result_4', 'Result_5', 'Result_6', 'Result_7', 'Result_8', 'Result_9']
tohole_list = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4', 'To_Hole5', 'To_Hole6', 'To_Hole7', 'To_Hole8', 'To_Hole9']
unit_list = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
sgapproach_df = pd.DataFrame(columns = ['date', 'Strokes Gained Appraoch'])
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		for num in range(0, 18):
			hole = round.iloc[num]
			if hole['Par'] == 3:
				distance = float(hole['Yard'])
				result2 = 'Result_1'
				nextdistance = float(hole['To_Hole1'])
				expect_approach = pd.DataFrame(expected_tee.loc[expected_tee.Distance == distance])
				expect_approach = float(expect_approach.Shots)
				if hole[result2] == "Made":
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
				if hole[result2] == "Green":
					expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
					expect_next = float(expect_next.Shots)
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
				elif hole[result2] == "Fairway":
					expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
					expect_next = float(expect_next.Shots)
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
					sgapproach_df.loc[n, 'date']= date
					n = n + 1
				elif hole[result2] == "Rough":
					expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
					expect_next = float(expect_next.Shots)
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
				elif hole[result2] == "Bunker":
					expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
					expect_next = float(expect_next.Shots)
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
				elif hole[result2] == "Trees":
					expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
					expect_next = float(expect_next.Shots)
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
				elif hole[result2] == "Water":
					if nextdistance == distance_around:
						sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
						sgapproach_df.loc[n, 'date'] = date
						n = n + 1
					else:
						expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
						expect_next = float(expect_next.Shots)
						sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
						sgapproach_df.loc[n, 'date'] = date
						n = n + 1
				elif hole[result2] == "OB":
					sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
					sgapproach_df.loc[n, 'date'] = date
					n = n + 1
			else: 
				for c in range(0,9):
					tohole = tohole_list[c]
					unit = unit_list[c]
					if float(hole[tohole]) >= 50:
						if hole[unit] == 'Yard':
							distance_approach = float(hole[tohole])
							result = tohole.replace('To_Hole', 'Result_')
							a = int(result.replace('Result_', ''))
							x = str(a + 1)
							y = str(a + 2)
							z = str(a - 1)
							result2 = 'Result_' + x
							tohole2 = 'To_Hole' + x
							result3 = 'Result_' + y
							tohole3 = 'To_Hole' + y
							resultneg1 = 'Result_' + z
							club2 = 'Club_' + x
							nextdistance = float(hole[tohole2])
							distance3 = float(hole[tohole3])
							if hole[result] == 'Fairway':
								expect_approach = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result2] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result2] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result2] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[club2] == "Penalty":
									if hole[result3] == "Green":
										expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Fairway":
										expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Rough":
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Bunker":
										expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Trees":
										expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Water":
										if nextdistance == distance_approach:
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
										else:
											expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
											expect_next = float(expect_next.Shots)
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
									elif hole[result3] == "OB":
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
							elif hole[result] == "Rough":
								expect_approach = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result2] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result2] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result2] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[club2] == "Penalty":
									if hole[result3] == "Green":
										expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Fairway":
										expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Rough":
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Bunker":
										expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Trees":
										expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Water":
										if nextdistance == distance_approach:
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
										else:
											expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
											expect_next = float(expect_next.Shots)
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
									elif hole[result3] == "OB":
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
							elif hole[result] == "Bunker":
								expect_approach = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result2] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result2] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result2] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[club2] == "Penalty":
									if hole[result3] == "Green":
										expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Fairway":
										expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Rough":
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Bunker":
										expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Trees":
										expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Water":
										if nextdistance == distance_approach:
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
										else:
											expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
											expect_next = float(expect_next.Shots)
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
									elif hole[result3] == "OB":
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
							elif hole[result] == "Trees":
								expect_approach = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result2] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result2] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == nextdistance])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result2] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == nextdistance])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result2] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[club2] == "Penalty":
									if hole[result3] == "Green":
										expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Fairway":
										expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Rough":
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Bunker":
										expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Trees":
										expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
									elif hole[result3] == "Water":
										if nextdistance == distance_approach:
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
										else:
											expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
											expect_next = float(expect_next.Shots)
											sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
											sgapproach_df.loc[n, 'date'] = date
											n = n + 1
									elif hole[result3] == "OB":
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
							elif hole[result] == "Water":
								expect_approach = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result3] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
							elif hole[result] == "OB":
								expect_approach = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_approach])
								expect_approach = float(expect_approach.Shots)
								if hole[result3] == "Made":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								if hole[result3] == "Green":
									expect_next = pd.DataFrame(expected_putts.loc[expected_putts.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Fairway":
									expect_next = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Rough":
									expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Bunker":
									expect_next = pd.DataFrame(expected_bunker.loc[expected_bunker.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Trees":
									expect_next = pd.DataFrame(expected_recovery.loc[expected_recovery.Distance == distance3])
									expect_next = float(expect_next.Shots)
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 1 - expect_next
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1
								elif hole[result3] == "Water":
									if nextdistance == distance_approach:
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
										sgapproach_df.loc[n, 'date']= date
										n = n + 1
									else:
										expect_next = pd.DataFrame(expected_rough.loc[expected_rough.Distance == distance3])
										expect_next = float(expect_next.Shots)
										sgapproach_df.loc[n, 'Strokes Gained Approach'] = expect_approach - 2 - expect_next
										sgapproach_df.loc[n, 'date'] = date
										n = n + 1
								elif hole[result3] == "OB":
									sgapproach_df.loc[n, 'Strokes Gained Approach'] = -2
									sgapproach_df.loc[n, 'date'] = date
									n = n + 1

SGapproach_df = pd.DataFrame(columns = ['date', 'Strokes Gained Approach'])
n = 0
for date in tournament_dates_list:
	sgapproach_round = pd.DataFrame(sgapproach_df.loc[sgapproach_df.date == date])
	sgapproach_round = float(sgapproach_round['Strokes Gained Approach'].sum())
	SGapproach_df.loc[n, 'Strokes Gained Approach'] = sgapproach_round
	SGapproach_df.loc[n, 'date'] = date
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

SGofftee_df['date']=pd.to_datetime(SGofftee_df['date'])
SGofftee_df.sort_values(by=['date'], inplace=True, ascending=True)	
SGofftee_df.to_excel(writer, sheet_name = 'Strokes Gained Off the Tee')

SGaround_df['date']=pd.to_datetime(SGaround_df['date'])
SGaround_df.sort_values(by=['date'], inplace=True, ascending=True)	
SGaround_df.to_excel(writer, sheet_name = 'Strokes Gained Around the Green')

SGapproach_df['date']=pd.to_datetime(SGapproach_df['date'])
SGapproach_df.sort_values(by=['date'], inplace=True, ascending=True)	
SGapproach_df.to_excel(writer, sheet_name = 'Strokes Gained Approach')

rolling_score_df = pd.DataFrame(columns = ['date', 'Average Score'])
rolling_gir_df = pd.DataFrame(columns = ['date', 'Average GIR'])
rolling_fwy_df = pd.DataFrame(columns = ['date', 'Average Fairways'])
rolling_scrm_df = pd.DataFrame(columns = ['date', 'Average Scrambling'])
rolling_SGputt_df = pd.DataFrame(columns = ['date', 'Average SG: Putting'])
rolling_SGofftee_df = pd.DataFrame(columns = ['date', 'Average SG: Off Tee'])
rolling_SGaround_df = pd.DataFrame(columns = ['date', 'Average SG: Around the Green'])
rolling_SGapproach_df = pd.DataFrame(columns = ['date', 'Average SG: Approach'])

rolling_KPIlist = [rolling_score_df, rolling_gir_df, rolling_fwy_df, rolling_scrm_df, rolling_SGputt_df, rolling_SGofftee_df, rolling_SGaround_df, rolling_SGapproach_df]
KPIlist = [score_df, gir_df, fwy_df, scrm_df, SGputt_df, SGofftee_df, SGaround_df, SGapproach_df]

n = -1
while n + 5 < len(score_df):
	n = n + 1
	for x in range(0,7):
		kpi = KPIlist[x]
		rolling_kpi = rolling_KPIlist[x]
		column_names = list(rolling_kpi.columns)
		data_name = column_names[1]
		recent5 = kpi.iloc[n:n+5]
		recent5date = recent5.iloc[4,0]
		recent5 = np.array(recent5.iloc[:,1])
		recent5mean = np.mean(recent5)
		rolling_kpi.loc[n, 'date'] = recent5date
		rolling_kpi.loc[n, data_name] = recent5mean

sheetname_list = ['Average Score', 'Average GIR', 'Average Fairways', 'Average Scrambling', 'Average SG Putting', 'Average SG Off Tee', 'Average SG Around the Green', 'Average SG Approach']

for x in range(0,7):
	rolling_kpi = rolling_KPIlist[x]
	sheet_name = sheetname_list[x]
	rolling_kpi.to_excel(writer, sheet_name = sheet_name)

writer.save()