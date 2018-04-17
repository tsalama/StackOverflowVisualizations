import csv
with open('master.csv', 'rb') as inp, open('accepted_answers.csv', 'wb') as out:
    writer = csv.writer(out)
    writer.writerow(["type", "vote", "reputation", "accept_rate"])
    for row in csv.reader(inp):
        if row[0] == "accepted-answer":
            writer.writerow(row)