# Zone4Scraper

Quick results scraper for Zone4 to output result information to a giant scoreboard

Parses Zone4 csv result output

File format uses a base header, and then category header adding extra columns, then racers, then a new line to separate categories. Categories may have different numbers of fields for differing numbers of laps.

## Setup

Got stuck since csv is built dynamically in the browser. No way to request it from the server. So we'll need to use Selenium and a browser driver to actually load the dynamic content.

`pip install selenium`

[https://github.com/mozilla/geckodriver/releases](geckodriver)

## TODO

* Parse header and support differing column orderings - check if necessary in other races
* Support laps and multiple numbers of laps
* Console control of output by category, top 3-6, last 3-6
* Support reading file multiple times, updating records and working out which are new changes
* Write output to file for scoreboard. Support fixed width of scoreboard.

## Changelog

Tuesday

* Got csv download using Selenium working finally.
* Need to decide whether to keep using that and parsing the csv
* Or start parsing the webpage directly - can just keep Selenium open and read occasionally.
* Check if we can detect changes to the page? or if we have to parse and diff
* Look at using the announcer view instead - shows new finish line crossers.

Wednesday

* Worked on console side - can store and load data with pickle, can select a category and output data