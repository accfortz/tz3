from random import randint


def create_file_with_numbers(file_name: str, number_of_numbers: int):
    with open(file_name, 'w') as f:
        for i in range(number_of_numbers):
            f.write(str(randint(-1000, 1000)))
            f.write(' ')


def create_wrong_file(file_name: str):
    with open(file_name, 'w') as f:
        f.write('1 4 2 3 foo')
