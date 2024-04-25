def solution(survey, choices):
    d = {'R': [], 'T': [], 'C': [], 'F': [], 'J': [], 'M': [], 'A': [], 'N': []}

    for i in range(len(survey)):
        if choices[i] < 4:
            d[survey[i][0]].append(4 - choices[i])
        elif choices[i] > 4:
            d[survey[i][1]].append(choices[i] - 4)
        else: pass

    answer = ''
    for j in range(0, len(d), 2):
        if sum(d[list(d.keys())[j]]) >= sum(d[list(d.keys())[j+1]]):
            answer += list(d.keys())[j]
        else:
            answer += list(d.keys())[j+1]
    return answer