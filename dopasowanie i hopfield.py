## zachłanne dopasowaie

TEMPLATE1 = [
    [0, 0, 0, 1],  
    [0, 0, 1, 1],
    [0, 1, 0, 1], 
    [0, 0, 0, 1], 
    [0, 0, 0, 1]
]
TEMPLATE2 = [
    [0, 1, 1, 1],  
    [1, 0, 0, 1],
    [0, 0, 1, 0], 
    [0, 1, 0, 0], 
    [1, 1, 1, 1]
]
TEMPLATE3 = [
    [1, 1, 1, 0],  
    [0, 0, 0, 1],
    [1, 1, 1, 1], 
    [0, 0, 0, 1], 
    [1, 1, 1, 0]
]
TEST1 =  [
    [0, 0, 0, 0],  
    [0, 0, 1, 1],
    [0, 1, 1, 1], 
    [0, 0, 0, 1], 
    [0, 0, 0, 1]
]
TEST2 =  [
    [1, 1, 1, 1],  
    [0, 0, 0, 1],
    [1, 1, 1, 1], 
    [0, 0, 1, 1], 
    [1, 1, 1, 1]
]
TEST3 =  [
    [1, 1, 1, 1],  
    [0, 0, 0, 1],
    [0, 0, 1, 0], 
    [1, 1, 0, 0], 
    [1, 1, 1, 1]
]

for test_name, test_map in zip(["test1", "test2", "test3"], [TEST1, TEST2, TEST3]):
    difference_metrics = []
    print(f"{test_name}:")
    for template_name, template_map in zip(["template1", "template2", "template3"], [TEMPLATE1, TEMPLATE2, TEMPLATE3]):
        metric = 0
        min_distance = 1000                 # arbitrarily picked number bigger than any possible distance within given arrays
        for a_y in range(len(test_map)):
            for a_x in range(len(test_map[a_y])):
                if test_map[a_y][a_x] == 0:
                    continue

                for b_y in range(len(template_map)):
                    for b_x in range(len(template_map[b_y])):
                        if template_map[b_y][b_x] == 0:
                            continue

                        current_distance = abs(a_y - b_y) + abs(a_x - b_x)
                        if min_distance > current_distance:
                            min_distance = current_distance
                metric += min_distance
        difference_metrics.append((template_name, -metric))
        print(f"difference between {template_name}: {-metric}")
    print("closest template:", min(difference_metrics, key=lambda x: x[1]))
    print()
