def read_file(file_name: str):
    data = []
    with open(file_name, 'r') as file:
        try:
            line = file.readline()
            for number in map(int, line.split()):
                data.append(number)
        except MemoryError:
            return data
    return data


def min_of_numbers(numbers: list) -> int:
    result = numbers[0]
    for element in numbers:
        if element < result:
            result = element
    return result


def max_of_numbers(numbers: list) -> int:
    result = numbers[0]
    for element in numbers:
        if element > result:
            result = element
    return result


def sum_of_numbers(numbers: list) -> int:
    result = 0
    for element in numbers:
        result += element
    return result


def multiplication_of_numbers(numbers: list):
    result = 1
    for element in numbers:
        try:
            result *= element
        except OverflowError:
            result = float("inf")
    return result


def main_func(file_name='numbers.txt'):
    list_of_numbers = read_file(file_name)
    if not len(list_of_numbers) == 0:
        min_value = min_of_numbers(list_of_numbers)
        max_value = max_of_numbers(list_of_numbers)
        sum_value = sum_of_numbers(list_of_numbers)
        multiplication_value = multiplication_of_numbers(list_of_numbers)
        return min_value, max_value, sum_value, multiplication_value
    return None
