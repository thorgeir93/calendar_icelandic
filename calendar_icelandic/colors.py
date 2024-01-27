#from termcolor import colored
#import termcolor

from colored import fg, attr

from enum import Enum

from reportlab.lib.colors import Color
from reportlab.lib import colors

DEFAULT: Color = colors.white
"""The default color."""


class Colors:
    DEFAULT: Color = DEFAULT
    """The default color."""

    HOLIDAY: Color = colors.red
    """Make holidays red."""

    SUNDAY = colors.blue
    """Make sundays blue."""

    MONTH_OFF_SIDE = "grey"
    """Make days that do not belong
    to the current month be grey.
    """

    MONDAY: Color = DEFAULT
    """Monday color."""

    TUESDAY: Color = DEFAULT
    """Tuesday color."""

    WEDNESDAY: Color = DEFAULT
    """Wednesday color."""

    THURSDAY: Color = DEFAULT
    """Thursday color."""

    FRIDAY: Color = DEFAULT
    """Friday color."""

    SATURDAY: Color = DEFAULT
    """Saturday color."""

    # Extract RGB values from a ReportLab color object
    @staticmethod
    def get_rgb_from_reportlab_color(color):
        return (int(color.red * 255), int(color.green * 255), int(color.blue * 255))

    @classmethod
    def colored(cls, text: str, color: Color):
        r, g, b = cls.get_rgb_from_reportlab_color(color)
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
