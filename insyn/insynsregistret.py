from datetime import date

import requests

from soup_utils import get_trade_entries_from_page, find_href_for_next_page
from trade import TradeEntry

BASE_URL = "https://marknadssok.fi.se/Publiceringsklient/sv-SE/Search/Search?"


def _get_trades_by_date_query(
        from_query: str,
        to_query: str,
        from_date: date,
        to_date: date,
) -> list[TradeEntry]:
    params = {from_query: from_date, to_query: to_date}

    contents = []
    response = requests.get(BASE_URL, params=params)
    contents.append(response.content)
    while next_page_href := find_href_for_next_page(response.content):
        print(f'{BASE_URL}{next_page_href}')
        response = requests.get(f'{BASE_URL}{next_page_href}')
        contents.append(response.content)

    result = []
    for page in contents:
        result += get_trade_entries_from_page(page)

    return result


class Insynsregistret:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_trades_by_publish_date(
            from_date: date = date.today(), to_date: date = date.today()
    ) -> list[TradeEntry]:
        return _get_trades_by_date_query(
            "Publiceringsdatum.From", "Publiceringsdatum.To", from_date, to_date
        )

    @staticmethod
    def get_trades_by_transaction_date(
            from_date: date = date.today(), to_date: date = date.today()
    ) -> list[TradeEntry]:
        return _get_trades_by_date_query(
            "Transaktionsdatum.From", "Transaktionsdatum.To", from_date, to_date
        )


insyn = Insynsregistret()
trades = insyn.get_trades_by_transaction_date(date(2022, 10, 8), date(2022, 10, 10))

print(len(trades))
