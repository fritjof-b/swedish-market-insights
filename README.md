# Swedish Market Insights

SMI is a small package for fetching inside trades made in Sweden.
The data is collected with `requests` and parsed with `BeautifulSoup4`
and returned as a `pandas.DataFrame`.

All data is publicly available on Finansinspektionen's [website](https://fi.se/).

## Installation

```
pip install swedish-market-insights
```

## Usage

```python3
from swedish_market_insights.inside_trades import InsideTradesAPI
from swedish_market_insights.short_positions import ShortPositionsAPI

recent_inside_trades = InsideTradesAPI.get_trades_by_transaction_date()
current_short_positions = ShortPositionsAPI.get_current_short_positions()
```

## Features

### Inside Trades
- Fetch inside trades by transaction date
- Fetch inside trades by publication date

### Short Positions
- Fetch current short positions
- Fetch historical short positions
- Fetch aggregated short positions

## Examples

### Fetch inside trades by transaction date

```python3
from swedish_market_insights.inside_trades import InsideTradesAPI
from datetime import date

trades = InsideTradesAPI.get_trades_by_transaction_date(
    from_date=date(2020, 1, 1),
    to_date=date(2020, 1, 31))
```

### Fetch inside trades by publication date

```python3
from swedish_market_insights.inside_trades import InsideTradesAPI
from datetime import date

trades = InsideTradesAPI.get_trades_by_publish_date(
    from_date=date(2022, 10, 8),
    to_date=date(2022, 10, 10))
```

### Fetch current short positions

```python3
from swedish_market_insights.short_positions import ShortPositionsAPI

current_short_positions = ShortPositionsAPI.get_current_short_positions()
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have any suggestions or
improvements.

## License

This project is licensed under the MIT License.