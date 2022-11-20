from typing import List

from bs4 import BeautifulSoup
from insynsregistret import TradeEntry


def get_trade_entries_from_page(page: bytes) -> List[TradeEntry]:
    trade_entries = []
    soup = BeautifulSoup(page, "html.parser")
    table_rows = soup.find_all("tr")
    for row in table_rows[1:]:
        row_data = row.findAll("td")
        row_data = [tag.get_text(strip=True) for tag in row_data]
        row_data = [s.replace("\xa0", " ") for s in row_data]
        trade_entries.append(TradeEntry.from_row(row_data))
    return trade_entries


def find_next_button(page: bytes):
    pass
