class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[',
                ')':'(',
                '}':'{'}

        stack = []


        for i in s:
            if i in ']})':
                if not stack:
                    return False
                if stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)
        
        return len(stack) == 0