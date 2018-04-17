import csv
import collections

# Num Tags
# Log Reputation

# ---FREQUENCIES---

# --QUESTIONS--
# Num Chars
q_chars = collections.Counter()
# with open('questions2.csv') as inp, open('questions_char_frequency_raw.csv', 'wb') as out:
# 	writer = csv.writer(out)
# 	for row in csv.reader(inp):
# 		q_chars.update({row[0]: 1})
		
# 	for value, frequency in q_chars.most_common():
# 		writer.writerow([value, frequency])

# bins = {'1-50':0, '51-100':0, '101-150':0, '151-200':0, '201-250':0, '251-300':0, '301-350':0, '351-400':0, '401-450':0, '451-500':0, '501-550':0, '551-600':0, '601-650':0, '651-700':0, '701-750':0, '751-800':0, '801-850':0, '851-900':0, '901-950':0, '951-1000':0, '1001+':0}
# with open('questions_char_frequency_raw.csv') as inp, open('questions_char_frequency.csv', 'wb') as out:
# 	writer = csv.writer(out)
# 	writer.writerow(["value", "frequency"])
# 	for row in csv.reader(inp):
# 		val = int(row[0])
# 		if val >= 1 and val < 50:
# 			bins['1-50'] += int(row[1])
# 		elif val >= 51 and val <= 100:
# 			bins['51-100'] += int(row[1])
# 		elif val >= 101 and val <= 150:
# 			bins['101-150'] += int(row[1])
# 		elif val >= 151 and val <= 200:
# 			bins['151-200'] += int(row[1])
# 		elif val >= 201 and val <= 250:
# 			bins['201-250'] += int(row[1])
# 		elif val >= 251 and val <= 300:
# 			bins['251-300'] += int(row[1])
# 		elif val >= 301 and val <= 350:
# 			bins['301-350'] += int(row[1])
# 		elif val >= 351 and val <= 400:
# 			bins['351-400'] += int(row[1])
# 		elif val >= 401 and val <= 450:
# 			bins['401-450'] += int(row[1])
# 		elif val >= 451 and val <= 500:
# 			bins['451-500'] += int(row[1])
# 		elif val >= 501 and val <= 550:
# 			bins['501-550'] += int(row[1])
# 		elif val >= 551 and val <= 600:
# 			bins['551-600'] += int(row[1])
# 		elif val >= 601 and val <= 650:
# 			bins['601-650'] += int(row[1])
# 		elif val >= 651 and val <= 700:
# 			bins['651-700'] += int(row[1])
# 		elif val >= 701 and val <= 750:
# 			bins['701-750'] += int(row[1])
# 		elif val >= 751 and val <= 800:
# 			bins['751-800'] += int(row[1])
# 		elif val >= 801 and val <= 850:
# 			bins['801-850'] += int(row[1])
# 		elif val >= 851 and val <= 900:
# 			bins['851-900'] += int(row[1])
# 		elif val >= 901 and val <= 950:
# 			bins['901-950'] += int(row[1])
# 		elif val >= 951 and val <= 1000:
# 			bins['951-1000'] += int(row[1])
# 		elif val >= 1001 and val <= 100000:
# 			bins['1001+'] += int(row[1])			
# 	for key in bins.iterkeys():
# 		writer.writerow([key, bins[key]])
		
