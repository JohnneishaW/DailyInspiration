import datetime


def main():
    ##READ PREPARED FILE##
   file = open('DailyAffirmations.txt', 'r', encoding='utf-8-sig')
   lines = file.readlines()
   #print(lines)
   file.close()
   ##SELECT AFFIRMATION BASED ON DAY OF YEAR##
   dayofyear = datetime.datetime.today().timetuple().tm_yday
   dailyAffirmation = (lines[dayofyear])
   print(dailyAffirmation)

if __name__ == "__main__":
    main()