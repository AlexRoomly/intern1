from datetime import timedelta
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


def notify_if_strong_fluctuations(data, threshold):
    '''
    Функция будет вычислять максимальное и минимальное значения цены закрытия и сравнивать разницу
    с заданным порогом. Если разница превышает порог, пользователь получает уведомление.
    :param data: DataFrame
    :param threshold: порог колебаний в % за период
    :return: уведомление при выполнении условия
    '''
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    price_fluctuation = (max_price - min_price) / min_price * 100
    if price_fluctuation > threshold:
        notification = (f'Колебание цены акций превысило заданные {threshold} % за период и составило '
                        f'{price_fluctuation} %.')
        print(notification)


def get_macd(ticker, period):
    """
    Расчёт дополнительных технических индикаторов MACD.
    :param ticker: Название тикета, может принимать значения ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    :param period: Период предоставления данных:
                   ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    :return: DataFrame c рассчитанными параметрами MACD
    """

    def data_macd_func(stock1, data_start1, data_end1, data_len1):
        """
        Выбирает необходимое количество строк с данными в DataFrame для расчета MACD
        :param stock1: информация об акциях
        :param data_start1: начало периода
        :param data_end1: конец периода
        :param data_len1: длина DataFrame
        :return: DataFrame c необходимым количеством строк
        """
        data_start_m = data_start1 - timedelta(days=33)
        data_m = stock1.history(start=data_start_m, end=data_end1)
        len_data_m = len(data_m.index)
        while (len_data_m - data_len1) < 33:
            data_start_m -= timedelta(days=1)
            data_m = stock1.history(start=data_start_m, end=data_end1)
            len_data_m = len(data_m.index)
        return data_m

    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    cols = ['EMA_of_12', 'EMA_of_26', 'MACD_Main', 'MACD_Signal']
    data_len = len(data.index)
    data_start = data.index[0]
    data_end = data.index[data_len - 1] + timedelta(days=1)
    data_macd = data_macd_func(stock, data_start, data_end, data_len)
    data_macd = data_macd.reindex(columns=data_macd.columns.tolist() + cols)
    data_len = len(data_macd.index)
    for i in range(data_len - 11):
        mean_value = data_macd['Close'].iloc[i:i + 11].mean()
        data_mean = data_macd.index[i + 11]
        data_macd.loc[data_mean, 'EMA_of_12'] = mean_value
        if i < (data_len - 25):
            mean_value_26 = data_macd['Close'].iloc[i:i + 25].mean()
            data_mean_26 = data_macd.index[i + 25]
            data_macd.loc[data_mean_26, 'EMA_of_26'] = mean_value_26
    data_macd['MACD_Main'] = data_macd['EMA_of_12'] - data_macd['EMA_of_26']
    for i in range(25, data_len - 8):
        mean_value_m = data_macd['MACD_Main'].iloc[i:i + 8].mean()
        data_mean_m = data_macd.index[i + 8]
        data_macd.loc[data_mean_m, 'MACD_Signal'] = mean_value_m
    data_m1 = data_macd.iloc[33:]
    return data_m1
