# transpose.py
"""
A script defining `transpose()` function that transposes a list of lists.
"""
def transpose(matrix: list[list]) -> list[list]:
    """Tranapose `matrix`. Raise error if matrix is not a list of same-length lists."""
    return [list(columns) for columns in zip(*matrix, strict=True)]
    

# base problem
assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
csv_data = [
    ["Mary's Coffee", "3.50", "Dining"],
    ["Spirit", "187.00", "Travel"],
    ["Joe's Eats", "24.28", "Dining"],
    ["Metro", "12.00", "Travel"],
    ["Lyft", "23.45", "Travel"],
    ["Lyft", "4.00", "Travel"],
    ["Mary's Coffee", "6.75", "Dining"],
]
merchants, costs, categories = transpose(csv_data)
total_cost = sum(float(c) for c in costs)
assert total_cost == 260.98