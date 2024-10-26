# list_operations.py

def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    min_pos = numbers.index(min_value)
    max_pos = numbers.index(max_value)
    return min_value, min_pos, max_value, max_pos

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_position(numbers, value):
    try:
        return numbers.index(value)
    except ValueError:
        return -1