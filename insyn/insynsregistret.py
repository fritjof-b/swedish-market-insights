from datetime import date
from typing import List

import requests
from soup_utils import get_trade_entries_from_page
from trade import TradeEntry

BASE_URL = "https://marknadssok.fi.se/Publiceringsklient/sv-SE/Search/Search?"


class Insynsregistret:
    def __init__(self) -> None:
        pass

    def _get_trades_by_date_query(
        self,
        from_query: str,
        to_query: str,
        from_date: date,
        to_date: date,
    ) -> List[TradeEntry]:
        params = {from_query: from_date, to_query: to_date}

        result = []
        response = requests.get(BASE_URL, params=params)
        page_trade_entries = get_trade_entries_from_page(response.content)
        result += page_trade_entries
        return result

    def get_trades_by_publish_date(
        self, from_date: date = date.today(), to_date: date = date.today()
    ) -> List[TradeEntry]:
        return self._get_trades_by_date_query(
            "Publiceringsdatum.From", "Publiceringsdatum.To", from_date, to_date
        )

    def get_trades_by_transaction_date(
        self, from_date: date = date.today(), to_date: date = date.today()
    ) -> List[TradeEntry]:
        return self._get_trades_by_date_query(
            "Transaktionsdatum.From", "Transaktionsdatum.To", from_date, to_date
        )
