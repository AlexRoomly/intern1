import pandas as pd

# df = pd.DataFrame({'First': [1, 2, 3], 'Second': [4, 5, 6], 'Close': [4, 5, 6]})


def calculate_and_display_average_price(data):
    """
    Функция принимает DataFrame и вычисляет среднее значение колонки 'Close'.
    Результат выводится в консоль.
    """
    result = data['Close'].mean()
    print('Среднее значение ', result)

# calculate_and_display_average_price(df)
