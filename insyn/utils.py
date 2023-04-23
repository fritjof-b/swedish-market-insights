from datetime import date


def date_from_string(date_string: str) -> date:
    year, month, day = [int(e) for e in date_string.split("-")]
    return date(year, month, day)


def is_relative(relative_str: str) -> bool:
    return "ja" in relative_str.lower()


def parse_volume_from_string(volume_str: str) -> int:
    cleaned_volume_str = volume_str.replace(",", "").replace(" ", "")
    return int(cleaned_volume_str)


def parse_price_from_string(price_str: str) -> float:
    cleaned_price_str = price_str.replace(",", ".")
    return float(cleaned_price_str)
