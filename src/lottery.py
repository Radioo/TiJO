from collections import Counter

def lottery(numbers, size):
    if not numbers or size is None:
        return []

    count = Counter(numbers)

    result = [num for num, freq in count.items() if freq == size]

    return result
