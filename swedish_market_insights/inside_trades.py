import logging
from datetime import date

import pandas as pd
import requests

from .constants import INSIDE_TRADES_BASE_URL
from .soup_utils import get_trade_entries_from_page, find_href_for_next_page

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def _get_trades_by_date_query(
    from_query: str,
    to_query: str,
    from_date: date,
    to_date: date,
) -> pd.DataFrame:
    """
    Helper function to fetch trades by date query.

    :param from_query: Query parameter name for the start date
    :param to_query: Query parameter name for the end date
    :param from_date: Start date
    :param to_date: End date
    :return: List of TradeEntry objects"""
    params = {from_query: from_date, to_query: to_date}

    result = pd.DataFrame()
    response = requests.get(INSIDE_TRADES_BASE_URL, params=params)
    result = pd.concat(
        [result, get_trade_entries_from_page(response.content)], ignore_index=True
    )
    while next_page_href := find_href_for_next_page(response.content):
        next_page_url = f"{INSIDE_TRADES_BASE_URL}{next_page_href}"
        logging.info(f"Fetching next page: {next_page_url}")
        response = requests.get(next_page_url)
        result = pd.concat(
            [result, get_trade_entries_from_page(response.content)], ignore_index=True
        )

    return result


class InsideTradesAPI:

    @staticmethod
    def get_trades_by_publish_date(
        from_date: date = date.today(), to_date: date = date.today()
    ) -> pd.DataFrame:
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
    ) -> pd.DataFrame:
        """
        Fetch trades by transaction date.

        :param from_date: Start date
        :param to_date: End date
        :return: List of TradeEntry objects"""
        return _get_trades_by_date_query(
            "Transaktionsdatum.From", "Transaktionsdatum.To", from_date, to_date
        )
