def solution(park, routes):
    S = [[i,park[i].index("S")] for i in range(len(park)) if "S" in park[i]][0]
    current = S
    for i in routes:
        op, n = i.split(' ')
        n = int(n)
        if op == "E":
            if "X" not in park[current[0]][current[1] + 1 : current[1] + n + 1] and current[1] + n < len(park[0]):
                current[1] += n
        elif op == "W":
            if "X" not in park[current[0]][current[1] - n : current[1]] and current[1] - n >= 0:
                current[1] -= n
        elif op == "S":
            if current[0] + n < len(park):
                if "X" not in [park[current[0] + j + 1][current[1]] for j in range(n)]:
                    current[0] += n
        else:
            if current[0] - n >= 0:
                if "X" not in [park[current[0] - j - 1][current[1]] for j in range(n)]:
                    current[0] -= n
    return current