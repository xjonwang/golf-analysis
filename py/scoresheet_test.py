import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib import pylab
import scipy.stats as stats
import random
#import xlrd
golf = pd.read_csv(r'C:\Users\Jon Wang\Downloads\scoresheet_test - Sheet1.csv')
np_golf = np.array(golf)

golf_u1f = pd.DataFrame(golf.loc[golf.Unit_1 == 'FT'])
golf_u2f = pd.DataFrame(golf.loc[golf.Unit_2 == 'FT'])
golf_u3f = pd.DataFrame(golf.loc[golf.Unit_3 == 'FT'])
golf_u12f = golf_u1f.append(golf_u2f)
golf_u123f = golf_u12f.append(golf_u3f)
golf_ft = golf_u123f.drop_duplicates()
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
golf_puttshot = ['To_Hole1', 'To_Hole2', 'To_Hole3', 'To_Hole4', 'To_Hole5', 'To_Hole6', 'To_Hole7', 'To_Hole8', 'To_Hole9']
golf_puttunit = ['Unit_1', 'Unit_2', 'Unit_3', 'Unit_4', 'Unit_5', 'Unit_6', 'Unit_7', 'Unit_8', 'Unit_9']
def putting_distances(f, a, b):
	golf_putt1 = pd.DataFrame(f.loc[f.To_Hole1 <= a])
	golf_puttd1 = pd.DataFrame(golf_putt1.loc[golf_putt1.To_Hole1 > b])
	golf_puttdistance1 = pd.DataFrame(golf_puttd1.loc[golf_puttd1.Unit_1 == 'FT'])
	golf_puttdistance1m = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_2 == 'Made'])
	golf_puttdistance1mi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_3 == 'Made'])
	golf_puttdistance1mimi = pd.DataFrame(golf_puttdistance1.loc[golf_puttdistance1.Result_4 == 'Made'])
	golf_putt2 = pd.DataFrame(f.loc[f.To_Hole2 <= a])
	golf_puttd2 = pd.DataFrame(golf_putt2.loc[golf_putt2.To_Hole2 > b])
	golf_puttdistance2 = pd.DataFrame(golf_puttd2.loc[golf_puttd2.Unit_2 == 'FT'])
	golf_puttdistance2m = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_3 == 'Made'])
	golf_puttdistance2mi = pd.DataFrame(golf_puttdistance2.loc[golf_puttdistance2.Result_4 == 'Made'])
	golf_putt3 = pd.DataFrame(f.loc[f.To_Hole3 <= a])
	golf_puttd3 = pd.DataFrame(golf_putt3.loc[golf_putt3.To_Hole3 > b])
	golf_puttdistance3 = pd.DataFrame(golf_puttd3.loc[golf_puttd3.Unit_3 == 'FT'])
	golf_puttdistance3m = pd.DataFrame(golf_puttdistance3.loc[golf_puttdistance3.Result_4 == 'Made'])
	golf_puttlength = len(golf_puttdistance1) + len(golf_puttdistance2) + len(golf_puttdistance3) 
	print(golf_puttlength, '1')
	golf_1putt = len(golf_puttdistance1m) + len(golf_puttdistance2m) + len(golf_puttdistance3m) 
	golf_2putt = len(golf_puttdistance1mi) + len(golf_puttdistance2mi) 
	golf_3putt = len(golf_puttdistance1mimi) 
	golf_1puttp = golf_1putt/golf_puttlength
	golf_2puttp = golf_2putt/golf_puttlength 
	golf_3puttp = golf_3putt/golf_puttlength
	#print('1 putt percentage:', golf_1putt/golf_puttlength)
	#print('2 putt percentage:', golf_2putt/golf_puttlength)
	#print('3 putt percentage:', golf_3putt/golf_puttlength)
	golf_puttrange = np.array([golf_1puttp, golf_2puttp, golf_3puttp])
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


