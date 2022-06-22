def search_1(l, S):
    if S in l:
        return [S]
    else:
        return []

def search_2(l, S):
    i=0
    j = len(l)-1
    while i<j:
        sum = l[i] + l[j]
        if sum == S:
            return [l[i], l[j]]
        
        elif sum<S:
            i+=1
        
        elif sum>S:
            j-=1
    
    return []


def recursive(l, N, S):
    if N == 1:
        return search_1(l, S)
    
    if N == 2:
        return search_2(l, S)

    else:
        i=0
        while i<=len(l)-N:
            res_search = recursive(l[i+1:], N-1, S-l[i])
            if res_search:
                return [l[i]] + res_search
            else:
                i+=1
                
    return []
    
    


def sum_n(l, N, S):
    if not l:
        return []

    if N>len(l):
        raise ValueError("N must be len N or less")
    
    if N<=0:
        raise ValueError("N must be 1 or more")

    return recursive(sorted(l), N, S)