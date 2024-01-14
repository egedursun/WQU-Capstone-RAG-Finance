import dotenv
import requests

dotenv.load_dotenv()
config = dotenv.dotenv_values()


MAX_TICKER_LIMIT = 32
MAX_FUNDAMENTAL_LIMIT = 1
MAX_DIVIDEND_LIMIT = 5
MAX_NEWS_LIMIT = 5
MAX_INDICATOR_LIMIT = 32


class PolygonClient:

    def __init__(self, url=config['POLYGON_API_URL'], key=config['POLYGON_API_KEY']):
        self.url = url
        self.key = key

    def get_tickers(self, ticker_symbol, time_window, start_date, end_date, is_adjusted, max_limit):
        if int(max_limit) > MAX_TICKER_LIMIT:
            max_limit = str(MAX_TICKER_LIMIT)
        url = f"{self.url}/v2/aggs/ticker/{ticker_symbol}/range/1/{time_window}/{start_date}/" \
              f"{end_date}?adjusted={is_adjusted}&sort=asc&limit={max_limit}&apiKey=" \
              f"{self.key}"
        response = requests.get(url)
        return response.json()

    def get_fundamental(self, ticker_symbol, timeframe, max_limit):
        if int(max_limit) > MAX_FUNDAMENTAL_LIMIT:
            max_limit = str(MAX_FUNDAMENTAL_LIMIT)
        url = f"{self.url}/vX/reference/financials?ticker={ticker_symbol}&" \
              f"timeframe={timeframe}&limit={max_limit}&apiKey={self.key}"
        response = requests.get(url)
        return response.json()

    def get_dividends(self, ticker_symbol, frequency, dividend_type, max_limit):
        if int(max_limit) > MAX_DIVIDEND_LIMIT:
            max_limit = str(MAX_DIVIDEND_LIMIT)
        url = f"{self.url}/v3/reference/dividends?ticker={ticker_symbol}&frequency={frequency}&" \
              f"dividend_type={dividend_type}&limit={max_limit}&apiKey={self.key}"
        response = requests.get(url)
        return response.json()

    def get_news(self, ticker_symbol, max_limit, start_date, end_date):
        if int(max_limit) > MAX_NEWS_LIMIT:
            max_limit = str(MAX_NEWS_LIMIT)
        url = f"{self.url}/v2/reference/news?ticker={ticker_symbol}&limit={max_limit}&apiKey={self.key}" \
              f"&published_utc.gte={start_date}&published_utc.lte={end_date}"
        # define additional URL parameters
        response = requests.get(url)
        return response.json()

    def get_technical_indicators(self,
                                 ticker_symbol,
                                 window,
                                 timespan,
                                 macd_short_window,
                                 macd_long_window,
                                 macd_signal_window,
                                 rsi_window,
                                 series_type,
                                 is_adjusted,
                                 max_limit):
        if int(max_limit) > MAX_INDICATOR_LIMIT:
            max_limit = str(MAX_INDICATOR_LIMIT)
        url_sma = f"{self.url}/v1/indicators/sma/{ticker_symbol}?timespan={timespan}&adjusted={is_adjusted}&" \
                  f"window={window}&series_type={series_type}&order=desc&limit={max_limit}&apiKey={self.key}"
        response_sma = requests.get(url_sma)

        url_ema = f"{self.url}/v1/indicators/ema/{ticker_symbol}?timespan={timespan}&" \
                  f"adjusted={is_adjusted}&window={window}&series_type={series_type}&expand_underlying=false&" \
                  f"order=desc&limit={max_limit}&apiKey={self.key}"
        response_ema = requests.get(url_ema)

        url_macd = f"{self.url}/v1/indicators/macd/{ticker_symbol}?timespan={timespan}&adjusted={is_adjusted}&" \
                   f"short_window={macd_short_window}&long_window={macd_long_window}&" \
                   f"signal_window={macd_signal_window}&series_type={series_type}&" \
                   f"expand_underlying=false&order=desc&limit={max_limit}&apiKey={self.key}"
        response_macd = requests.get(url_macd)

        url_rsi = f"{self.url}/v1/indicators/rsi/{ticker_symbol}?timespan={timespan}&adjusted={is_adjusted}&" \
                  f"window={rsi_window}&series_type={series_type}&expand_underlying=false&" \
                  f"order=desc&limit={max_limit}&apiKey={self.key}"
        response_rsi = requests.get(url_rsi)

        combined_response = {
            "Simple Moving Average (SMA)": response_sma.json(),
            "Exponential Moving Average (EMA)": response_ema.json(),
            "Moving Average Convergence Divergence (MACD)": response_macd.json(),
            "Relative Strength Index (RSI)": response_rsi.json()
        }

        return combined_response


if __name__ == "__main__":
    p = PolygonClient()
    # print(p.get_tickers("AAPL", "day", "2023-01-09", "2023-01-09", "true", "10"))
    # print(p.get_fundamental("AAPL", "annual", "10"))
    # print(p.get_dividends("AAPL", "4", "CD", "5"))
    # print(p.get_news("AAPL", "10", "2021-01-01", "2023-01-01"))
    # print(p.get_technical_indicators("AAPL", "50", "day", "10", "20", "5", "10", "close", "true", "10"))
    pass
