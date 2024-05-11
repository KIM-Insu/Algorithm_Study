def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    answer = 0
    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer