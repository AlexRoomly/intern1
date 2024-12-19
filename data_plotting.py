import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    '''
    Создаёт график, отображающий цены закрытия и скользящие средние.
    Предоставляет возможность сохранения графика в файл. Параметр filename опционален;
    если он не указан, имя файла генерируется автоматически.
    :param data: DataFrame с данными
    :param ticker: Название тикета, может принимать значения ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    :param period: Период предоставления данных:
                   ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    :param filename: Имя файла для сохранения изображения с графиком, по умолчанию имя файла будет
                     формироваться автоматически
    :return: Сообщение о сохранении графика в файл
    '''
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
