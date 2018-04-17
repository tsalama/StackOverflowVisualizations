import csv
import collections

# QUESTIONS
# Votes
q_votes = collections.Counter()
with open('questions.csv') as inp, open('questions_vote_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["num_votes", "frequency"])
	for row in csv.reader(inp):
		q_votes.update({row[0]: 1})
		
	for num_votes, count in q_votes.most_common():
		writer.writerow([num_votes, count])
# Acceptance Rates
q_arates = collections.Counter()
with open('questions.csv') as inp, open('questions_arates_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["acceptance_rates", "frequency"])
	for row in csv.reader(inp):
		q_arates.update({row[2]: 1})
		
	for acceptance_rates, count in q_arates.most_common():
		writer.writerow([acceptance_rates, count])

# ANSWERS
# Votes
ans_votes = collections.Counter()
with open('answers.csv') as inp, open('answers_vote_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["num_votes", "frequency"])
	for row in csv.reader(inp):
		ans_votes.update({row[0]: 1})
		
	for num_votes, count in ans_votes.most_common():
		writer.writerow([num_votes, count])
# Acceptance Rates
ans_arates = collections.Counter()
with open('answers.csv') as inp, open('answers_arates_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["acceptance_rates", "frequency"])
	for row in csv.reader(inp):
		ans_arates.update({row[2]: 1})
		
	for acceptance_rates, count in ans_arates.most_common():
		writer.writerow([acceptance_rates, count])

# ACCEPTED ANSWERS
# Votes
ac_ans_votes = collections.Counter()
with open('accepted_answers.csv') as inp, open('accepted_answers_vote_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["num_votes", "frequency"])
	for row in csv.reader(inp):
		ac_ans_votes.update({row[0]: 1})
		
	for num_votes, count in ac_ans_votes.most_common():
		writer.writerow([num_votes, count])
# Acceptance Rates
ac_ans_arates = collections.Counter()
with open('accepted_answers.csv') as inp, open('accepted_answers_arates_frequency.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(["acceptance_rates", "frequency"])
	for row in csv.reader(inp):
		ac_ans_arates.update({row[2]: 1})
		
	for acceptance_rates, count in ac_ans_arates.most_common():
		writer.writerow([acceptance_rates, count])