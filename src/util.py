"""
Util functions
"""
from typing import Tuple


def calculate_xy(x_max: int, x_min: int, y_max: int, y_min: int) -> Tuple[int, int]:
    """
    Formula to get X and Y values.

    X = x_min + (x_max-x_min)/2
    Y = y_min + (y_max-y_min)/2

    :return: A tuple, X and Y values, int values
    """
    x_min_tmp = int(x_max - x_min) / 2
    x_value = int(x_min + x_min_tmp)

    y_min_temp = int(y_max - y_min) / 2
    y_value = int(y_min + y_min_temp)

    return x_value, y_value
