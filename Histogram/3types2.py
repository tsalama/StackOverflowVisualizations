import csv
with open('postproc.csv', 'rb') as inp, open('acceptedanswers2.csv', 'wb') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
        if row[0] == "accepted-answer":
            writer.writerow(row)