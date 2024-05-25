#!/usr/bin/python3
def compute_matrix(matrix=[]):
     return list(map(lambda row: list(map(lambda num: num ** 2, row)), matrix))
if __name__=="__main__":
    matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
