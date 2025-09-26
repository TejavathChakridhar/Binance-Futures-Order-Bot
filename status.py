#!/usr/bin/env python3
"""
Quick status check for the Binance trading bot.
Run this to see if your bot is configured and ready to use.
"""
import os

def check_status():
    print("🤖 Binance Trading Bot Status Check")
    print("=" * 40)
    
    # Check environment variables
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    testnet = os.getenv('TESTNET', '0')
    
    print(f"API Key: {'✅ Set' if api_key else '❌ Not set'}")
    print(f"API Secret: {'✅ Set' if api_secret else '❌ Not set'}")
    print(f"Testnet Mode: {'🧪 ON' if testnet in ('1', 'true', 'True') else '🔴 OFF (Live trading)'}")
    
    # Quick import test
    try:
        import src.config
        print("Configuration: ✅ Working")
    except Exception as e:
        print(f"Configuration: ❌ Error - {e}")
        return False
    
    print("\n💡 Usage Examples:")
    print("Market Order: python -m src.market_orders BTCUSDT buy 0.001")
    print("Limit Order:  python -m src.limit_orders BTCUSDT buy 0.001 45000")
    print("Full Test:    python test_bot.py")
    
    if not api_key or not api_secret:
        print("\n⚠️  To enable trading, set your API credentials:")
        print("$env:BINANCE_API_KEY='your_api_key_here'")
        print("$env:BINANCE_API_SECRET='your_api_secret_here'")
        print("$env:TESTNET='1'  # For testing")
    
    return True

if __name__ == "__main__":
    check_status()