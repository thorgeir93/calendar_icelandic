# Author: thorgeir <thorgeirsigurd@gmail.com>
#
# Requirements:
#   pip install -U workalendar
#   pip install -U calendar
#
# TODO print out three months in the same row.
#
import argparse
import calendar
from workalendar.europe import Iceland
from datetime import datetime

cal = calendar.LocaleTextCalendar(firstweekday=6, locale='is_IS')

def colorize(target_string, color):
    return "%s%s%s" % (color, target_string, "\033[0m")

def month(the_year, the_month, display_year=True):
    holidays = [h[0] for h in Iceland().holidays( the_year )]

    #header_row = ""
    #weekday_names_row = ""
    #monthdays_row = [] 

    #
    # The Header
    #
    print( "" )
    #print( "     ", end="" )
    month_title = cal.formatmonthname(the_year, the_month, 1, withyear=False) 
    if display_year:
        print(colorize( month_title.title()+'(%s)' % the_year, "\033[4m"))
    else:
        print(colorize( month_title.title(), "\033[4m"))
    print( cal.formatweekheader(2) )
    print( '-' * 20 )

    # The calendar itself.
    for week_num, week in enumerate(cal.monthdatescalendar(the_year,the_month)):
        weekdays = ''
        for weekday, day in enumerate(week):
            the_day = str(day.day)
            
            if len(the_day) == 1:
                the_day = " "+the_day
           
            # Make the the last days from last month be
            # less readable than main days in the month. 
            if week_num == 0 and day.day > 8:
                the_day = colorize(the_day, "\033[93m")
            
            # Make the days from the next month be less 
            # readable than main days in the month. 
            elif week_num > 3 and day.day < 8:
                the_day = colorize(the_day, "\033[93m")
                
            elif day in holidays:
                the_day = colorize(the_day, "\033[46m")
            
            elif day.weekday() == 6:
                the_day = colorize(the_day, "\033[96m")
               
            weekdays += the_day+" "
        print( weekdays )

def hole_year(the_year):
    for i in range(1, 13):
        month( the_year, i ) 

def _print_out_possible_colors():
    for i in range(1,257):
        i=str(i)
        print( i, '\033['+i+'m', "Test the color", i, '\033[0m')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple Icelandic calendar.')
    parser.add_argument('-m', '--month',
                        type=int,
                        dest='month', 
                        default=datetime.today().month,
                        help='Which month to choose from, one of 1 to 12. The default value is the number of the current month.')
    
    parser.add_argument('-y', '--year',
                        type=int,
                        dest='year', 
                        default=datetime.today().year,
                        help='Which year to choose from, 0 to 9999. The default value is the current year.')
    
    args = parser.parse_args()

    month( args.year, args.month )

    #print( args.cl_args )
    
    #print( args.cl_args.month )

    #_print_out_possible_colors()
    #month( 2018, 4 )
    #hole_year(2019)


