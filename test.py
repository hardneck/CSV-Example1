import csv

with open('06-51-1452-20-1.txt') as infile:
	rows = csv.reader(infile)
	a1, b1 = [], []
	for row in rows:
		a1.append((int(row[0])-100)*12 + int(row[1]))
		b1.append(int(row[3]))

with open('06-51-1451-10-8.txt') as infile:
	rows = csv.reader(infile)
	a2, b2 = [], []
	for row in rows:
		a2.append((int(row[0])-100)*12 + int(row[1]))
		b2.append(int(row[3]))

import matplotlib.pyplot as pt
import numpy as np
from scipy.interpolate import make_interp_spline

a1.reverse()
b1.reverse()
a2.reverse()
b2.reverse()

x1 = np.array(a1)
y1 = np.array(b1)
x2 = np.array(a2)
y2 = np.array(b2)

s1 = np.linspace(x1.min(), x1.max(), 200)
t1 = make_interp_spline(x1, y1, k=3)(s1)
s2 = np.linspace(x2.min(), x2.max(), 200)
t2 = make_interp_spline(x2, y2, k=3)(s2)

pt.title("2011–2014 Household Power Consumption")
pt.xlabel("Count of Elapsed Months")
pt.ylabel("Units of Consumed Electricity")
pt.plot(s1, t1, 'k--')
pt.plot(s2, t2, 'm--')
pt.plot(x1, y1, 'yo')
pt.plot(x2, y2, 'co')
pt.legend(["128", "130"], loc="upper center")
pt.show()
