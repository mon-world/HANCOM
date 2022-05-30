import numpy as np

np.random.seed(41)
a = np.random.randint(0, 100, 12).reshape(-1, 4)
print(a, end='\n\n')

print(np.max(a))
print(np.max(a, axis=0), end='\n\n')

print(np.argmax(a))
print(np.argmax(a, axis=0), end='\n\n')

# labels: [desk, chair, lamp, computer, tv  ]
# argmax: [0.1   0.35    0.25  0.05     0.25]
#                  1
# print(labels[1])
print('-' * 30)

b = a.reshape(-1)       # flatten
print(b, end='\n\n')

c = b.argsort()         # 큰 순부터 작은 순으로
print(c)
print(b[c])             # 순서 큰 순 = 작은 숫자 순

# b.sort()
print(b)
print('-' * 30)

d = np.int32([1, 0, 3, 0, 0, 2])
r1 = np.nonzero(d)
print(r1)               # (array([0, 2, 5]),) 일관되지 않은 형식 (bad)
print(d[r1])

r1 = np.int32(r1)
print(r1)               # [[0 2 5]] 일관된 형식 (good)
print(d[r1])
print()

e = d.reshape(2, 3)
print(e)

r2 = np.nonzero(e)
print(r2)
print(e[r2])
