from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_calendar(year, month, filename="calendar.pdf"):
    # Constants
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Leap year check
        days_in_month[1] = 29
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Create a new PDF with letter page size
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Draw title (month and year)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 1 * inch, f"{month} {year}")

    # Set up grid
    day_width = width / 7
    day_height = (height - 2 * inch) / 6

    # Draw day names
    c.setFont("Helvetica-Bold", 12)
    for i, day in enumerate(days):
        c.drawString((i * day_width) + (day_width / 2), height - 1.5 * inch, day)

    # Draw day cells
    for i in range(6):  # Rows
        for j in range(7):  # Columns
            x = j * day_width
            y = height - 2*inch - (i * day_height)
            c.rect(x, y, day_width, day_height)

    # Fill in the days for the month
    c.setFont("Helvetica", 12)
    start_day = (days_in_month[month-1] - 1) % 7  # Replace this with the appropriate starting day for the month
    for day in range(1, days_in_month[month-1] + 1):
        column = (start_day + day - 1) % 7
        row = (start_day + day - 1) // 7
        x = column * day_width + (day_width / 4)
        y = height - 2.25*inch - (row * day_height)
        c.drawString(x, y, str(day))

    c.save()

# Test
create_calendar(2023, 10, "October_2023.pdf")
