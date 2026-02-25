import random


def user_input() -> int:
    while True:
        user_input = input('Введите целое число от 1 до 10 '
                           '(количество значений в массиве): ')
        try:
            n = int(user_input)
            if 1 <= n <= 10:
                return n
        except ValueError:
            print(f'Ошибка: "{user_input}" не является целым числом. '
                  'Попробуйте снова.')


def num_array(array: list, n: int) -> int:
    min_value = min(array)
    max_value = max(array)
    avg_value = sum(array) / n

    return min_value, max_value, avg_value


if __name__ == '__main__':
    n = user_input()
    array = [random.random() for _ in range(n)]
    min_value, max_value, avg_value = num_array(array, n)
    print(f'Массив: {array} \n'
          f'Минимальное значение в массиве: {min_value} \n'
          f'Максимальное значение в массиве: {max_value} \n'
          f'Среднее значение в массиве: {avg_value}')
