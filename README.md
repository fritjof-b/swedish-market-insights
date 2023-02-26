# Insynsregistret

Insynsregistret is a small package for fetching inside trades made in Sweden.
The data is collected with `requests` and parsed with `BeautifulSoup4`.
All data is publicly available on Finansinspektionen's [website](https://fi.se/).

<!-- ## Installation -->

<!-- `pip install insyn` -->

## Usage

```python3
from insyn import insynsregistret

api = insynsregistret.Insynsregistret()
recent_inside_trades = api.get_trades_by_transaction_date()
```