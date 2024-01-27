from datetime import date
from typing import Final

from reportlab.lib.colors import Color

from calendar_icelandic.colors import Colors
from calendar_icelandic.mode import Mode

from calendar_icelandic.calendar_config import get_weekdays


weekdays_icelandic: Final[list[str]] = [
    "Mánudagur", "Þriðjudagur", "Miðvikudagur", "Fimmtudagur",
    "Föstudagur", "Laugardagur", "Sunnudagur"
]

WEEKDAYS: Final[list[str]] = weekdays_icelandic

class Position:
    x: int = 0
    y: int = 0

class Day:

    def __init__(self, ts: date, lang: str = "is", mode: Mode = Mode.terminal, color_default: Color = Colors.DEFAULT, color_lock: Color | None = None):
        """
        Args:
            color_lock: Locks the color of the day, This color will be used even though it's
                a holiday or something else.
        """
        self.ts = ts
        self._is_holiday: bool = False
        self._mode = mode
        self._lang = lang
        self._labels: list[str] = []
        self._color_default: Color | None = color_default
        self._color_lock: Color | None = color_lock

    def lock_color(self, color_lock: Color):
        """
        Args:
            color_lock: Locks the color of the day, This color will be used even though it's
            a holiday or something else.
        """
        self._color_lock = color_lock

    def mark_as_holiday(self, color: Color = Colors.HOLIDAY):
        """Set this day as holiday."""
        self._is_holiday = True
        self._color_default = color

    @property
    def is_holiday(self) -> bool:
        """Checks if this day is a holiday."""
        return self._is_holiday

    def get_weekday_name(self, lang: str = "is"):
        return get_weekdays(lang=lang)[self.ts.weekday()]

    def is_sunday(self) -> bool:
        return self.ts.weekday() == 6

    def set_label(self, label: str):
        """Stores the given label to the current day."""
        self._labels.append(label)

    def __str__(self):
        day_str = str(self.ts.day).rjust(2)  # Right-align the day

        if self._mode == Mode.terminal:
            if self._color_lock:
                return Colors.colored(day_str, self._color_lock)
            return Colors.colored(day_str, self._color_default)

        return day_str


class SunDay:
    """Class representing Sunday."""
    title: str = "Sunnudagur"
    short: str = "Sun"

class MonDay(Day):
    """Class representing Monday."""
    color: str = Colors.MONDAY

class TuesDay(Day):
    """Class representing Tuesday."""
    color: str = Colors.TUESDAY

class WednesDay(Day):
    """Class representing Wednesday."""
    color: str = Colors.WEDNESDAY

class ThursDay(Day):
    """Class representing Thursday."""
    color: str = Colors.THURSDAY

class FriDay(Day):
    """Class representing Friday."""
    color: str = Colors.FRIDAY

class SaturDay(Day):
    """Class representing Saturday."""
    color: str = Colors.SATURDAY