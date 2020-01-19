# -*- coding: utf-8 -*-
def printSeasonRecords(name, line):
    labels = ["QC13", "QC12", "QC11", "QC10", "QC9", "WC8", "WCVII"]
    years = ["2019 - 2020", "2018 - 2019", "2017 - 2018", "2016 - 2017", "2015 - 2016", "2014 - 2015", "2013 - 2014"]
    year_divs = [line.find(x) for x in years]
    for x in range(len(year_divs) - 1):
        if year_divs[x + 1] == -1:
            wins = line.count("won", year_divs[x])
            wins = wins / 2
            losses = line.count("lost", year_divs[x])
            losses = losses / 2
            if wins >= 0:
                print(name + " " + str(labels[x]) + " " + str(wins) + " - " + str(losses))
            break
        else:
            wins = line.count("won", year_divs[x], year_divs[x + 1])
            wins = wins / 2
            losses = line.count("lost", year_divs[x], year_divs[x + 1])
            losses = losses / 2
            if wins >= 0:
                print(name + " " + str(labels[x]) + " " + str(wins) + " - " + str(losses))
    return True

file = open("urls.txt", "r")
lines = file.readlines()
for l in lines:
    if l[0] == 'o':
        name = l[8:-2];
        html_file = open(name, "r")
        html_lines = html_file.readlines()
        printSeasonRecords(name[:-5], html_lines[266])
        html_file.close()
file.close()




# on line 267 of each file, count the number of instances of 'won' and 'lost'
# for each year and divide by 2 to get record
# Years: 2013 - 2014 thru 2019 - 2020
