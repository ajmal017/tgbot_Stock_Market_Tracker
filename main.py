!pip install yfinance

import requests
import datetime
import yfinance as yf

API_TOKEN = '1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghi'  # replace your Bot Token
HTTP_URL = 'https://api.telegram.org/bot'
API_getMe = '/getMe'
API_getUpdates = '/getUpdates'
API_sendMessage = '/sendMessage'

def telegram_request(str_API_TOKEN, str_API_getMe, dict_payload, dict_headers):
  r = requests.post(HTTP_URL + str_API_TOKEN + str_API_getMe, params=dict_payload, headers=dict_headers)
  return r.json()

def get_yf_current_price(str_code):
  return yf.Ticker(str_code).history(period="1day")['Close'][0]

def get_yf_50davg(str_code):
  return yf.Ticker(str_code).info["fiftyDayAverage"]

myText = str(datetime.datetime.now()) + "\r\n" + "\r\n" \
          + "===== Index =====" + "\r\n"\
          + "HSI: " + str(get_yf_current_price("^HSI")) + " --50davg--> " + str(get_yf_50davg("^HSI")) + "\r\n"\
          + "S&P 500: " + str(get_yf_current_price("^GSPC")) + " --50davg--> " + str(get_yf_50davg("^GSPC")) + "\r\n"\
          + "Dow 30: " + str(get_yf_current_price("^DJI")) + " --50davg--> " + str(get_yf_50davg("^DJI")) + "\r\n"\
          + "===== Cryptocurrencies =====" + "\r\n"\
          + "Crypto 200: " + str(get_yf_current_price("^CMC200")) + " --50davg--> " + str(get_yf_50davg("^CMC200")) + "\r\n"\
          + "BTCUSD: " + str(get_yf_current_price("BTC-USD")) + " --50davg--> " + str(get_yf_50davg("BTC-USD")) + "\r\n"\
          + "ETHUSD: " + str(get_yf_current_price("ETH-USD")) + " --50davg--> " + str(get_yf_50davg("ETH-USD")) + "\r\n"\
          + "MCOUSD: " + str(get_yf_current_price("MCO-USD")) + " --50davg--> " + str(get_yf_50davg("MCO-USD")) + "\r\n"\
          + "===== Commodities =====" + "\r\n"\
          + "Gold: " + str(get_yf_current_price("GC=F")) + " --50davg--> " + str(get_yf_50davg("GC=F")) + "\r\n"\
          + "Silver: " + str(get_yf_current_price("SI=F")) + " --50davg--> " + str(get_yf_50davg("SI=F")) + "\r\n"\
          + "===== Forex =====" + "\r\n"\
          + "HKD-CNH: " + str(get_yf_current_price("HKDCNH=X")) + " --50davg--> " + str(get_yf_50davg("HKDCNH=X")) + "\r\n"\
          + "USD-HKD: " + str(get_yf_current_price("HKD=X")) + " --50davg--> " + str(get_yf_50davg("HKD=X")) + "\r\n"\
          + "SGD-HKD: " + str(get_yf_current_price("SGDHKD=X")) + " --50davg--> " + str(get_yf_50davg("SGDHKD=X")) + "\r\n"\
          + "\r\n" + "From Yahoo! Finance"

payload = {
    'chat_id': '@czglobalmarket',
    'text': myText,
    'parse_mode':'HTML'
}
telegram_request(API_TOKEN, API_sendMessage, payload, {})
