import csv
import matplotlib.pyplot as pt
import numpy as np
from scipy.interpolate import make_interp_spline

# 讀取成功路128號之電費帳單資料，共計25筆。
with open('06-51-1452-20-1.txt') as infile:
	rows = csv.reader(infile)
	a1, b1 = [], []
	for row in rows:
		a1.append((int(row[0])-100)*12 + int(row[1]))
		b1.append(int(row[3]))

# 讀取成功路130號之電費帳單資料，共計25筆。
with open('06-51-1451-10-8.txt') as infile:
	rows = csv.reader(infile)
	a2, b2 = [], []
	for row in rows:
		a2.append((int(row[0])-100)*12 + int(row[1]))
		b2.append(int(row[3]))

# 須將橫軸資料由小至大排列，而對應之縱軸資料亦隨之改變。
a1.reverse()
b1.reverse()
a2.reverse()
b2.reverse()

x1 = np.linspace(min(a1), max(a1), 200)
y1 = make_interp_spline(a1, b1, k=3)(x1)
x2 = np.linspace(min(a2), max(a2), 200)
y2 = make_interp_spline(a2, b2, k=3)(x2)

pt.title("2011–2014 Household Power Consumption")
pt.xlabel("Count of Elapsed Months")
pt.ylabel("Units of Electricity Consumed")
pt.plot(x1, y1, 'k--', label="_nolegend_")
pt.plot(x2, y2, 'k--', label="_nolegend_")
pt.plot(a1, b1, 'yo', label="128")
pt.plot(a2, b2, 'co', label="130")
pt.legend(loc="upper center")
pt.show()
