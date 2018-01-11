import csv
import datetime
file = open('학급문고.csv', encoding='utf8')
data = csv.reader(file)
head = next(data)
data = list(data)
file.close()

def printlib():

while True:
