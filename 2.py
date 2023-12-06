#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def extremum_function(type='max'):
    """
    Функция-замыкание, возвращающая внутреннюю функцию для нахождения минимального или максимального значения.
    По умолчанию type равен 'max'.
    """
    def find_extremum(collection):
        """
        Внутренняя функция для нахождения минимального или максимального значения в коллекции.
        """
        if type == 'max':
            return max(collection)
        elif type == 'min':
            return min(collection)
        else:
            raise ValueError("Некорректное значение параметра type. Допустимые значения: 'min' или 'max'.")

    return find_extremum

if __name__ == "__main__":
    my_collection = [3, 7, 1, 5, 9]

    # Создаем функцию-замыкание для поиска максимального значения (по умолчанию)
    max_extremum_func = extremum_function()
    max_result = max_extremum_func(my_collection)
    print("Максимальное значение в коллекции:", max_result)

    # Создаем функцию-замыкание для поиска минимального значения
    min_extremum_func = extremum_function(type='min')
    min_result = min_extremum_func(my_collection)
    print("Минимальное значение в коллекции:", min_result)
