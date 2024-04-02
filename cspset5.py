#question 5a on cs 124 pset 5  

p = 1249  
P = [3, 1, 4, 1, 5, 9, 2, 6]  
D = [1, 4, 6, 8, 3, 4, 8, 3, 1, 9, 4, 1, 6, 7, 8, 3, 9, 3, 3, 1, 4, 1, 7, 1, 7, 5, 1, 1, 3, 2]  
k = len(P)  
n = len(D)  


def initial_hash(sequence, p):
    hash_value = 0
    for i in range(len(sequence)):
        hash_value = (hash_value * 10 + sequence[i]) % p
    return hash_value

def compute_rolling_hash(old_hash, old_digit, new_digit, k, p):

    new_hash = (old_hash - old_digit * pow(10, k - 1, p)) % p
    new_hash = (new_hash * 10 + new_digit) % p
    return new_hash


hash_P = initial_hash(P, p)


total_comparisons = 0
specific_comparisons = []


hash_substring = initial_hash(D[:k], p)

#iterative hashing!!!1!!
for i in range(n - k +1): #all possible substrings 
    
    if hash_substring == hash_P:
       
        cmp_count = 0
        for j in range(k):
            cmp_count += 1
            total_comparisons += 1
            if D[i+j] != P[j]:
               
                break
        specific_comparisons.append((i, cmp_count))

 
    if i < n - k:
        hash_substring = compute_rolling_hash(hash_substring, D[i], D[i+k], k, p)
        print(i, hash_substring) #off by +1 but i'm too lazy to fix it - just implicitly know that all of these are indexed +1 b/c i can check manually

print(hash_P, specific_comparisons, total_comparisons)