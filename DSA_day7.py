# 1. Implement Stack using List
stack = []
# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push:", stack)
# Pop element
popped = stack.pop()
print("Popped element:", popped)
print("Stack after pop:", stack)

# 2. Check Valid Parentheses

def is_valid_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack
test_string = "{[()]}"
print("Is valid parentheses?", is_valid_parentheses(test_string))