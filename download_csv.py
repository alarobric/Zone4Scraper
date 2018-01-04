import os
import time
import glob

from selenium import webdriver

def download_csv(race_url):
    """Open firefox and download the given race as csv.

    @param race_url Zone4 URL for race
    @returns filename of new csv
    """
    #set firefox to download without prompting
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain;charset=utf-8")

    browser = webdriver.Firefox(firefox_profile=fp)
    browser.implicitly_wait(10) # tell Firefox to wait up to 10 seconds to find something

    #browser.get('http://zone4.ca/race/2017-12-17/c6e78e84/2017-haywood-noram-day-3-mass/results/')
    browser.get(race_url)

    # find and click the download csv button
    browser.find_element_by_xpath('//div[contains(@class,"public-race-actions")]/div[contains(@class,"right")]/a').click()
    browser.find_element_by_link_text('Download Results (CSV)').click()

    # need to tell selenium to wait for the file then quit
    while not glob.glob('Res*.csv'):
        print('waiting for file')
        time.sleep(1)

    csvfile = glob.glob('Res*.csv')
    print('File found', csvfile)

    browser.quit()

    return csvfile[0]
