SAMPLE1 = [[0, 0, 0, 1],  
[0, 0, 1, 1], 
[0, 1, 0, 1], 
[0, 0, 0, 1],
[0, 0, 0, 1]]
SAMPLE2 = [[0, 1, 1, 1], 
[1, 0, 0, 1],
[0, 0, 1, 0],
[0, 1, 0, 0],
[1, 1, 1, 1]]
SAMPLE3 = [[1, 1, 1, 0],  
[0, 0, 0, 1],
[1, 1, 1, 1],
[0, 0, 0, 1],
[1, 1, 1, 0]]
TEST1 = [[0, 0, 0, 0], 
[0, 0, 1, 1],
[0, 1, 1, 1],
[0, 0, 0, 1],
[0, 0, 0, 1]]
TEST2 = [[1, 1, 1, 1],
[0, 0, 0, 1],
[1, 1, 1, 1],
[0, 0, 1, 1],
[1, 1, 1, 1]]
TEST3 = [[1, 1, 1, 1],
[0, 0, 0, 1],
[0, 0, 1, 0],
[1, 1, 0, 0],
[1, 1, 1, 1]]
TEST4 = [[1, 1, 1, 1],
[0, 0, 0, 1],
[1, 1, 1, 1],
[0, 0, 1, 1],
[1, 1, 1, 1]]

SAMPLES = [SAMPLE1, SAMPLE2, SAMPLE3]
TESTS = [TEST1, TEST2, TEST3, TEST4]

for i in range(len(TESTS)):
    print(f"sprawdzanie testu {i + 1}")
    metrics = []
    for j in range(len(SAMPLES)):
        metric = 0
        for a_y in range(len(TESTS[i])):
            for a_x in range(len(TESTS[i][a_y])):
                if TESTS[i][a_y][a_x] == 0:
                    continue
                
                min_dist = 1000     # arbitrary value higher than any distance possible within given arrays
                for b_y in range(len(SAMPLES[j])):
                    for b_x in range(len(SAMPLES[j][b_y])):
                        if SAMPLES[j][b_y][b_x] == 0:
                            continue

                        dist = abs(a_y - b_y) + abs(a_x - b_x)    # manhattan dinstance
                        min_dist = min([dist, min_dist])
                metric += min_dist
        unsimilaritiy_a_b = metric

        metric = 0
        for a_y in range(len(SAMPLES[j])):
            for a_x in range(len(SAMPLES[j][a_y])):
                if SAMPLES[j][a_y][a_x] == 0:
                    continue
                
                min_dist = 1000     # arbitrary value higher than any distance possible within given arrays
                for b_y in range(len(TESTS[i])):
                    for b_x in range(len(TESTS[i][b_y])):
                        if TESTS[i][b_y][b_x] == 0:
                            continue

                        dist = abs(a_y - b_y) + abs(a_x - b_x)    # manhattan dinstance
                        min_dist = min([dist, min_dist])
                metric += min_dist
        unsimilaritiy_b_a = metric
        metrics.append(-(unsimilaritiy_a_b + unsimilaritiy_b_a))

    print(f"najbardziej podobny szablon: {metrics.index(max(metrics)) + 1}")
    print()