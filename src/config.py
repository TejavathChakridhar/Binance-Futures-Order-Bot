import os

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
BASE_URL = os.getenv('BINANCE_FUTURES_BASE', 'https://fapi.binance.com')
RECV_WINDOW = 5000
LOG_FILE = os.getenv('BOT_LOG_FILE', 'bot.log')
TESTNET = os.getenv('TESTNET', '0') in ('1', 'true', 'True')

if TESTNET:
    BASE_URL = os.getenv('BINANCE_FUTURES_TESTNET', 'https://testnet.binancefuture.com')
