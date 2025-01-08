import pandas as pd

"""
Модуль содержит дополнительные функции:
позволяет экспортировать данные в CSV формате.
"""


def export_data_to_csv(data, filename):
    """
    Функция позволяет сохранять загруженные данные об акциях в CSV файл.
    :param data: DataFrame
    :param filename: имя файла
    :return: Сообщение о сохранении данных в файл
    """
    data.to_csv(filename, index=False)
    print(f"Данные сохранены в {filename}.")
