def solution(n, lost, reserve):
    student = [i for i in range(1, n + 1)]
    lost.sort()
    reserve.sort()
    for i in lost:
        student.remove(i)
    for j in reserve:
         if j not in student:
            student.append(j)
    reserve = [i for i in reserve if i not in lost]
    if 1 in reserve and 2 not in student:
        student.append(2)
        reserve.remove(1)
    if n in reserve and n-1 not in student:
        student.append(n-1)
        reserve.remove(n)
    for i in reserve:
        if i > 1 and i-1 not in student:
            student.append(i-1)
        elif i < n and i+1 not in student:            
            student.append(i+1)
    return len(student)