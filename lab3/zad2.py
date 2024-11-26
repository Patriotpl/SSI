from math import dist

from random import choices
from statistics import mean

def k_means(data: list[list[float]], names: list[list[str]], n: int) -> dict:
    m = 4
    for i in range(len(data)):
        data[i] = [float(data[i][0]), float(data[i][1])]
    centers = choices(data, k=m)
    for _ in range(n):
        print(centers)
        groups = {}
        for i in range(len(centers)):
            groups[i] = []
        for i in range(len(data)):
            distances = [dist(data[i], x) for x in centers]
            u = min(distances)
            groups[distances.index(u)].append(data[i])
        centers = []
        for j in groups.keys():
            new_center = []
            new_center.append(mean([x[0] for x in groups[j]]))
            new_center.append(mean([x[1] for x in groups[j]]))
            centers.append(new_center)
        
        return groups

if __name__ == "__main__":
    with open("data/spiralka.txt", "r") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split())
    with open("data/spiralka-names.txt", "r") as f:
        lines = f.readlines()
    names = []
    for line in lines:
        names.append(line.split())

    k_means(data, names, 100)
