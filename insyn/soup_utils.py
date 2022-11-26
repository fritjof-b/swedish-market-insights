from bs4 import BeautifulSoup

from trade import TradeEntry


def get_trade_entries_from_page(page: bytes) -> list[TradeEntry]:
    trade_entries = []
    soup = BeautifulSoup(page, "html.parser")
    table_rows = soup.find_all("tr")
    for row in table_rows[1:]:
        row_data = row.findAll("td")
        row_data = [tag.get_text(strip=True) for tag in row_data]
        row_data = [s.replace("\xa0", " ") for s in row_data]
        trade_entries.append(TradeEntry.from_row(row_data))
    return trade_entries


def find_href_for_next_page(page: bytes) -> str:
    soup = BeautifulSoup(page, "html.parser")
    next_button = soup.find('li', class_="next")
    href = next_button.a.get("href") if next_button.a else ''
    return href
