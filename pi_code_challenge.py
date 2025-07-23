def solution(P, Q):
    from itertools import combinations

    n = len(P)
    
    unique_letters = set(P + Q)
    letter_list = list(unique_letters)
    k = len(letter_list)  
    letter_index = {ch: i for i, ch in enumerate(letter_list)}  
    options = [(letter_index[P[i]], letter_index[Q[i]]) for i in range(n)]

    min_distinct = k  
    for mask in range(1, 1 << k):
        valid = True
        for a, b in options:
            if not ((mask >> a) & 1 or (mask >> b) & 1):
                valid = False
                break
        if valid:
            cnt = bin(mask).count('1')
            min_distinct = min(min_distinct, cnt)

    return min_distinct
