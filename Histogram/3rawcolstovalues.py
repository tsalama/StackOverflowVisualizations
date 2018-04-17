import csv
import math

with open('master2.csv') as inp, open('postproc.csv', 'wb') as out:
	writer = csv.writer(out)
	for row in csv.reader(inp):
		numchars  = len(row[1]) - row[1].count(' ')
		numtags = len(row[3].split())
		if row[2] != '':
			replog1p = round(math.log1p(int(row[2])))
		else:
			replog1p = 0
		writer.writerow([row[0], numchars, numtags, row[2], replog1p])
