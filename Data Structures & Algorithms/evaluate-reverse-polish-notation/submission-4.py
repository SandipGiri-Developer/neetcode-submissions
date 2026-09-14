class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens :
            if s == "+":
               stack.append(stack.pop() + stack.pop())
            elif s == "-":
               a,b = stack.pop(),stack.pop()
               stack.append(int(b-a))
            elif s == "*":
               stack.append(stack.pop() * stack.pop())
            elif s == "/":
               a,b = stack.pop(),stack.pop()
               stack.append(int(b/a))   
            else:
                a = int(s)
                stack.append(a)
        return stack[0]        
        