# Parses Zone4 html result output

from selenium import webdriver

import race_results

class Parser(object):
    def __init__(self, race_url, debug=False):
        self.debug = debug
        self.race = race_results.Race(race_url)
        self.browser = None

        self.load_results_page(race_url)

    def load_results_page(self, race_url):
        """Open firefox and load the results page

        @param race_url Zone4 URL for race
        """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10) # tell Firefox to wait up to 10 seconds to find something

        self.browser.get(race_url)

        # wait for initial page load
        self.browser.find_element_by_xpath('//div[contains(@class,"public-race-actions")]/div[contains(@class,"right")]/a')

    def close_results_page(self):
        self.browser.quit()

    def quit(self):
        self.close_results_page()

    def parse_category(self, racer_group):
        category = racer_group.find_element_by_xpath('div[1]/h2').text
        category = category.split('–')[0].rstrip()
        print(category)

        secondary_info = racer_group.find_element_by_xpath('div[1]/div[contains(@class,"secondary-info")]').text
        print(secondary_info)

        category = race_results.Category(category)

        for racer_elem in racer_group.find_elements_by_xpath('.//ul[contains(@class,"racer-list")]/li'):
            racer = self.parse_racer(racer_elem)
            category.add_racer(racer)

        self.race.add_category(category)

    def parse_racer(self, elem):
        status = None
        rank = elem.find_element_by_xpath('.//span[contains(@class,"place only-wide")]').text
        #hidden elements don't return text
        name = elem.find_element_by_xpath('a[2]/span[contains(@class,"getName")]').text
        name = elem.find_element_by_xpath('a/span').get_attribute('innerHTML')
        time = elem.find_element_by_xpath('.//span[contains(@class,"finish time")]').text
        bib = elem.find_element_by_class_name('bib').text.split(':')[1].strip()
        bib = int(bib)
        if not rank.isnumeric():
            status = rank
        #todo split name better
        firstname = name.split(' ')[0]
        lastname = ''
        try:
            lastname = name.split(' ')[1]
        except:
            pass

        racer = race_results.Racer(bib, firstname, lastname, status)
        if time:
            racer.time = time
        #if finish:
            #racer.finish = finish
        if rank:
            racer.rank = rank

        if self.debug:
            print(racer)

        return racer

    def parse_page(self):
        for racer_group in self.browser.find_elements_by_class_name('racer-group'):
            self.parse_category(racer_group)

        return self.race

if __name__ == '__main__':
    PARSER = Parser('http://zone4.ca/race/2017-12-17/c6e78e84/2017-haywood-noram-day-3-mass/results/', debug=True)
    PARSER.parse_page()
