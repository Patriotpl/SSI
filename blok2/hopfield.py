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

for test_no in range(len(TESTS)):
    print(f"sprawdzanie testu {test_no + 1}")
    weights = [[0] * len(TESTS[test_no][0])] * len(TESTS[test_no])
    network = [] * len(TESTS[test_no]) * len(TESTS[test_no][0])
    for i in range(len(network)):
        for j in range(len(network)):
            if j == i:
                continue

            summ = ... # weź wyjście z samej tabelki test