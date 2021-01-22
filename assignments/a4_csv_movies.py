'''
Assignment 4: CSV Movies

Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] and write them to a CSV file. The data from each list should be a row in the file, with each item in the list separated by a comma.

'''

import csv


rows = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]


with open('testcsv.csv','w') as f:

    writer = csv.writer(f, delimiter=',')

    for i in range(len(rows)):

        writer.writerow(rows[i])