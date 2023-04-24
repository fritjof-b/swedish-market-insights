from dataclasses import dataclass
from datetime import date

from swedish_market_insights.utils import (
    date_from_string,
    is_relative,
    parse_price_from_string,
    parse_volume_from_string,
)


@dataclass(frozen=True)
class TradeEntry:
    date: "date"
    issuer: "str"
    person: "str"
    position: "str"
    relative: "bool"
    kind: "str"
    instrument_name: "str"
    instrument_type: "str"
    isin: "str"
    transaction_date: "date"
    volume: "int"
    volume_unit: "str"
    price: "float"
    currency: "str"
    status: "str"
    details: "str"

    @staticmethod
    def from_row(row) -> "TradeEntry":
        date = date_from_string(row[0])
        issuer = row[1]
        person = row[2]
        position = row[3]
        relative = is_relative(row[4])
        kind = row[5]
        instrument_name = row[6]
        instrument_type = row[7]
        isin = row[8]
        transaction_date = date_from_string(row[9])
        volume = parse_volume_from_string(row[10])
        volume_unit = row[11]
        price = parse_price_from_string(row[12])
        currency = row[13]
        status = row[14]  # TODO Maybe fetch link to report here instead
        details = row[15]

        return TradeEntry(
            date=date,
            issuer=issuer,
            person=person,
            position=position,
            relative=relative,
            kind=kind,
            instrument_name=instrument_name,
            instrument_type=instrument_type,
            isin=isin,
            transaction_date=transaction_date,
            volume=volume,
            volume_unit=volume_unit,
            price=price,
            currency=currency,
            status=status,
            details=details,
        )
