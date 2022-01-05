from datetime import date, timedelta

"""
def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)
"""
def allsundays(year, weekdays):
    # 'weekdays': An array of integers (0=Monday)
    # 'year': Year as integer

    d = date(year, 1, 1)                    # January 1st
    dates = []  # Datetime objects that pass requirement
    while d.year == year:
        if d.weekday() in weekdays:
            dates.append(d)
        d += timedelta(days = 1) # Add 1 day
    return dates

def main():
    days = allsundays(2020, [4])
    for d in days:
        print("\subsection{Lab _: " + d.strftime("%Y %m %d (%a)") + "}")

if __name__ == "__main__":
    main()
