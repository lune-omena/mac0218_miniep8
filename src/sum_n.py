def sum_n(l, N, S):
    if not l:
        return []

    if N>len(l):
        raise ValueError("N must be len N or less")
    
    if N<=0:
        raise ValueError("N must be 1 or more")