from bs4 import BeautifulSoup

from .trade import TradeEntry


def get_trade_entries_from_page(page: bytes) -> list[TradeEntry]:
    trade_entries = []
    soup = BeautifulSoup(page, "html.parser")
    table_rows = soup.find_all("tr")
    for row in table_rows[1:]:
        row_data = [
            tag.get_text(strip=True).replace("\xa0", " ") for tag in row.find_all("td")
        ]
        trade_entries.append(TradeEntry.from_row(row_data))
    return trade_entries


def find_href_for_next_page(page: bytes) -> str:
    soup = BeautifulSoup(page, "html.parser")
    next_button = soup.find("li", class_="next")
    if next_button and next_button.a:
        href = next_button.a.get("href")
    else:
        href = ""
    return href