# Num Tags
q_tags = collections.Counter()
with open('questions2.csv') as inp, open('questions_tags_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		q_tags.update({row[1]: 1})
		
	for value, frequency in q_tags.most_common():
		writer.writerow([value, frequency])

# Log Reputation
q_rep = collections.Counter()
with open('questions2.csv') as inp, open('questions_rep_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		q_rep.update({row[3]: 1})
		
	for value, frequency in q_rep.most_common():
		writer.writerow([value, frequency])


# --ANSWERS--
# Num Chars
ans_chars = collections.Counter()
with open('answers2.csv') as inp, open('answers_char_frequency_raw.csv', 'wb') as out:
	writer = csv.writer(out)
	for row in csv.reader(inp):
		ans_chars.update({row[0]: 1})
		
	for value, frequency in ans_chars.most_common():
		writer.writerow([value, frequency])

bins = {'1-50':0, '51-100':0, '101-150':0, '151-200':0, '201-250':0, '251-300':0, '301-350':0, '351-400':0, '401-450':0, '451-500':0, '501-550':0, '551-600':0, '601-650':0, '651-700':0, '701-750':0, '751-800':0, '801-850':0, '851-900':0, '901-950':0, '951-1000':0, '1001+':0}
with open('answers_char_frequency_raw.csv') as inp, open('answers_char_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		val = int(row[0])
		if val >= 1 and val < 50:
			bins['1-50'] += int(row[1])
		elif val >= 51 and val <= 100:
			bins['51-100'] += int(row[1])
		elif val >= 101 and val <= 150:
			bins['101-150'] += int(row[1])
		elif val >= 151 and val <= 200:
			bins['151-200'] += int(row[1])
		elif val >= 201 and val <= 250:
			bins['201-250'] += int(row[1])
		elif val >= 251 and val <= 300:
			bins['251-300'] += int(row[1])
		elif val >= 301 and val <= 350:
			bins['301-350'] += int(row[1])
		elif val >= 351 and val <= 400:
			bins['351-400'] += int(row[1])
		elif val >= 401 and val <= 450:
			bins['401-450'] += int(row[1])
		elif val >= 451 and val <= 500:
			bins['451-500'] += int(row[1])
		elif val >= 501 and val <= 550:
			bins['501-550'] += int(row[1])
		elif val >= 551 and val <= 600:
			bins['551-600'] += int(row[1])
		elif val >= 601 and val <= 650:
			bins['601-650'] += int(row[1])
		elif val >= 651 and val <= 700:
			bins['651-700'] += int(row[1])
		elif val >= 701 and val <= 750:
			bins['701-750'] += int(row[1])
		elif val >= 751 and val <= 800:
			bins['751-800'] += int(row[1])
		elif val >= 801 and val <= 850:
			bins['801-850'] += int(row[1])
		elif val >= 851 and val <= 900:
			bins['851-900'] += int(row[1])
		elif val >= 901 and val <= 950:
			bins['901-950'] += int(row[1])
		elif val >= 951 and val <= 1000:
			bins['951-1000'] += int(row[1])
		elif val >= 1001 and val <= 100000:
			bins['1001+'] += int(row[1])			
	for key in bins.iterkeys():
		writer.writerow([key, bins[key]])		

# Num Tags
ans_tags = collections.Counter()
with open('answers2.csv') as inp, open('answers_tags_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		ans_tags.update({row[1]: 1})
		
	for value, frequency in ans_tags.most_common():
		writer.writerow([value, frequency])

# Log Reputation
ans_rep = collections.Counter()
with open('answers2.csv') as inp, open('answers_rep_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		ans_rep.update({row[3]: 1})
		
	for value, frequency in ans_rep.most_common():
		writer.writerow([value, frequency])


# --ACCEPTED ANSWERS--
# Num Chars
acc_ans_chars = collections.Counter()
with open('acceptedanswers2.csv') as inp, open('acc_answers_char_frequency_raw.csv', 'wb') as out:
	writer = csv.writer(out)
	for row in csv.reader(inp):
		acc_ans_chars.update({row[0]: 1})
		
	for value, frequency in acc_ans_chars.most_common():
		writer.writerow([value, frequency])

bins = {'1-50':0, '51-100':0, '101-150':0, '151-200':0, '201-250':0, '251-300':0, '301-350':0, '351-400':0, '401-450':0, '451-500':0, '501-550':0, '551-600':0, '601-650':0, '651-700':0, '701-750':0, '751-800':0, '801-850':0, '851-900':0, '901-950':0, '951-1000':0, '1001+':0}
with open('acc_answers_char_frequency_raw.csv') as inp, open('acc_answers_char_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		val = int(row[0])
		if val >= 1 and val < 50:
			bins['1-50'] += int(row[1])
		elif val >= 51 and val <= 100:
			bins['51-100'] += int(row[1])
		elif val >= 101 and val <= 150:
			bins['101-150'] += int(row[1])
		elif val >= 151 and val <= 200:
			bins['151-200'] += int(row[1])
		elif val >= 201 and val <= 250:
			bins['201-250'] += int(row[1])
		elif val >= 251 and val <= 300:
			bins['251-300'] += int(row[1])
		elif val >= 301 and val <= 350:
			bins['301-350'] += int(row[1])
		elif val >= 351 and val <= 400:
			bins['351-400'] += int(row[1])
		elif val >= 401 and val <= 450:
			bins['401-450'] += int(row[1])
		elif val >= 451 and val <= 500:
			bins['451-500'] += int(row[1])
		elif val >= 501 and val <= 550:
			bins['501-550'] += int(row[1])
		elif val >= 551 and val <= 600:
			bins['551-600'] += int(row[1])
		elif val >= 601 and val <= 650:
			bins['601-650'] += int(row[1])
		elif val >= 651 and val <= 700:
			bins['651-700'] += int(row[1])
		elif val >= 701 and val <= 750:
			bins['701-750'] += int(row[1])
		elif val >= 751 and val <= 800:
			bins['751-800'] += int(row[1])
		elif val >= 801 and val <= 850:
			bins['801-850'] += int(row[1])
		elif val >= 851 and val <= 900:
			bins['851-900'] += int(row[1])
		elif val >= 901 and val <= 950:
			bins['901-950'] += int(row[1])
		elif val >= 951 and val <= 1000:
			bins['951-1000'] += int(row[1])
		elif val >= 1001 and val <= 100000:
			bins['1001+'] += int(row[1])			
	for key in bins.iterkeys():
		writer.writerow([key, bins[key]])		

# Num Tags
acc_ans_tags = collections.Counter()
with open('acceptedanswers2.csv') as inp, open('acc_answers_tags_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		acc_ans_tags.update({row[1]: 1})
		
	for value, frequency in acc_ans_tags.most_common():
		writer.writerow([value, frequency])

# Log Reputation
acc_ans_rep = collections.Counter()
with open('acceptedanswers2.csv') as inp, open('acc_answers_rep_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["value", "frequency"])
	for row in csv.reader(inp):
		acc_ans_rep.update({row[3]: 1})
		
	for value, frequency in acc_ans_rep.most_common():
		writer.writerow([value, frequency])

