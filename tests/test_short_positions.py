import pandas as pd
import pytest
import responses

from swedish_market_insights.short_positions import ShortPositionsAPI

SHORT_POSITIONS_BASE_URL = "https://fi.se/en/our-registers/net-short-positions/"


def read_mock_ods_file() -> bytes:
    with open("tests/mock_short_positions.ods", "rb") as f:
        return f.read()


@responses.activate
def test_get_current_short_positions():
    responses.add(
        responses.GET,
        f"{SHORT_POSITIONS_BASE_URL}GetAktuellFile",
        body=read_mock_ods_file(),
        status=200,
    )

    df = ShortPositionsAPI.get_current_short_positions()
    assert isinstance(df, pd.DataFrame)


@responses.activate
def test_get_historical_short_positions():
    responses.add(
        responses.GET,
        f"{SHORT_POSITIONS_BASE_URL}GetHistFile",
        body=read_mock_ods_file(),
        status=200,
    )

    df = ShortPositionsAPI.get_historical_short_positions()
    assert isinstance(df, pd.DataFrame)


@responses.activate
def test_get_aggregated_short_positions():
    responses.add(
        responses.GET,
        f"{SHORT_POSITIONS_BASE_URL}GetBlankningsregisterAggregat",
        body=read_mock_ods_file(),
        status=200,
    )

    df = ShortPositionsAPI.get_aggregated_short_positions()
    assert isinstance(df, pd.DataFrame)
