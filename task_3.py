class BaseConverter:

    def convert(self, celsius: float, target: str) -> float:
        if target.upper() == 'K':
            return celsius + 273.15
        elif target.upper() == 'F':
            return celsius * 9 / 5 + 32
        else:
            raise ValueError(
                'Ошибка. Пожалуйста, введите "K" для перевода '
                'в Кельвины или "F" для перевода в Фаренгейты.')


if __name__ == '__main__':
    converter = BaseConverter()

    while True:
        try:
            celsius = float(input('Введите температуру в градусах Цельсия: '))
            break
        except ValueError:
            print('Ошибка. Пожалуйста, введите число.')

    while True:
        target = input('В какую шкалу необходимо перевести градусы?'
                       '"K" - Кельвины, "F" - Фаренгейты. ').strip().upper()
        if target in ('K', 'F'):
            break
        print('Ошибка. Пожалуйста, введите "K" для перевода '
              'в Кельвины или "F" для перевода в Фаренгейты.')

    try:
        result = converter.convert(celsius, target)
        print(f'{celsius} C = {result} {target}')
    except ValueError as e:
        print(e)
