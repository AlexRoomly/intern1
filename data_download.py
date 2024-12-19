import pandas as pd
import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    '''
    Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает DataFrame с данными.
    :param ticker: Название тикета, может принимать значения ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    :param period: Период предоставления данных:
                   ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    :return: DataFrame с данными
    '''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    '''
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    :param data: DataFrame с данными
    :param window_size: Размер окна для расчета среднего (по умолчанию 5 дней)
    :return: DataFrame с данными
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''
    Функция принимает DataFrame и вычисляет среднее значение колонки 'Close'.
    Результат выводится в консоль.
    :param data:DataFrame
    :return: Среднее по столбцу 'Close'
    '''
    result = data['Close'].mean()
    print('Среднее значение цены за период', result)
