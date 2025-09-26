#!/usr/bin/env python3
"""
Test script to verify the Binance trading bot is working correctly.
This script checks various components without making actual trades.
"""
import os
import sys
import traceback

def test_imports():
    """Test if all modules can be imported successfully."""
    print("🧪 Testing module imports...")
    try:
        import src.config
        import src.utils
        import src.validate_and_log
        import src.market_orders
        import src.limit_orders
        print("✅ All modules imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during imports: {e}")
        return False

def test_config():
    """Test configuration setup."""
    print("\n🔧 Testing configuration...")
    try:
        from src.config import API_KEY, API_SECRET, BASE_URL, TESTNET
        
        # Check if API credentials are set
        if API_KEY and API_SECRET:
            print("✅ API credentials are configured")
            api_configured = True
        else:
            print("⚠️  API credentials not found in environment variables")
            print("   Set BINANCE_API_KEY and BINANCE_API_SECRET to test API calls")
            api_configured = False
        
        print(f"📡 Base URL: {BASE_URL}")
        print(f"🧪 Testnet mode: {'ON' if TESTNET else 'OFF'}")
        
        return api_configured
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_validation_functions():
    """Test validation and logging functions."""
    print("\n✅ Testing validation functions...")
    try:
        from src.validate_and_log import validate_symbol, validate_quantity, validate_price
        
        # Test symbol validation
        symbol = validate_symbol("BTCUSDT")
        print(f"✅ Symbol validation works: {symbol}")
        
        # Test quantity validation
        qty = validate_quantity("0.001")
        print(f"✅ Quantity validation works: {qty}")
        
        # Test price validation
        price = validate_price("50000.50")
        print(f"✅ Price validation works: {price}")
        
        return True
    except Exception as e:
        print(f"❌ Validation error: {e}")
        traceback.print_exc()
        return False

def test_utils():
    """Test utility functions (without making API calls)."""
    print("\n🛠️  Testing utility functions...")
    try:
        from src.utils import send_signed_request
        print("✅ Utility functions loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Utility error: {e}")
        return False

def test_order_modules():
    """Test order module functions (without placing actual orders)."""
    print("\n📊 Testing order modules...")
    try:
        from src.market_orders import place_market_order
        from src.limit_orders import place_limit_order
        print("✅ Order functions loaded successfully")
        print("   Note: No actual orders will be placed in this test")
        return True
    except Exception as e:
        print(f"❌ Order module error: {e}")
        return False

def test_api_connection():
    """Test API connection (if credentials are available)."""
    print("\n🌐 Testing API connection...")
    try:
        from src.config import API_KEY, API_SECRET
        if not API_KEY or not API_SECRET:
            print("⚠️  Skipping API test - credentials not configured")
            return True
        
        from src.utils import send_signed_request
        
        # Test with a safe endpoint that doesn't place orders
        print("📡 Testing connection to Binance API...")
        try:
            # This is a safe endpoint that just gets account information
            response = send_signed_request('GET', '/fapi/v2/account', {})
            print("✅ API connection successful!")
            print(f"   Account balance available: {len(response.get('assets', []))} assets")
            return True
        except Exception as api_error:
            print(f"❌ API connection failed: {api_error}")
            print("   This might be due to:")
            print("   - Invalid API credentials")
            print("   - Network connectivity issues")
            print("   - API permissions not set correctly")
            return False
            
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def run_comprehensive_test():
    """Run all tests and provide a comprehensive report."""
    print("🚀 Starting Binance Trading Bot Test Suite")
    print("=" * 50)
    
    tests = [
        ("Module Imports", test_imports),
        ("Configuration", test_config),
        ("Validation Functions", test_validation_functions),
        ("Utility Functions", test_utils),
        ("Order Modules", test_order_modules),
        ("API Connection", test_api_connection),
    ]
    
    results = {}
    for test_name, test_func in tests:
        results[test_name] = test_func()
    
    print("\n" + "=" * 50)
    print("📋 TEST RESULTS SUMMARY:")
    print("=" * 50)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:20} {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your bot is ready to use!")
        print("\n💡 Next steps:")
        print("   1. Set BINANCE_API_KEY and BINANCE_API_SECRET environment variables")
        print("   2. Test with small amounts first")
        print("   3. Use TESTNET=1 for testing")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    run_comprehensive_test()