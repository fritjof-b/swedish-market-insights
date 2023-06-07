import logging
from io import BytesIO

import pandas as pd
import requests

from .constants import SHORT_POSITIONS_BASE_URL

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


N_SKIP_ROWS = 5


class ShortPositionsAPI:
    @staticmethod
    def get_current_short_positions() -> pd.DataFrame:
        logging.info("Fetching current short positions")
        return ShortPositionsAPI._fetch_file_by_type("GetAktuellFile")

    @staticmethod
    def get_historical_short_positions() -> pd.DataFrame:
        logging.info("Fetching historical short positions")
        return ShortPositionsAPI._fetch_file_by_type("GetHistFile")

    @staticmethod
    def get_aggregated_short_positions() -> pd.DataFrame:
        logging.info("Fetching aggregated short positions")
        return ShortPositionsAPI._fetch_file_by_type("GetBlankningsregisterAggregat")

    @staticmethod
    def _fetch_file_by_type(file_type: str) -> pd.DataFrame:
        response = requests.get(f"{SHORT_POSITIONS_BASE_URL}{file_type}")
        response.raise_for_status()

        file_content = BytesIO(response.content)

        df = pd.read_excel(file_content, engine="odf", skiprows=N_SKIP_ROWS)
        return df
