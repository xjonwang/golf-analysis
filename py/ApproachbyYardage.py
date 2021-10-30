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
n = 0
result_list = ['Result_1', 'Result_2', 'Result_3', 'Result_4', 'Result_5', 'Result_6', 'Result_7', 'Result_8', 'Result_9']
tohole_list = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4', 'To_Hole5', 'To_Hole6', 'To_Hole7', 'To_Hole8', 'To_Hole9']
unit_list = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
distance_list = [50, 75, 100, 125, 150, 175, 200, 225, 250]
SG5075 = SG75100 = SG100125 = SG125150 = SG150175 = SG175200 = SG200225 = SG225250 = pd.DataFrame(columns = ['date', 'Strokes Gained Approach'])
sgapproach_list = [SG5075, SG75100, SG100125, SG125150, SG150175, SG175200, SG200225, SG225250]
for date in tournament_dates_list:
	round = pd.DataFrame(golf.loc[golf.Date == date])
	if len(round) == 18:
		for num in range(0, 18):
			hole = round.iloc[num]
			if hole['Par'] == 3:
				for c in range(0, 8):
					a = int(distance_list[c])
					b = int(distance_list[c + 1])
					sgapproach_df = sgapproach_list[c]
					if hole['Yard'] > a and hole['Yard'] <= b:
						print("made it")
						distance = float(hole['Yard'])
						result2 = 'Result_1'
						nextdistance = float(hole['To_Hole1'])
						expect_approach = pd.DataFrame(expected_tee.loc[expected_tee.Distance == distance])
						expect_approach = float(expect_approach.Shots)
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
						continue
			else: 
				for c in range(0,9):
					tohole = tohole_list[c]
					unit = unit_list[c]
					if float(hole[tohole]) >= 50:
						if hole[unit] == 'Yard':
							for n in range(0, 8):
								a = int(distance_list[n])
								b = int(distance_list[n + 1])
								sgapproach_df = sgapproach_list[n]
								if hole['Yard'] > a and hole['Yard'] <= b:
									distance_approach = float(hole[tohole])
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
										expect_approach = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_approach])
										expect_approach = float(expect_approach.Shots)
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
											if nextdistance == distance_around:
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
												if nextdistance == distance_around:
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
											if nextdistance == distance_around:
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
												if nextdistance == distance_around:
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
											if nextdistance == distance_around:
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
												if nextdistance == distance_around:
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
											if nextdistance == distance_around:
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
												if nextdistance == distance_around:
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
											if nextdistance == distance_around:
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
									elif hole[result] == "OB":
										expect_approach = pd.DataFrame(expected_fairway.loc[expected_fairway.Distance == distance_approach])
										expect_approach = float(expect_approach.Shots)
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
											if nextdistance == distance_around:
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

SGApproachbyYardage = pd.DataFrame(columns = ['Yardage', 'Strokes Gained Approach'])
n = 0
for df in sgapproach_list:
	SGaverage = df.mean()
	print(df)
	print(SGaverage)
	SGApproachbyYardage.loc[n, 'Strokes Gained Approach'] = SGaverage
	n = n + 1
print(SGApproachbyYardage)