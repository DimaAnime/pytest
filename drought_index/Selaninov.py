def selaninov_drought_index(temperature, precipitation):
    """
    Вычисление индекса засухи Селянинова.

    Параметры:
    - temperature: Список ежемесячных значений температуры.
    - precipitation: Список ежемесячных значений осадков.

    Возвращаемое значение:
    - Значение индекса засухи Селянинова.
    """

    # Проверка, что длины списков температуры и осадков совпадают
    if len(temperature) != len(precipitation):
        print("Длины списков температуры и осадков должны быть одинаковыми.")
        return None
    elif len(precipitation)==0:
        print("Длины списка осадков должны быть больше 0.")
        return None

    # Вычисление средней температуры
    avg_temperature = sum(temperature) / len(temperature)

    # Вычисление суммы ежемесячных осадков
    total_precipitation = sum(precipitation)

    # Вычисление индекса засухи Селянинова
    kddi = avg_temperature / (total_precipitation / len(precipitation))

    return kddi

if __name__=="__main__":
    # Пример использования
    temperature_data = []
    precipitation_data = []

    index_result = selaninov_drought_index(temperature_data, precipitation_data)
    print(f"Индекс засухи Селянинова: {index_result}")
