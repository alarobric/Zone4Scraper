# Parses Zone4 csv result output
# File format uses a base header, and then category header adding extra columns,
#   then racers, then a new line to separate categories.abs
# Categories may have different numbers of fields for differing numbers of laps.abs

import csv

import race_results

class Parser(object):
    def __init__(self, debug=False):
        self.debug = debug
        self.race = None

    def parse_header(self, row):
        if self.debug:
            for field in row:
                print(field)
            print('Done\n')

        if not row[0:7] == ["ï»¿", "rank", "time", "status", "firstname", "lastname", "Bib #"]:
            print(row[0:7])
            print(["ï»¿", "rank", "time", "status", "firstname", "lastname", "Bib #"])
            raise NameError('Invalid columns')

    def parse_category(self, row):
        name = row[0]
        if self.debug:
            print('New category: ', name)

        if not row[-2:] == ["Finish", "(rank)"]:
            print(row[-2:])
            print(["Finish", "(rank)"])
            raise NameError('Invalid category columns')

        return race_results.Category(name)

    def parse_racer(self, row):
        rank = row[1]
        time = row[2]
        status = row[3]
        firstname = row[4]
        lastname = row[5]
        bib = int(row[6]) if row[6] else -1
        finish = row[-2]
        #rank = row[-1]
        racer = race_results.Racer(bib, firstname, lastname, status)
        if time:
            racer.time = time
        if finish:
            racer.finish = finish
        if rank:
            racer.rank = rank

        if self.debug:
            print(racer)

        return racer

    def parse_csv(self, filename):
        with open(filename, newline='') as csvfile:
            #create a race to hold the data
            self.race = race_results.Race(filename)

            #parse the csv line by line
            result_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            header = False
            category = None
            for row in result_reader:
                if not header:
                    self.parse_header(row)
                    header = True
                elif not row:
                    if self.debug:
                        print('Empty row')
                    category = None
                elif category is None:
                    category = self.parse_category(row)
                    self.race.add_category(category)
                else:
                    racer = self.parse_racer(row)
                    category.add_racer(racer)
                    if self.debug:
                        print(row)
        return self.race

if __name__ == '__main__':
    PARSER = Parser(debug=True)
    PARSER.parse_csv('test_results.csv')
