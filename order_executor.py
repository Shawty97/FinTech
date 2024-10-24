import MetaTrader5 as mt5

# Öffne die Verbindung zur MetaTrader 5-Plattform
mt5.initialize()

# Definiere die Order-Parameter
symbol = "EURUSD"
volume = 0.1
price = 1.1000
stop_loss = 1.0900
take_profit = 1.1100

# Öffne eine neue Order
order = mt5.order_send({
    "action": mt5.TRADE_REQUEST_ACTIONS_DEAL,
    "type": mt5.ORDER_TYPE_BUY,
    "symbol": symbol,
    "volume": volume,
    "price": price,
    "stoploss": stop_loss,
    "takeprofit": take_profit
})

# Überprüfe den Status der Order
if order.retcode == mt5.TRADE_RETCODE_DONE:
    print("Order erfolgreich ausgeführt!")