class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        stack=[]
        result=True
        for char in s:
            if char=='(' or char=='[' or char=='{':
                stack.append(char)

            if char==')':
                if not stack:
                    result=False
                    return result
                else:
                    a=stack.pop()
                    if a=='(':
                        continue
                    else:
                        result=False
                        return result
            if char==']':
                if not stack:
                    result=False
                    return result
                else:
                    a=stack.pop()
                    if a=='[':
                        continue
                    else:
                        result=False
                        return result
            if char=='}':
                if not stack:
                    result=False
                    return result
                else:
                    a=stack.pop()
                    if a=='{':
                        continue
                    else:
                        result=False
                        return result

        if not stack:
            return result
        else:
            return False
