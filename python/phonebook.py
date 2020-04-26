from sys import exit
import csv

file = open("phonedictionary.csy", "a")

name = input(" Enter you name :")
number = input(" Enter your number :")

writer = csv.writer(file)
writer.writerow((name,number))

file.close()
