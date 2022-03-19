# Election_Analysis

## Overview of Project
The purpose of the election analysis is to show how python can be used with provided data to create a text file and used data pulled from the different source to create a new data sheet to provide a better view of what the data from the exteranl source means. In this specific project we used data from an excel worksheet with 369,712 different rows to get that data and use it to to county the amount of votes linked with the ballot ID's, and also which county that ballot was given, and for which candidate the vote was given too. Using python to extract the data from the excel sheet we used *with open()* to open the file then *csv.reader*  to read the file and then used *for* and *if* statemente to make up the code. In this project list and dictionaries were also used to orginize and manipulate the data. After that was all coded, we used the write functionality to write the output of the code into a text file. To write the file file into a text file I used *txt_file.write* to write that specific variable that had the specific output code that was needed. So in this project there are 3 neccessary files that are for the project, the **PyPoll_Challange**, the **election_analysis.txt**, and the **election_results** excel document.
## Results

**Total Votes:** 
> - 369,711

**County Votes:**
> - Jefferson, 10.5% (38,855)
> - Denver, 82.8% (306,055)
> - Arapahoe, 6.7% (24,801)

**County With Largest Amount of Votes:**

> - Denver, with 306,055 votes

**Candidate Vote Count:**

> - Charles Casper Stockham, 23.0% (85,213)
> - Diana DeGette, 73.8% (272,892)
> - Raymon Anthony Doane, 3.1% (11,606)

**Winning Candidate:**

> - Winner: Diana DeGette
> - Winning Vote Count: 272,892
> - Winning Percentage: 73.8%

## Summary
