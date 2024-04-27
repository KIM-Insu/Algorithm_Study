def solution(survey, choices):
    d = {'R': [], 'T': [], 'C': [], 'F': [], 'J': [], 'M': [], 'A': [], 'N': []}

    for i in range(len(survey)):
        if choices[i] < 4:                          
            d[survey[i][0]].append(4 - choices[i])  # 비동의 관련 선택지를 선택했다면 survey[i]의 첫 번째 캐릭터에 점수 
        elif choices[i] > 4:
            d[survey[i][1]].append(choices[i] - 4)  # 동의 관련 선택지를 선택했다면 survey[i]의 두 번째 캐릭터에 점수
        else: pass                                  # '모르겠음'을 선택했다면 어떤 성격 유형도 점수 X

    answer = ''
    for j in range(0, len(d), 2):                                     # 점수가 저장된 딕셔너리를 두칸씩 띄면서 순회
        if sum(d[list(d.keys())[j]]) >= sum(d[list(d.keys())[j+1]]):  # 두 성격유형 중 점수의 합이 더 높은 성격유형을 선택하고 저장
            answer += list(d.keys())[j]
        else:
            answer += list(d.keys())[j+1]
    return answer