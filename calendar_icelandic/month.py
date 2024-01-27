from datetime import date, timedelta

from workalendar.core import Calendar
from workalendar.europe import Iceland

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

from calendar_icelandic.day import Day
from calendar_icelandic.calendar_config import get_weekdays
from calendar_icelandic.mode import Mode



class Month:
    def __init__(self, year: int, month: int, calendar: type[Calendar], mode: Mode, lang: str = "is"):
        self.year = year
        self.month = month
        self.calendar = calendar
        self.lang = lang
        self._days: list[Day] = []
        self._mode = mode

    @property
    def days(self) -> list[Day]:
        """Returns the days of the month."""
        if not self._days:
            self._days = self._generate_days()
        return self._days

    def _generate_days(self) -> list[Day]:
        """Generates the days of the months.

        """
        first_day = date(self.year, self.month, 1)

        # Find the first Sunday before the start of the month
        while first_day.weekday() != 6:
            first_day -= timedelta(days=1)

        # Generate a list of Day objects for the entire month
        month_days = []
        ts: date
        for i in range(42):  # 42 days for 6 weeks
            ts = first_day + timedelta(days=i)
            day = Day(ts=ts, mode=self._mode)
            if self.calendar.is_holiday(ts):
                day.mark_as_holiday()
                day.set_label(self.calendar.get_holiday_label(ts))
            month_days.append(day)

        return month_days

    def terminal(self):
        # Output the calendar
        for i, day in enumerate(self.days):
            if i % 7 == 0 and i != 0:
                print()  # Start a new line for each week
            print(day, end=" ")

    def render_to_pdf(self, filename: str = "calendar.pdf") -> None:

        # Style the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Default color
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
        ])

        # Convert the list of days into a table for ReportLab
        data: list[list[str]] = [get_weekdays(lang=self.lang)]

        week: list[str] = []

        from reportlab.lib.colors import red
        for i, day in enumerate(self.days):
            week.append(str(day))

            # Calculate X and Y coordinates
            x = i % 7
            y = i // 7 + 1  # Add 1 to start from row 1, assuming row 0 is the header

            print(day.color)
            style.add('TEXTCOLOR', (x, y), (x, y), day.color)

            if i % 7 == 6:
                data.append(week)
                week = []

        # If there are any remaining days in the week after exiting the loop
        if week:
            data.append(week)

        table = Table(data, colWidths=[2.5*cm for _ in range(7)], rowHeights=[2*cm for _ in range(7)])
        table.setStyle(style)

        # Create the PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        doc.build([table])

if __name__ == "__main__":
    year = 2023
    month = 12
    icelandic_calendar_instance = Iceland()
    month = Month(year, month, calendar=icelandic_calendar_instance, mode=Mode.terminal)
    #calendar.render_to_pdf("December_2023.pdf")
    month.terminal()
