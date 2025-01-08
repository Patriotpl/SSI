SAMPLE1 = [[1, 1, 0, 0, 0],  
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0]]
SAMPLE2 = [[1, 0, 0, 0, 1],  
[0, 1, 0, 1, 0],
[0, 0, 1, 0, 0],
[0, 1, 0, 1, 0],
[1, 0, 0, 0, 1]]
SAMPLE3 = [[0, 0, 1, 0, 0],  
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 1, 0, 0],
[0, 0, 1, 0, 0]]
TEST1 = [[0, 1, 0, 0, 0],  
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 0]]
TEST2 = [[1, 1, 0, 0, 1],  
[0, 1, 0, 1, 0],
[0, 1, 1, 1, 0],
[0, 1, 0, 1, 0],
[1, 1, 0, 0, 1]]
TEST3 = [[0, 0, 0, 0, 0],  
[0, 0, 1, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0]]
TEST4 = [[0, 1, 1, 1, 1],  
[1, 0, 1, 1, 1],
[1, 0, 1, 1, 1],
[1, 0, 1, 1, 1],
[1, 0, 1, 1, 1]]

SAMPLES = [SAMPLE1, SAMPLE2, SAMPLE3]
TESTS = [TEST1, TEST2, TEST3, TEST4]
weights = [[0] * len(TESTS[0]) ** 2] * len(TESTS[0]) ** 2
out = [-1] * len(weights[0])

for i in range(100):
    for sample_no in range(len(SAMPLES)):
        for i in range(len(out)):
            summ = 0
            for j in range(len(out)):
                if i == j:
                    continue
                summ += weights[j][i] * out[j]
            out[i] = 1 if summ >= 0 else -1
        for i in range(len(TESTS[sample_no])):
            for j in range(len(TESTS[sample_no][i])):
                if i == j:
                    continue
                weights[j][i] += 1 / len(TESTS[sample_no]) * out[j] * out[i]

for test_no in range(len(TESTS)):
    first_time = True
    for i in range(len(out)):
        summ = 0
        for j in range(len(out)):
            if i == j:
                continue
            summ += weights[j][i] * out[j]
        out[i] = 1 if summ >= 0 else 0      # usually this'd be -1, but we can convert it for this excersize, by just changing -1 to 0
    first_time = False
    for i in range(len(out)):
        summ = 0
        for j in range(len(out)):
            if i == j:
                continue
            summ += weights[j][i] * out[j]
        out[i] = 1 if summ >= 0 else 0      # usually this'd be -1, but we can convert it for this excersize, by just changing -1 to 0
    print(out)