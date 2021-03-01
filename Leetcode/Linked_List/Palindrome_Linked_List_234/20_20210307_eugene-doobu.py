
def isClosed(_lval, _rval):
    if _lval == '(' and _rval == ')':
        return True
    if _lval == '{' and _rval == '}':
        return True
    if _lval == '[' and _rval == ']':
        return True
    return False

class Solution:
    def isValid(self, s: str) -> bool:
        # diff : () - 1byte / [], {} - 2byte
        stack = []

        for c in s:
            stack.append(c)

            if len(stack) == 1:
                continue

            rval = stack.pop()
            lval = stack.pop()

            # check closed
            if isClosed(lval, rval):
                continue
            else:
                stack.append(lval)
                stack.append(rval)

        # result
        if not stack:
            return True
        else:
            return False
