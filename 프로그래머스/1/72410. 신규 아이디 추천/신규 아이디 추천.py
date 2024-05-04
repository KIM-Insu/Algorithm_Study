def solution(new_id):
    stack = []
    new_id = new_id.lower()
    special = '-_.'
    temp = ''

    for letter in new_id:
        if letter.isalpha() or letter.isdigit() or letter in special:     
            temp += letter
    # (3), (4)
    for letter in temp:
        if letter == '.':
            if not stack or stack[-1] == '.':
                continue
            else:
                stack.append(letter)
        else:
            stack.append(letter)
                    
    if not stack:
        stack.append('a')
        
    if len(stack) >= 16:
        while len(stack) > 15:
            stack.pop()
    
    if stack[-1] == '.':
        stack.pop()
            
    if len(stack) <= 2:
        while len(stack) < 3:
            stack.append(stack[-1])
    
    return ''.join(stack)