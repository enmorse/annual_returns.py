from math import sqrt


def calculate_variance(dataset):
    mean = sum(dataset) / len(dataset)

    numerator = 0

    for data in dataset:
        numerator += (data - mean) ** 2

    return numerator / len(dataset)


def calculate_stddev(dataset):
    variance = calculate_variance(dataset)
    return sqrt(variance)