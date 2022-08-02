import csv



def mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    length = len(numbers)
    mean = mean(numbers)

    s = 0
    for i in range(length-1):
        s += (numbers[i] - mean) ** 2

    return (s / (length - 1)) ** 0.5

if __name__ == 'main':
    with open('009-C105-StandardDeviation/csv/data.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(f"Standard deviation: {standard_deviation([float(i) for i in data[0]])}")