chipping_1520improvement = [chipping_1520yp, chipping_1520yp1, chipping_1520yp2, chipping_1520yp3, chipping_1520yp4]
chipping_2025improvement = [chipping_2025yp, chipping_2025yp1, chipping_2025yp2, chipping_2025yp3, chipping_2025yp4]
chipping_2530improvement = [chipping_2530yp, chipping_2530yp1, chipping_2530yp2, chipping_2530yp3, chipping_2530yp4]
chipping_3035improvement = [chipping_3035yp, chipping_3035yp1, chipping_3035yp2, chipping_3035yp3, chipping_3035yp4]
chipping_3540improvement = [chipping_3540yp, chipping_3540yp1, chipping_3540yp2, chipping_3540yp3, chipping_3540yp4]
chipping_4050improvement = [chipping_4050yp, chipping_4050yp1, chipping_4050yp2, chipping_4050yp3, chipping_4050yp4]
chipping_5060improvement = [chipping_5060yp, chipping_5060yp1, chipping_5060yp2, chipping_5060yp3, chipping_5060yp4]
score_5i1 = np.array([])
score_5i2 = np.array([])
score_5i3 = np.array([])
score_5i4 = np.array([])
score_5i5 = np.array([])
golf_score = [score_5i1, score_5i2, score_5i3, score_5i4, score_5i5]
game_num = (0, 1, 2, 3, 4)
game_num2 = (0, 1, 2, 3, 4)
for x in game_num:
	for y in game_num2:
		a = golf_5iimprovement
		b = chipping_1520improvement[x]
		c = chipping_2025improvement[y]
		d = chipping_2530improvement[y]
		e = chipping_3035improvement[y]
		f = chipping_3540improvement[y]
		g = chipping_4050improvement[y]
		h = chipping_5060improvement[y]
		i = golf_ft03
		j = golf_ft45
		k = golf_ft68
		l = golf_ft912
		m = golf_ft1317
		n = golf_ft1825
		o = golf_ft2635
		p = golf_ft3645
		golf_scoreimprovement = score_percentage(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
		golf_score[x] = np.append(golf_score[x], golf_scoreimprovement)
		
score_5i1chp1 = golf_score1[0]
print(score_5i1chp1, 'both normal')
print(np.sum(score_5i1chp1))
score_5i1chp2 = golf_score1[1]
print(score_5i1chp2, '5i normal, chip 10%')
print(np.sum(score_5i1chp2))
score_5i1chp3 = golf_score1[2]
print(score_5i1chp3, '5i normal, chip 20%')
print(np.sum(score_5i1chp3))
score_5i1chp4 = golf_score1[3]
print(score_5i1chp4, '5i normal, chip 30%')
print(np.sum(score_5i1chp4))
score_5i1chp5 = golf_score1[4]
print(score_5i1chp5, '5i normal, chip 40%')
print(np.sum(score_5i1chp5))
score_5i2chp1 = golf_score1[5]
print(score_5i2chp1, '5i 10%, chip normal')
print(np.sum(score_5i2chp1))
score_5i2chp2 = golf_score1[6]
print(score_5i2chp2, '5i 10%, chip 10%')
print(np.sum(score_5i2chp2))
score_5i2chp3 = golf_score1[7]
print(score_5i2chp3, '5i 10%, chip 20%')
print(np.sum(score_5i2chp3))
score_5i2chp4 = golf_score1[8]
print(score_5i2chp4, '5i 10%, chip 30%')
print(np.sum(score_5i2chp4))
score_5i2chp5 = golf_score1[9]
print(score_5i2chp5, '5i 10%, chip 40%')
print(np.sum(score_5i2chp5))
score_5i3chp1 = golf_score1[10]
print(score_5i3chp1, '5i 20%, chip normal')
print(np.sum(score_5i3chp1))
score_5i3chp2 = golf_score1[11]
print(score_5i3chp2, '5i 20%, chip 10%')
print(np.sum(score_5i3chp2))
score_5i3chp3 = golf_score1[12]
print(score_5i3chp3, '5i 20%, chip 20%')
print(np.sum(score_5i3chp3))
score_5i3chp4 = golf_score1[13]
print(score_5i3chp4, '5i 20%, chip 30%')
print(np.sum(score_5i3chp4))
score_5i3chp5 = golf_score1[14]
print(score_5i3chp5, '5i 20%, chip 40%')
print(np.sum(score_5i3chp5))
score_5i4chp1 = golf_score1[15]
print(score_5i4chp1, '5i 30%, chip normal')
print(np.sum(score_5i4chp1))
score_5i4chp2 = golf_score1[16]
print(score_5i4chp2, '5i 30%, chip 10%')
print(np.sum(score_5i4chp2))
score_5i4chp3 = golf_score1[17]
print(score_5i4chp3, '5i 30%, chip 20%')
print(np.sum(score_5i3chp3))
score_5i4chp4 = golf_score1[18]
print(score_5i4chp4, '5i 30%, chip 30%')
print(np.sum(score_5i4chp4))
score_5i4chp5 = golf_score1[19]
print(score_5i4chp5, '5i 30%, chip 40%')
print(np.sum(score_5i4chp5))
score_5i5chp1 = golf_score1[20]
print(score_5i5chp1, '5i 40%, chip normal')
print(np.sum(score_5i5chp1))
score_5i5chp2 = golf_score1[21]
print(score_5i5chp2, '5i 40%, chip 10%')
print(np.sum(score_5i5chp2))
score_5i5chp3 = golf_score1[22]
print(score_5i5chp3, '5i 40%, chip 20%')
print(np.sum(score_5i5chp3))
score_5i5chp4 = golf_score1[23]
print(score_5i5chp4, '5i 40%, chip 30%')
print(np.sum(score_5i5chp4))
score_5i5chp5 = golf_score1[24]
print(score_5i5chp5, '5i 40%, chip 40%')
print(np.sum(score_5i5chp5))

golf_a3 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 3])
	golf_a5 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 5])
	golf_a45 = pd.DataFrame(golf_a5.loc[golf_a5.proximity > 3])
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
	golf_a451 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 45])
	golf_a3645 = pd.DataFrame(golf_a451.loc[golf_a451.proximity > 35])
	golf_a60 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 60])
	golf_a4660 = pd.DataFrame(golf_a60.loc[golf_a60.proximity > 45])
	golf_a75 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 75])
	golf_a6175 = pd.DataFrame(golf_a75.loc[golf_a75.proximity > 60])
	golf_a90 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 90])
	golf_a7690 = pd.DataFrame(golf_a90.loc[golf_a90.proximity > 75])
	golf_a105 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 105])
	golf_a91105 = pd.DataFrame(golf_a105.loc[golf_a105.proximity > 90])
	golf_a120 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 120])
	golf_a106120 = pd.DataFrame(golf_a120.loc[golf_a120.proximity > 105])
	golf_a150 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 150])
	golf_a121150 = pd.DataFrame(golf_a150.loc[golf_a150.proximity > 120])
	golf_a180 = pd.DataFrame(golf_aoof.loc[golf_aoof.proximity <= 180])
	golf_a151180 = pd.DataFrame(golf_a180.loc[golf_a180.proximity > 150])
	golf_a03p = len(golf_a3)/len(golf_aoof)
	golf_a45p = len(golf_a45)/len(golf_aoof)
	golf_a68p = len(golf_a68)/len(golf_aoof)
	golf_a912p = len(golf_a912)/len(golf_aoof)
	golf_a1317p = len(golf_a1317)/len(golf_aoof)
	golf_a1825p = len(golf_a1825)/len(golf_aoof)
	golf_a2635p = len(golf_a2635)/len(golf_aoof) 
	golf_a3645p = len(golf_a3645)/len(golf_aoof)
	golf_a4660p = len(golf_a4660)/len(golf_aoof) 
	golf_a6175p = len(golf_a6175)/len(golf_aoof) 
	golf_a7690p = len(golf_a7690)/len(golf_aoof) 
	golf_a91105p = len(golf_a91105)/len(golf_aoof) 
	golf_a106120p = len(golf_a106120)/len(golf_aoof)
	golf_a121150p = len(golf_a121150)/len(golf_aoof)
	golf_a151180p = len(golf_a151180)/len(golf_aoof)