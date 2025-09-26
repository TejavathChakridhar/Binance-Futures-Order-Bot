import argparse
from .utils import send_signed_request
from .validate_and_log import validate_symbol, validate_quantity, log_info, log_error

ORDER_PATH = '/fapi/v1/order'

def place_market_order(symbol: str, side: str, quantity: float, reduce_only: bool = False):
    payload = {'symbol': symbol, 'side': side.upper(), 'type': 'MARKET', 'quantity': quantity, 'reduceOnly': str(reduce_only).lower()}
    return send_signed_request('POST', ORDER_PATH, payload)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Place a Binance Futures MARKET order')
    parser.add_argument('symbol')
    parser.add_argument('side', choices=['BUY', 'SELL', 'buy', 'sell'])
    parser.add_argument('quantity')
    args = parser.parse_args()
    try:
        symbol = validate_symbol(args.symbol)
        qty = validate_quantity(args.quantity)
        res = place_market_order(symbol, args.side, qty)
        log_info('Market order placed', symbol=symbol, side=args.side, quantity=qty, response=res.get('orderId'))
        print('Order response:', res)
    except Exception as e:
        log_error('Failed to place market order', error=str(e))
        print('Error:', e)
