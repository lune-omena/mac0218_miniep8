def search_1(l, S):
    if S in l:
        return [S]
    else:
        return []



def recursive(l, N, S):
    if N == 1:
        return search_1(l, S)
    
    


def sum_n(l, N, S):
    if not l:
        return []

    if N>len(l):
        raise ValueError("N must be len N or less")
    
    if N<=0:
        raise ValueError("N must be 1 or more")

    return recursive(l, N, S)