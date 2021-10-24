from datetime import datetime


def wep_ap_date_format(date: datetime) -> str:
    abbreviations = {
        "months": [
            "Jan.",
            "Feb.",
            "March",
            "April",
            "May",
            "June",
            "July",
            "Aug.",
            "Sept.",
            "Oct.",
            "Nov.",
            "Dec."
        ]
    }
    day = date.day
    month = abbreviations["months"][date.month - 1]
    year = date.year
    return f"{month} {day}, {year}"