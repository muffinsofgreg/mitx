import math

def polysum(n, s):
    """
    Returns the sum of the area and square of the perimeter rounded to four
    decimal points.

    0.25*n*s**2
    -----------
    tan(pi/n)

    Input n number of sides, s length of each side
    """

    numerator = .25 * n * s**2
    denominator = math.tan(math.pi / n)

    area = numerator / denominator

    perimeter = n * s

    sum = round(area + perimeter**2, 4)

    return sum
