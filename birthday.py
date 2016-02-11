"""
birthday.py
Author: Andreas
Credit: Dan, Payton, tiggerntatie
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

#imports
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
month=month_name[todaymonth]

#Datalists
winter=['December', 'January', 'February']
spring=['March', 'April', 'May']
summer=['June', 'July', 'August']
fall=['September', 'October', 'November']
eighties=list(range(1980, 1990))
nineties=list(range(1990, 2000))
two_thousands=list(range(2000, 2100))
Stone_Age=list(range(0, 1980))

#Inputs
username=input("Hello, what is your name? ")
birthmonth=input("Hi " + username + ", what was the name of the month you were born in? ")
birthyear=int(input("And what year were you born in, " + username + "? "))
birthday=int(input("And the day? " ))


#Code
if birthmonth=="October" and birthday==31:
    print("You were born on Halloween! ")

elif birthmonth==month and birthday==todaydate:
    print("Happy birthday! ")
 
else:

    if birthmonth in winter:
        season="winter"
    
    if birthmonth in spring:
        season="spring"
    
    if birthmonth in summer:
        season="summer"
    
    if birthmonth in fall:
        season="fall"
    
    if birthyear in eighties:
        aeon="eighties"
    
    if birthyear in nineties:
        aeon="nineties"
        
    if birthyear in two_thousands:
        aeon="two thousands"
        
    if birthyear in Stone_Age:
        aeon="Stone Age"
    
    
    s="{0}, you are a {1} baby of the {2}."
    print(s.format(username, season, aeon))
    


