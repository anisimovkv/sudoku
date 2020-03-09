from functools import reduce

import numpy as np


def sudoku_solver(input: np.ndarray) -> np.ndarray:
    while np.any(input <= 0):
        input = find_variant(input)
    return input


def find_variant(input: np.ndarray) -> np.ndarray:
    all_elemnts: np.ndarray = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(3):
        start_row = i * 3
        stop_row = start_row + 3
        for j in range(3):
            start_column = j * 3
            stop_column = start_column + 3
            block: np.ndarray = input[
                                start_row:stop_row,
                                start_column:stop_column]
            for ii in range(start_row, stop_row):
                for jj in range(start_column, stop_column):
                    if input[ii, jj] != 0:
                        continue
                    row: np.ndarray = input[ii, :]
                    colum: np.ndarray = input[:, jj]
                    row_colum: np.ndarray = np.union1d(row, colum)
                    result: np.ndarray = np.union1d(row_colum, block)
                    values: np.ndarray = np.setdiff1d(all_elemnts, result)
                    if values.size == 1:
                        input[ii][jj] = values[0]
    return input
