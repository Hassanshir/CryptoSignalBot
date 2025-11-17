import requests
import time
import hashlib
import hmac

API_KEY = "اینجا کلید API"
API_SECRET = "اینجا سکرت API"

BASE_URL = "https://api.toobit.com"

def sign(params):
    query = "&".join([f"{k}={v}" for k, v in params.items()])
    signature = hmac.new(API_SECRET.encode(), query.encode(), hashlib.sha256).hexdigest()
    return signature

def get_volume(symbol="BTCUSDT"):
    path = "/api/v1/market/ticker"
    params = {
        "symbol": symbol
    }
    r = requests.get(BASE_URL + path, params=params)
    data = r.json()

    return {
        "price": data['data']['lastPrice'],
        "volume": data['data']['vol']
    }

if __name__ == "__main__":
    info = get_volume()
    print(info)
