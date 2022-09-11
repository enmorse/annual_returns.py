from utils import calculate_variance, calculate_stddev


def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)


annual_returns = [0.02, 0.05, -0.04, 0.04, 0.02, -0.02,
                  0.01, 0.03, 0.05, 0.02]


annual_returns_percentage = [display_as_percentage(
    annual_return) for annual_return in annual_returns]
print('The historical annual rates of return are: {}'.format(
    ','.join(annual_returns_percentage)))


variance = calculate_variance(annual_returns)
print('The variance of the rates of return is', variance)


stddev = display_as_percentage(calculate_stddev(
    annual_returns))
print('The standard deviation of the rates of returns is', stddev)
