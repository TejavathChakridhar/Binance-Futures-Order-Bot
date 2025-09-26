import argparse
from .utils import send_signed_request
from .validate_and_log import validate_symbol, validate_quantity, validate_price, log_info, log_error

ORDER_PATH = '/fapi/v1/order'

def place_limit_order(symbol: str, side: str, quantity: float, price: float, time_in_force: str = 'GTC'):
    payload = {'symbol': symbol, 'side': side.upper(), 'type': 'LIMIT', 'quantity': quantity, 'price': price, 'timeInForce': time_in_force}
    return send_signed_request('POST', ORDER_PATH, payload)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Place a Binance Futures LIMIT order')
    parser.add_argument('symbol')
    parser.add_argument('side', choices=['BUY', 'SELL', 'buy', 'sell'])
    parser.add_argument('quantity')
    parser.add_argument('price')
    args = parser.parse_args()
    try:
        symbol = validate_symbol(args.symbol)
        qty = validate_quantity(args.quantity)
        price = validate_price(args.price)
        res = place_limit_order(symbol, args.side, qty, price)
        log_info('Limit order placed', symbol=symbol, side=args.side, quantity=qty, price=price, response=res.get('orderId'))
        print('Order response:', res)
    except Exception as e:
        log_error('Failed to place limit order', error=str(e))
        print('Error:', e)
