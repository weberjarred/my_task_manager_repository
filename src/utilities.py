"""Purpose: Provide helper functions
(e.g., date formatting, common validations)."""


def format_date(date_obj, format_str="%d %b %Y"):
    """
    Formats a given date object into a string based on the specified format.

    Args:
        date_obj (datetime.date or datetime.datetime): The date object to
            format.
        format_str (str, optional): The format string to use for formatting
            the date. Defaults to "%d %b %Y", which represents a date in
            the format "day month year" (e.g., "01 Jan 2023").

    Returns:
        str: The formatted date string.
    """
    return date_obj.strftime(format_str)
