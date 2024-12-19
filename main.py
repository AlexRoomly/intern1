import data_download as dd
import data_plotting as dplt


def main():
    '''
    Основная функция, управляющая процессом загрузки, обработки данных и их визуализации.
    Запрашивает у пользователя ввод данных, вызывает функции загрузки и обработки данных,
    а затем передаёт результаты на визуализацию.
    '''
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

    # Вычислить среднюю цену закрытия акций за заданный период
    dd.calculate_and_display_average_price(stock_data)

    # Добавить скользящее среднее значение к данным
    stock_data = dd.add_moving_average(stock_data)

    # Создать график
    dplt.create_and_save_plot(stock_data, ticker, period)


if __name__ == "__main__":
    main()
