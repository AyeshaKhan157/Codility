# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A, B):
    N = len(A)
    
    for r in range(N):
        valid = True
        for i in range(N):
            if A[i] == B[(i - r) % N]:
                valid = False
                break
        if valid:
            return r

    return -1

print(solution([1, 3, 5, 2, 8, 7], [7, 1, 9, 8, 5, 7])) 
