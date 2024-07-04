from collections import defaultdict
T = defaultdict(int)
T['zero'] = 0
T['three'] = 3
T['one'] = 1

for key, value in T.items():
    print(key, value)
    
for K in T:
    print(K, T[K])

T = sorted(T, key = lambda x: x[1])
print(T)
