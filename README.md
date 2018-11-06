# Zone4Scraper

Quick results scraper for Zone4 to output result information to a giant scoreboard

Parses Zone4 csv result output

File format uses a base header, and then category header adding extra columns, then racers, then a new line to separate categories. Categories may have different numbers of fields for differing numbers of laps.

## Setup

Got stuck since csv is built dynamically in the browser. No way to request it from the server. So we'll need to use Selenium and a browser driver to actually load the dynamic content.

Optionally use virtualenv to manage your python environment
`virtualenv env`
`env\Scripts\activate`

Then
`pip install selenium`

[https://github.com/mozilla/geckodriver/releases](geckodriver)

## Usage

`python console.py`

Zone4Scraper is console based and menu driven.

Available options:

* 's' - Set or update the race name. This is the link to the Zone4 results page for the race.
* 'p' - Download and parse the results as a csv file. *download_csv.py, csv_parser.py*
* 'l' - Load past results from pickle file
* 'k' - Load results from HTML - *html_parser.py*

Once a race is loaded, the basic number of categories and racers is output. A category can be selected

* 'c' - Select a category
* 'o' - Print the full list of racers in the category
* 't' - Prints just the top 6 racers in the category to the scoreboard text file. Print a header including category name.

The number of racers to output and filename to write to are both specified at the top of console.py. The scoreboard file could be a network share used by the scoreboard computer to read and display on a Jumbotron.

## TODO

[Issue list](//github.com/alarobric/Zone4Scraper/issues)

* #2 Write output to file for scoreboard. Support fixed width of scoreboard.
* #3 Support laps and multiple numbers of laps
* #4 Console control of output by category, top 3-6, last 3-6
* #5 Support reading file multiple times, updating records and working out which are new changes
* #6 Parse header and support differing column orderings - check if necessary in other races
* #7 Allow automatic update, parsing results every 30s etc.

## Changelog

Nov 5, 2018

Added some documentation to remind myself how things work. Getting ready for another season, this time the scoreboard is working!

Jan 3, 2018

* Worked on console side - can store and load data with pickle, can select a category and output data

Jan 2, 2018

* Got csv download using Selenium working finally.
* Need to decide whether to keep using that and parsing the csv
* Or start parsing the webpage directly - can just keep Selenium open and read occasionally.
* Check if we can detect changes to the page? or if we have to parse and diff
* Look at using the announcer view instead - shows new finish line crossers.