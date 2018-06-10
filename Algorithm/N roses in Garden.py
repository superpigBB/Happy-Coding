def solution(p, k):
    """
    type p: list[]
    type k: int
    type found : int
    """
    n = len(p)
    l = [1] * n
    found = 0
    if n == k:
        found = 1
        # print 'found::: ', found
        return n
    else:
        while n >= 2:
            index = p.pop() - 1
            l[index] = 0
            total = 0
            for i in l:
                if i == 0:
                    if total == k:
                        break
                    total = 0
                    continue
                else:
                    total += i
            if total == k and total != 0:
                found = 1
                # print 'found~~~', found
                return n - 1
            n -= 1
        if found == 0:
            return -1


print(solution([3, 1, 5, 4, 2], 1))
