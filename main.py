import datetime
from tkinter import *


def main():
    ##READ PREPARED FILE##
   file = open('DailyAffirmations.csv', 'r', encoding='utf-8-sig')
   lines = file.readlines()
   #print(lines)
   file.close()
   ##SELECT AFFIRMATION BASED ON DAY OF YEAR##
   dayofyear = datetime.datetime.today().timetuple().tm_yday
   dailyAffirmation = (lines[dayofyear])

if __name__ == "__main__":
    main()
    