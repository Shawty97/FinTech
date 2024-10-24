import bookmap

# Öffne die Verbindung zur Bookmap-Plattform
bm = bookmap.Bookmap()

# Definiere die Order-Parameter
symbol = "EURUSD"
volume = 0.1
price = 1.1000
stop_loss = 1.0900
take_profit = 1.1100

# Öffne eine neue Order
order = bm.place_order({
    "symbol": symbol,
    "volume": volume,
    "price": price,
    "stop_loss": stop_loss,
    "take_profit": take_profit
})

# Überprüfe den Status der Order
if order.status == bookmap.OrderStatus.OPEN:
    print("Order erfolgreich ausgeführt!")