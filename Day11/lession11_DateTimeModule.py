"""
Date Time Module
________________
"""

from datetime import *

cDate=datetime.now()
print(cDate)

cDateYear=datetime.now()
print(cDateYear.year)

cDateMonth=datetime.now()
print(cDateYear.month)

cDateDay=datetime.now()
print(cDateDay.day)

cDateHour=datetime.now()
print(cDateHour.hour)
print(cDateHour.minute)
print(cDateHour.second)

# Formating Date & Time


print(cDateHour.strftime('Week day short  : %a'))
print(cDateHour.strftime('Week day full   : %A'))
print(cDateHour.strftime('Week day number : %w'))
print('='*80)

print(cDateHour.strftime('Week day of month         : %d'))
print(cDateHour.strftime('Week day month short      : %b'))
print(cDateHour.strftime('Week day month full       : %B'))
print(cDateHour.strftime('Week day month number     : %m'))
print(cDateHour.strftime('Without Century           : %y'))
print(cDateHour.strftime('With Century              : %Y'))
print('='*80)

cDateT=datetime.now()
print(cDateT.strftime("Hour 24                   :%H"))
print(cDateT.strftime("Hour 12                   :%I"))
print(cDateT.strftime("Hour am/pm                :%p"))
print(cDateT.strftime("Minute 60                 :%M"))
print(cDateT.strftime("Second 60                 :%S"))
print(cDateT.strftime("Micro Second              :%f"))

print(cDateT.strftime("Full Time                 :%T"))
print(cDateT.strftime("Full Date                 :%D"))

print(cDateT.strftime("Full Date                 :%Y-%m-%d"))
print(cDateT.strftime("Full Date                 :%Y-%m-%d %T"))

print(cDateT.strftime("Custom Time               :%I:%M:%S %p"))

print(cDateT.strftime("Custom date               :%A, %B %d,%Y"))   
