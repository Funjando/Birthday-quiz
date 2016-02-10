"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
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
eighties=range(1980, 1989)
nineties=range(1990, 1999)
two_thousands=range(2000, 2099)
Stone_Age=range(0, 1979)

#Inputs
username=input("Hello, what is your name?")
birthmonth=input("Hello " + username + ", what was the name of the month you were born in?")
birthyear=input("And what year were you born in, " + username + "?")
birthday=input("And the day?")



#Code


if birthmonth=="October" and birthday==31:
    print("You were born on Halloween!")

elif birthmonth==month and birthday==todaydate:
    print("Happy birthday!")
    
elif birthmonth in winter:
    type=winter

elif birthmonth in spring:
    type=spring

elif birthmonth in summer:
    type=summer

elif birthmonth in fall:
    type=fall

elif birthyear in eighties:
    aeon=eighties

elif birthyear in nineties:
    aeon=nineties
    
elif birthyear in two_thousands:
    aeon="two thousand"
    
elif birthyear in Stone_Age:
    aeon="Stone Age"




print(username + ", you are a {0} baby of the {1}") .format(type, aeon)



