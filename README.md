# fetch-backend-assessment

  

This program calculates the number of points left with each payer after spending X number of points (X provided by the user). This program is a part of the fetch backend take home assessment.

## Requirements

Python version ^3.7

 
## Instructions to run

In the command line terminal, enter the following

    python3 main.py X
Provide the value of X which is an integer
For example:

    python3 main.py 5000

## Output
The program outputs a dictionary with the names of the payers and the number of points that each of them are left with after spending X points.

## Error States
There are 2 error states in the program:

 1. If X < 0, then the program outputs "ERROR! Points to spend cannot be less than 0" and exits.
 2. The program expects "transactions.csv" file to be present in the current working directory of the program. If it is not present, the program outputs "ERROR! Points to spend cannot be less than 0"
