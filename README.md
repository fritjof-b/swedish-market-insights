# Swedish Market Insights

SMI is a small package for fetching inside trades made in Sweden.
The data is collected with `requests` and parsed with `BeautifulSoup4`.
All data is publicly available on Finansinspektionen's [website](https://fi.se/).

## Installation

```
pip install insyn
```

## Usage

```python3
from swedish_market_insights import ficlient

api = ficlient.FiClient()
recent_inside_trades = api.get_trades_by_transaction_date()
```

## Features

- Fetch inside trades by transaction date
- Fetch inside trades by publication date

## Examples

### Fetch inside trades by transaction date

```python3
from swedish_market_insights import ficlient
from datetime import date

api = ficlient.FiClient()
trades = api.get_trades_by_transaction_date(
    from_date=date(2020, 1, 1),
    to_date=date(2020, 1, 31))
```

### Fetch inside trades by publication date

```python3
from datetime import date
from swedish_market_insights import ficlient

api = ficlient.FiClient()
trades = api.get_trades_by_publish_date(
    from_date=date(2022, 10, 8),
    to_date=date(2022, 10, 10))
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub if you have any suggestions or
improvements.

## License

This project is licensed under the MIT License.