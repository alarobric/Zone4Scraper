# Parses Zone4 csv result output
# File format uses a base header, and then category header adding extra columns,
#   then racers, then a new line to separate categories.abs
# Categories may have different numbers of fields for differing numbers of laps.abs
#
# TODO
# Parse header and support differing column orderings - check if necessary in other races
# Support laps and multiple numbers of laps
# Console control of output by category, top 3-6, last 3-6
# Support reading file multiple times, updating records and working out which are new changes
# Write output to file for scoreboard. Support fixed width of scoreboard.

import csv

class Category(object):
    """Defines a result category"""
    def __init__(self, name):
        self.name = name

class Racer(object):
    """Defines a racer and results"""
    status = None
    time = None
    finish = None
    rank = None

    def __init__(self, bib, firstname, lastname, status):
        self.bib = bib
        self.firstname = firstname
        self.lastname = lastname
        self.status = status if status else None

    def __str__(self):
        ret = 'Racer %d - %s %s' % (self.bib, self.firstname, self.lastname)
        if self.status is not None:
            ret += ' - ' + self.status
        if self.time is not None:
            ret += ' - ' + self.time
        if self.finish is not None:
            ret += ' - ' + self.finish
        if self.rank is not None:
            ret += ' - ' + self.rank
        return ret

def parse_header(row):
    for field in row:
        print(field)

    print('Done\n')

def parse_category(row):
    name = row[0]
    print('New category: ', name)
    return Category(name)

def parse_racer(row):
    bib = int(row[1]) if row[1] else -1
    time = row[2]
    status = row[3]
    firstname = row[4]
    lastname = row[5]
    finish = row[-2]
    rank = row[-1]
    racer = Racer(bib, firstname, lastname, status)
    if time:
        racer.time = time
    if finish:
        racer.finish = finish
    if rank:
        racer.rank = rank
    print(racer)

def parse_csv(filename):
    with open(filename, newline='') as csvfile:
        result_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        header = False
        category = None
        for row in result_reader:
            if not header:
                parse_header(row)
                header = True
            elif row:
                print('Empty row')
                category = None
            elif category is None:
                category = parse_category(row)
            else:
                parse_racer(row)
                #print('zz'.join(row))
                print(row)

parse_csv('test_results.csv')
