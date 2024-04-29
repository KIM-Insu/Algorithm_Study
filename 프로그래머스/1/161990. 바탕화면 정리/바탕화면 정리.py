def solution(wallpaper):
    dict = {}
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            dict[i] = [j for j in range(len(wallpaper[i])) if wallpaper[i][j] == '#']

    keys = list(dict.keys())
    values = []
    for s in list(dict.values()):
        for t in s:
            values.append(t)
            values.sort()

    answer = [min(keys), min(values), max(keys) + 1, max(values) + 1]
    return answer