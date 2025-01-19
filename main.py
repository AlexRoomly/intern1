import data_download as dd
import data_plotting as dplt
import additional_functionality as adf


def main():
    """
    Основная функция, управляющая процессом загрузки, обработки данных и их визуализации.
    Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных,
    а затем передаёт результаты на визуализацию.
    """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc),"
          " GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л,"
          " с начала года, макс.")

    # ticker = 'AAPL'
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    # period = '3mo'
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Получить данные
    stock_data = dd.fetch_stock_data(ticker, period)

    # Добавление дополнительных технических индикаторов MACD.
    req_macd = None
    req_macd = input("Рассчитать дополнительные технические индикаторы MACD, введите 'y': ")
    if req_macd=='y':
        stock_data = dd.get_macd(ticker, period)

    # Вычислить среднюю цену закрытия акций за заданный период
    dd.calculate_and_display_average_price(stock_data)

    # Проверка порога колебания цены акций
    threshold = float(input('Введите пороговый процент колебания цены акций за период: '))
    dd.notify_if_strong_fluctuations(stock_data, threshold)

    # Возможность экспортировать данные в CSV формате
    req = input("Если хотите сохранить данные в CSV файл, введите 'y': ")
    if req == 'y':
        req_filename = input("Введите имя файла, с расширением '.csv': ")
        adf.export_data_to_csv(stock_data, req_filename)

    # Добавить скользящее среднее значение к данным
    stock_data = dd.add_moving_average(stock_data)

    # Создать график
    if req_macd:
        dplt.create_and_save_plot_macd(stock_data, ticker, period)
    else:
        dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
