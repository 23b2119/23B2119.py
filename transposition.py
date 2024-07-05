# 転置のやり方
# zip()の使い方

DX = [1, 1, 1]
DY = [0, 0, 0]
DZ = [1, 1, 1]

for dx, dy, dz in zip(DX, DY, DZ):
    print(dx, dy, dz)
    
print('==========')

D = [[1, 1, 1],
    [0, 0, 0],
    [1, 1, 1]]
    
for d in zip(*D):
    print(d)

