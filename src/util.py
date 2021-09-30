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


def get_points(x_max: int, x_min: int, y_max: int, y_min: int, x_value: int, y_value: int) -> dict:
    regions = (
        {"all_points_x": (x_min, x_value, x_max, x_max, x_max, x_value, x_min, x_min, x_min),
         "all_points_y": (y_min, y_min, y_min, y_value, y_max, y_max, y_max, y_value, y_min)
         })
    return regions
