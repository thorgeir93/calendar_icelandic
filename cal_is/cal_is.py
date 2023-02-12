#!/usr/bin/env python
#
# Author: thorgeir <thorgeirsigurd@gmail.com>
#
# Requirements:
#   pip install -U workalendar
#   pip install -U calendar
#
# TODO print out three months in the same row.
#
from __future__ import print_function
import argparse
import datetime
import calendar
from workalendar.europe import Iceland

__author__ = "thorgeir <thorgeirsigurd@gmail.com>"

cal = calendar.LocaleTextCalendar(firstweekday=6, locale='is_IS')

#grid = [
#    (x, ),
#]

class Colors(object):
    RED="\033[96m"
    RED_LIGHT="\033[46m"
    GRAY="\033[93m"
    WHITE="\033[2m"
    CLEAR="\033[0m"
    BLINK_WHITE="\033[6m"
    HIGHLIGHT_RED="\033[46m"

class Day(Colors):
    def __init__(self, number):
        self.number = number
        self.set_color()

    def set_number(self):
        self.color = self.white
    
    def set_weekday_name(self, weekday_name):
        self.weekday_name = weekday_name
    
    def set_weekday_number(self, weekday_number):
        self.weekday_number = weekday_number

    def set_color(self):
        self.color = self.WHITE

    def set_position(self, x, y):
        self.position=(x, y)

    def get_position(self):
        return self.position

    def output(self):
        extra_space = ""

        if len(str(self.number)) == 1:
            extra_space = " "
            
        return "{0}{1}{2}{3}".format(self.color, extra_space, self.number, self.CLEAR)

class Sunday(Day):
    def set_color(self):
        self.color = self.RED_LIGHT

class CurrentDay(Day):
    def set_color(self):
        self.color = self.BLINK_WHITE
    
class Holiday(Day):
    def set_color(self):
        self.color = self.HIGHLIGHT_RED

class OtherMonthDay(Day):
    def set_color(self):
        self.color = self.GRAY

def colorize(target_string, color):
    return "%s%s%s" % (color, target_string, "\033[0m")

#def month(the_year, the_month, display_year=True):
#    # Extract only the holyday dates, not the name of the holiday.
#    holidays = [h[0] for h in Iceland().holidays( the_year )]
#
#    #
#    # The Header
#    #
#    print( "" )
#    #print( "     ", end="" )
#    month_title = cal.formatmonthname(the_year, the_month, 1, withyear=False) 
#    if display_year:
#        print(colorize( month_title.title()+'(%s)' % the_year, "\033[4m"))
#    else:
#        print(colorize( month_title.title(), "\033[4m"))
#    print( cal.formatweekheader(2) )
#    print( '-' * 20 )
#
#    month_weeks = []
#
#    # The calendar itself.
#    for week_num, week in enumerate(cal.monthdatescalendar(the_year,the_month)):
#        week_list = []
#        weekdays = ''
#        for weekday, day in enumerate(week):
#            day_number = int(day.day)
#            the_day = str(day.day)
#            
#            if len(the_day) == 1:
#                the_day = " "+the_day
#           
#            # Make the the last days from last month be
#            # less readable than main days in the month. 
#            if week_num == 0 and day.day > 8:
#                day = OtherMonthDay( day_number )
#                the_day = colorize(the_day, "\033[93m")
#            
#            # Make the days from the next month be less 
#            # readable than main days in the month. 
#            elif week_num > 3 and day.day < 8:
#                day = OtherMonthDay( day_number )
#                the_day = colorize(the_day, "\033[93m")
#                
#            elif day in holidays:
#                day = Holiday(day_number)
#                the_day = colorize(the_day, "\033[46m")
#            
#            elif day.weekday() == 6:
#                day = Sunday(day_number)
#                the_day = colorize(the_day, "\033[96m")
#
#            # Make the today number blik for good visability
#            if day == datetime.date.today():
#                day = CurrentDay(day_number)
#                the_day = colorize(the_day, "\033[6m")
#              
#            week_list.append( day )
#            weekdays += the_day+" "
#        month_weeks.append( week_list )
#        print( weekdays )
#
#    return month_weeks

def month(the_year, the_month, display_year=True, notes=None):
    """
    :param notes: Config about which dates contains notes.
        Where key is the date itself, value is list where the first element
        is the type of the note and the second element is the notes itself.
         {"2022-03-27": ["note", "Foobar!"]}
    :type notes: Dict.
    """
    # Extract only the holyday dates, not the name of the holiday.
    holidays = [h[0] for h in Iceland().holidays( the_year )]

    if notes is None:
        notes = {}

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

    month_weeks = []

    # The calendar itself.
    for week_num, week in enumerate(cal.monthdatescalendar(the_year,the_month)):
        week_list = []
        weekdays = ''
        for weekday, day in enumerate(week):
            if str(day) in notes.keys():
                note_type, note_text = notes[str(day)]
                print(note_type)
                print(note_text)

            day_number = int(day.day)
            
            # Make the the last days from last month be
            # less readable than main days in the month. 
            if week_num == 0 and day.day > 8:
                day = OtherMonthDay( day_number )
            
            # Make the days from the next month be less 
            # readable than main days in the month. 
            elif week_num > 3 and day.day < 8:
                day = OtherMonthDay( day_number )
                
            elif day in holidays:
                day = Holiday(day_number)
            
            elif day.weekday() == 6:
                day = Sunday(day_number)

            # Make the today number blik for good visability
            if day == datetime.date.today():
                day = CurrentDay(day_number)

            if isinstance(day, datetime.date):
                day = Day(day_number)
              
            week_list.append(day)

        month_weeks.append( week_list )

    return month_weeks

def hole_year(the_year):
    for i in range(1, 13):
        month(the_year, i) 

def _print_out_possible_colors():
    for i in range(1,257):
        i=str(i)
        print( i, '\033['+i+'m', "Test the color", i, '\033[0m')

#def save_note():

if __name__ == "__main__":
    #_print_out_possible_colors()
    #import sys; sys.exit(0)
    parser = argparse.ArgumentParser(description='Simple Icelandic calendar.')

    parser.add_argument('-m', '--month',
        type=int,
        dest='month', 
        default=datetime.date.today().month,
        help='Which month to choose from, one of 1 to 12. The default value is the number of the current month.'
    )
    
    parser.add_argument('-y', '--year',
        type=int,
        dest='year', 
        default=datetime.date.today().year,
        help='Which year to choose from, 0 to 9999. The default value is the current year.'
    )

    parser.add_argument('-a', '--add',
        type=str,
        default=None,
        help='Add a note to a specificed day.'
    )
    
    #parser.add_argument('-t', '--type',
    #    type=,
    #    default=None,
    #    help='Add a note to '
    #)
    args = parser.parse_args()

    notes = None
    if args.add:
        print("What is your note?")
        note = raw_input()

        notes = {
            args.add: ["note", note]
        }

    #save_note(notes)

    one_month = month(args.year, args.month, notes=notes)

    for week in one_month:
        for day in week:
            #print( day )
            #print(dir(day))
            #try:
            print(day.output()+" ", end='')
            #except:
            #    print( str(day.day)+" ", end='')
            #    pass
                #print(day)
        print('')

    #print( res )

    #_print_out_possible_colors()
    #month( 2018, 4 )
    #hole_year(2019)
