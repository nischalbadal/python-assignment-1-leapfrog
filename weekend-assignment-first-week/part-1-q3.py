
def isBalanced(s):
    openers = ['(', '{', '[']
    closers = {
        ')': '(', 
        '}': '{', 
        ']': '['
    }
    bracket_stack = []
    for c in s:
        if c in openers:
            bracket_stack.append(c)
        elif c in closers:
            if len(bracket_stack) == 0:
                return 'NO'

            if bracket_stack.pop() != closers[c]:
                return 'NO'

    if len(bracket_stack) > 0:
        return 'NO'

    return 'YES'
  
exp1 = input('Enter a string of Brackets: ')

print(isBalanced(exp1))
