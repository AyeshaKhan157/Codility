from itertools import combinations

def solution(S):
    max_len = 0
    letters = set(S)

    for k in range(1, 4):
        for combo in combinations(letters, k):
            allowed = set(combo)
            filtered = [c for c in S if c in allowed]

            # Now count blocks and total length
            blocks = []
            prev = ''
            count = 0

            for c in filtered:
                if c == prev:
                    count += 1
                else:
                    if prev:
                        blocks.append((prev, count))
                    prev = c
                    count = 1
            if prev:
                blocks.append((prev, count))

            if len(blocks) <= 3:
                total = sum(c for _, c in blocks)
                max_len = max(max_len, total)

    return max_len



print(solution("aaddddbacbba"))     
print(solution("aabxyuuubaba"))     
print(solution("wxxxyxxxxxyyyxyyy")) 
print(solution("abbnntheaxbtheb"))   

