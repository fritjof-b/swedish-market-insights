from datetime import date


def date_from_string(date_string: str) -> "date":
    year, month, day = [int(e) for e in date_string.split("-")]
    return date(year, month, day)


def is_relative(relative: str) -> bool:
    return "ja" in relative.lower()


def parse_volume_from_string(volume: str) -> int:
    if "," in volume:
        return int("".join([_ for _ in volume.split(",")]))

    if " " in volume:
        return int("".join([_ for _ in volume.split()]))

    return int("".join([_ for _ in volume.split()]))


def parse_price_from_string(price: str) -> float:
    return float(".".join([_ for _ in price.split(",")]))
