import pytest
from context import TradeEntry
from datetime import date


@pytest.fixture
def complete_trade_entry():
    te = TradeEntry(
        date=date(year=2022, month=11, day=18),
        issuer="Foobar Group AB",
        person="John Doe",
        position="Verkställande direktör (VD)",
        relative=True,
        kind="Förvärv",
        instrument_name="Foobar Group AB",
        instrument_type="Aktie",
        isin="SE0013372407",
        transaction_date=date(year=2022, month=11, day=18),
        volume=1000,
        volume_unit="Antal",
        price=1.85,
        currency="SEK",
        status="",
        details="Anmälan",
    )
    return te


@pytest.fixture
def complete_row():
    row = [
        "2022-11-18",
        "Foobar Group AB",
        "John Doe",
        "Verkställande direktör (VD)",
        "Ja",
        "Förvärv",
        "Foobar Group AB",
        "Aktie",
        "SE0013372407",
        "2022-11-18",
        "1 000",
        "Antal",
        "1,85",
        "SEK",
        "",
        "Anmälan",
    ]
    return row


def test_trade_entry_from_row_creation_successful(complete_row, complete_trade_entry):
    trade_entry_to_test = TradeEntry.from_row(complete_row)
    assert trade_entry_to_test == complete_trade_entry
