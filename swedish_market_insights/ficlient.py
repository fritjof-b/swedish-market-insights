import logging
from datetime import date

import requests

from .soup_utils import get_trade_entries_from_page, find_href_for_next_page
from .trade import TradeEntry

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = "https://marknadssok.fi.se/Publiceringsklient/sv-SE/Search/Search?"


def _get_trades_by_date_query(
    from_query: str,
    to_query: str,
    from_date: date,
    to_date: date,
) -> list[TradeEntry]:
    """
    Helper function to fetch trades by date query.

    :param from_query: Query parameter name for the start date
    :param to_query: Query parameter name for the end date
    :param from_date: Start date
    :param to_date: End date
    :return: List of TradeEntry objects"""
    params = {from_query: from_date, to_query: to_date}

    result = []
    response = requests.get(BASE_URL, params=params)
    result += get_trade_entries_from_page(response.content)
    while next_page_href := find_href_for_next_page(response.content):
        next_page_url = f"{BASE_URL}{next_page_href}"
        logging.info(f"Fetching next page: {next_page_url}")
        response = requests.get(next_page_url)
        result += get_trade_entries_from_page(response.content)

    return result


class FiClient:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_trades_by_publish_date(
        from_date: date = date.today(), to_date: date = date.today()
    ) -> list[TradeEntry]:
        """
        Fetch trades by publish date.

        :param from_date: Start date
        :param to_date: End date
        :return: List of TradeEntry objects"""
        return _get_trades_by_date_query(
            "Publiceringsdatum.From", "Publiceringsdatum.To", from_date, to_date
        )

    @staticmethod
    def get_trades_by_transaction_date(
        from_date: date = date.today(), to_date: date = date.today()
    ) -> list[TradeEntry]:
        """
        Fetch trades by transaction date.

        :param from_date: Start date
        :param to_date: End date
        :return: List of TradeEntry objects"""
        return _get_trades_by_date_query(
            "Transaktionsdatum.From", "Transaktionsdatum.To", from_date, to_date
        )
