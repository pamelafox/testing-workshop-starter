def greater_num(num1, num2):
    """Returns whichever number is highest of the two supplied numbers."""
    if num1 > num2:
        return num1
    else:
        return num2


def hello_world(language_code):
    """Returns the translation of "Hello, World" into the language
    specified by the language code (e.g. "es", "pt", "en"),
    defaulting to English if an unknown language code is specified.
    """
    if language_code == "es":
        return "Hola, Mundo"
    elif language_code == "pt":
        return "Olá, Mundo"
    return "Hello, World"


def assign_grade(score):
    """Returns a letter grade for the numeric score based on the grade bins of:
    "A" (90-100), "B" (80-89), "C" (70-79), "D" (65-69), or "F" (0-64)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D"
    else:
        return "F"
