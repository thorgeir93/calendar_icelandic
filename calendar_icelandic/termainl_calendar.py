from workalendar.core import Calendar
from workalendar.europe import Iceland

from calendar_icelandic.display import ColorPrinter
from calendar_icelandic.mode import Mode
from calendar_icelandic.month import Month

class TerminalCalendar:
    """
    A calendar for displaying months and their days with color coding.
    """

    def __init__(self, month_names: list[str], day_names: list[str], year: int, calendar_instance: type[Calendar], printer: ColorPrinter, lang: str = "is"):
        """
        Initialize a Calendar object.

        :param month_names: List of month names.
        :param day_names: List of abbreviated day names.
        :param year: Year for the calendar.
        :param calendar_instance: An instance of the calendar to determine holidays.
        :param printer: An instance of ColorPrinter for colorized printing.
        """
        self.month_names: list[str] = month_names
        self.day_names: list[str] = day_names
        self.year: int = year
        self.calendar_instance: type[Calendar] = calendar_instance
        self.printer = printer
        self._lang = lang

    def _print_header(self, month_num: int) -> None:
        """
        Print the header (month name and day abbreviations) for a given month.

        :param month_num: Month number (1 to 12).
        """
        self.printer.println(f"{self.month_names[month_num - 1].capitalize()}({self.year})")
        self.printer.println(" ".join(self.day_names))
        self.printer.println("-" * 20)

    def print_month(self, month_num: int) -> None:
        """
        Print the month including the header and day numbers for a given month.

        :param month_num: Month number (1 to 12).
        """
        month: Month = Month(self.year, month_num, self.calendar_instance, lang=self._lang, mode=Mode.terminal)
        self._print_header(month_num)
        for index, day in enumerate(month.days):
            day_color = "red" if day.is_sunday else "gray" if not day.is_in_month else "white"
            #self.printer.print(day)
            print(day, end="")
            self.printer.print(" ")  # Space between days
            if (index + 1) % 7 == 0:
                print()
        print("\n")

    def print_calendar(self) -> None:
        """
        Print the entire calendar year including the header and day numbers for each month.
        """
        for month_num in range(1, 13):
            self.print_month(month_num)


if __name__ == "__main__":
    icelandic_month_names = [
        "janúar", "febrúar", "mars", "apríl", "maí", "júní",
        "júlí", "ágúst", "september", "október", "nóvember", "desember"
    ]
    icelandic_day_names = ["su", "má", "þr", "mi", "fi", "fö", "la"]

    year = 2017


    icelandic_calendar_instance = Iceland()

    #month = Month(2023, 10, icelandic_calendar_instance)

    #print(month)

    icelandic_calendar = TerminalCalendar(icelandic_month_names, icelandic_day_names, year, icelandic_calendar_instance, printer=ColorPrinter())

    icelandic_calendar.print_calendar()
