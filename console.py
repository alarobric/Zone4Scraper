import os
import pickle

import csv_parser
import download_csv
import html_parser

NUM_RACERS_OUTPUT = 6
SHARE_FOLDER_PATH = r'C:\Users\Alan\Desktop\scoreboard.txt'

class Console(object):
    racename = 'http://zone4.ca/race/2017-12-17/c6e78e84/2017-haywood-noram-day-3-mass/results/'
    race = None
    category = None
    parser = csv_parser.Parser(True)
    html_parser = None

    def __init__(self):
        pass

    def display_title_bar(self):
        os.system('clear')
        print('\t********************')
        print('\t*** Zone4Scraper ***')
        print('\t********************')

    def main_menu(self):
        print('')
        print('Main menu')
        if self.racename:
            print('Race: ', self.racename)
            print('[s] Adjust race url')
        else:
            print('[s] Setup race name and url')

        if not self.race:
            print('You have no race data - load some?')
            print('[l] Load from pickle')
            print('[p] Download and parse race results as csv')
            print('[k] Parse html results')
        else:
            print('You have %d categories and %d racers loaded'
                  % (self.race.num_categories(), self.race.num_racers()))

        if self.category:
            print('Current category: ', self.category)
        if self.race:
            print('[c] Select a category')

        if self.category:
            print('[o] Output full category')
            print('[t] Output top x results to scoreboard')

        print('[q] to quit')

        return input('What to do? ')

    def setup_race_name(self):
        if self.racename:
            print('Warning: racename is already defined as ', self.racename)
        print('Please enter the racename, or blank to leave as is')
        inp = input('racename: ')
        if inp:
            self.racename = inp

    def parse_race(self):
        print('Going to download the race csv export')
        new_csv = download_csv.download_csv(self.racename)
        print('Got new csv ', new_csv)
        self.race = self.parser.parse_csv(new_csv)

    def parse_race_as_html(self):
        print('Parsing race as html')
        self.html_parser = html_parser.Parser(self.racename, debug=True)
        self.race = self.html_parser.parse_page()
        self.html_parser.quit()

    def select_category(self):
        if not self.race:
            print('You need to parse a race first')
            return

        for i, cat in enumerate(self.race.categories):
            print('%d. %s' % (i+1, cat.name))
        choice = input('Select a category: ')
        choice = int(choice) - 1
        if choice >= len(self.race.categories) or choice < 0:
            print('Invalid choice')
            return
        self.category = self.race.categories[choice]

    def output_racers(self, num_racers_output=0):
        if not self.category:
            print('You need to select a category first')
            return

        if num_racers_output == 0:
            num_racers_output = len(self.category.racers)
        else:
            num_racers_output = min(num_racers_output, len(self.category.racers))
        for i in range(0, num_racers_output):
            print(self.category.racers[i])

    def output_racers_scoreboard(self, num_racers_output=0):
        if not self.category:
            print('You need to select a category first')
            return

        if num_racers_output == 0:
            num_racers_output = len(self.category.racers)
        else:
            num_racers_output = min(num_racers_output, len(self.category.racers))

        with open(SHARE_FOLDER_PATH, 'w') as scoreboard_file:
            header = '** %s **\r\n' %(self.category.name)
            scoreboard_file.write(header)
            print(header)

            for i in range(0, num_racers_output):
                scoreboard_file.write(self.category.racers[i].as_string_for_scoreboard())
                scoreboard_file.write('\r\n')
                print(self.category.racers[i].as_string_for_scoreboard())

    def quit(self):
        with open('cache.pickle', 'wb') as cache:
            pickle.dump(self.race, cache)

    def load(self):
        with open('cache.pickle', 'rb') as cache:
            self.race = pickle.load(cache)

    def run(self):
        self.display_title_bar()
        choice = ''

        while choice != 'q':
            choice = self.main_menu()

            self.display_title_bar()
            if choice == 's':
                self.setup_race_name()
            elif choice == 'p':
                self.parse_race()
            elif choice == 'k':
                self.parse_race_as_html()
            elif choice == 'c':
                self.select_category()
            elif choice == 'o':
                self.output_racers()
            elif choice == 't':
                self.output_racers_scoreboard(NUM_RACERS_OUTPUT)
            elif choice == 'l':
                self.load()
            elif choice == 'q':
                self.quit()

        print('Bye!')

if __name__ == '__main__':
    APP = Console()
    APP.run()
