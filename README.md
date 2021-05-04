# finance_calculator(capstone project 1 level_1)

● Create a new Python file in this folder called finance_calculators.py.
● At the top of the file include the line import math
● Write the code that will do the following:


1. The user should be allowed to choose which calculation they want
to do. The first output that the user sees when the program runs
should look like this :
How the user capitalises their selection should not affect how the
program proceeds. I.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’,
‘Investment’, ‘INVESTMENT’, etc. should all be recognised as valid
entries. If the user doesn’t type in a valid input, show an appropriate
error message.


2. If the user selects #‘investment’, do the following:

■ Ask the user to input:
● The amount of money that they are depositing.
● The interest rate (as a percentage). Only the number
of the interest rate should be entered — don’t worry
about having to deal with the added ‘%’, e.g. The user
should enter 8 and not 8%.
● The number of years they plan on investing for.
● Then ask the user to input whether they want “simple”
or “compound” interest, and store this in a variable
called interest. Depending on whether they typed“simple” or “compound”, output the appropriate
amount that they will get after the given period at the
interest rate. Look below in “Interest formulae” for the
formulae to be used.
