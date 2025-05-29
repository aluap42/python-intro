import re
from datetime import datetime

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def calculate_area_of_rectangle(a: float, b: float) -> float:
    if a < 0 or b < 0:
        raise ValueError("Boki prostokąta nie mogą być ujemne")
    return a * b

def filter_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]

def format_date_yyyy_mm_dd(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%d.%m.%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty (oczekiwano: dd.mm.yyyy)")

def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
