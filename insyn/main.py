from insynsregistret import Insynsregistret

insynsregistret = Insynsregistret()

trades = insynsregistret.get_trades_by_publish_date()

for trade_entry in trades:
    print(trade_entry.date)
