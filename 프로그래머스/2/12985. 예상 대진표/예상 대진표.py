def solution(n,a,b):     
    round_cnt = 0
    while a != b:
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1     
        round_cnt += 1
    return round_cnt