import logging
from .config import LOG_FILE

logger = logging.getLogger('binance_bot')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def validate_symbol(symbol: str):
    if not isinstance(symbol, str) or len(symbol) < 4:
        raise ValueError('Invalid symbol')
    return symbol.upper()

def validate_quantity(qty: float):
    q = float(qty)
    if q <= 0:
        raise ValueError('Quantity must be > 0')
    return q

def validate_price(price: float):
    p = float(price)
    if p <= 0:
        raise ValueError('Price must be > 0')
    return p

def log_info(msg: str, **kwargs):
    logger.info(msg + (' | ' + ' | '.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ''))

def log_error(msg: str, **kwargs):
    logger.error(msg + (' | ' + ' | '.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ''))

def log_debug(msg: str, **kwargs):
    logger.debug(msg + (' | ' + ' | '.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else ''))
