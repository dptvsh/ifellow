def user_input() -> int:
    while True:
        try:
            h, m = input('Введите время в формате "час минута": ').split()
            hours = int(h)
            minutes = int(m)
            if hours > 24:
                print('Проверьте количество часов. '
                      'Пожалуйста, введите число от 0 до 23.')
            elif minutes > 60:
                print('Проверьте введенные минуты. '
                      'Пожалуйста, введите число от 0 до 59.')
            else:
                return hours, minutes
        except ValueError:
            print('Проверьте введенное время. '
                  'Пожалуйста, введите 2 целых числа.')


def calculate(hours: int, minutes: int) -> float:
    hours %= 12
    hour_angle = 30 * hours + 0.5 * minutes
    minute_angle = 6 * minutes
    total_angle = abs(hour_angle - minute_angle)

    return min(total_angle, 360 - total_angle)


if __name__ == '__main__':
    hours, minutes = user_input()
    angle = calculate(hours, minutes)
    print(f'В {hours:02d}:{minutes:02d} угол между стрелками составляет '
          f'{angle} градусов.')
