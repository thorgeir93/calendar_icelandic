
# Names of the weekdays in various languages
WEEKDAYS: dict[str, list[str]] = {
    "en": ["Sunday", "Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday"],
    "is": ["Sunnudagur", "Mánudagur", "Þriðjudagur", "Miðvikudagur", "Fimmtudagur", "Föstudagur", "Laugardagur"],
}

WEEKDAYS_MIN: dict[str, list[str]] = {
    "en": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    "is": ["Sun", "Mán", "Þri", "Mið", "Fim", "Fös", "Lau"],
}

# Names of the months in various languages
MONTHS: dict[str, list[str]] = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "is": ["Janúar", "Febrúar", "Mars", "Apríl", "Maí", "Júní", "Júlí", "Ágúst", "September", "Október", "Nóvember", "Desember"],
}

def get_weekdays(lang: str = "is") -> list:
    """Return the list of weekdays for the specified language."""
    return WEEKDAYS.get(lang, WEEKDAYS["is"])

def get_months(lang: str = "is") -> list:
    """Return the list of months for the specified language."""
    return MONTHS.get(lang, MONTHS["is"])