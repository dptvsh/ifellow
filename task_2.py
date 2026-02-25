def find_duplicate(str: str) -> str:
    seen = set()
    duplicates = set()
    for char in str:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)

    if duplicates:
        return f'Повторяющиеся символы: {', '.join(duplicates)}'
    else:
        return 'Повторяющихся символов нет.'


if __name__ == '__main__':
    str = 'Hello'
    result = find_duplicate(str)
    print(result)
