def compare(x):                        # sort의 기준이 되는 함수 생성 (수의 비교를 위해 4 자릿수로 통일)
    if len(x) == 1:                    # 한 자릿수면 숫자를 4개 이어붙이기 (ex. 7 -> 7777)        
        return x * 4
    elif len(x) == 2:                  # 두 자릿수면 2번 이어붙이기 (ex. 76 -> 7676)  
        return x * 2
    elif len(x) == 3:                  # 세 자릿수면 맨 첫 글자 이어붙이기 (ex. 766 -> 7667)
        return x + x[0]
    else:
        return x

def solution(numbers):
    numbers = list(map(str, numbers))  # 리스트 원소를 전부 str로 변환
    numbers.sort(reverse= True, key= lambda x : compare(x)) # 만들어놓은 함수에 따라 내림차순으로 정렬
    answer = ''.join(numbers)          # 정렬된 리스트의 원소들을 순서대로 문자열로 저장
    
    if answer[0] == '0':               # [0,0,0,0] 같이 모든 원소가 0인 케이스는 "0"으로 출력 
        return '0'
    return answer
