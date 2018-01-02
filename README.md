# Zone4Scraper
Quick results scraper for Zone4 to output result information to a giant scoreboard

Parses Zone4 csv result output

File format uses a base header, and then category header adding extra columns, then racers, then a new line to separate categories. Categories may have different numbers of fields for differing numbers of laps.

## TODO
* Parse header and support differing column orderings - check if necessary in other races
* Support laps and multiple numbers of laps
* Console control of output by category, top 3-6, last 3-6
* Support reading file multiple times, updating records and working out which are new changes
* Write output to file for scoreboard. Support fixed width of scoreboard.
