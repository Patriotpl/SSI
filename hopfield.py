import numpy as np


SAMPLE1 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]
SAMPLE2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]
SAMPLE3 = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]
TEST1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0]
]
TEST2 = [
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
]
TEST3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
TEST4 = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1]
]

FIGURE_SIZE = 5
FLAT_SIZE = FIGURE_SIZE ** 2
SAMPLES = [SAMPLE1, SAMPLE2, SAMPLE3]
TESTS = [TEST1, TEST2, TEST3, TEST4]
weights = np.zeros((FLAT_SIZE, FLAT_SIZE))
flat = np.array([np.array(sample).flatten() for sample in SAMPLES])
flat = np.where(flat == 0, -1, flat)

for i in range(FLAT_SIZE):
    for j in range(FLAT_SIZE):
        if i == j:
            continue
        
        weights[i][j] = np.dot(flat[:, i], flat[:, j]) / FLAT_SIZE


for test in TESTS:
    flat = np.array(test).flatten()
    flat[flat == 0] = -1
    for i in range(FLAT_SIZE):
        summ = 0
        for j in range(FLAT_SIZE):
            if i == j:
                continue

            summ += flat[j] * weights[i][j]
        
        flat[i] = 1 if summ >= 0 else -1

    unflat = flat.reshape(FIGURE_SIZE, FIGURE_SIZE)
    unflat[unflat == -1] = 0

    print("pierwotny wzór:")
    for row in test:
        print(row)
    print("naprawiony wzór:")
    print(unflat)
    print()