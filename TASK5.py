#Addition - nested loops
m1 = [[51,45,34],[67,85,16],[5,89,1]]
m2 = [[14,6,23],[26,7,23],[48,10,0.5]]
res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] = m1[i][j] + m2[i][j]

print(res)

#Subtraction
m1 = [[11,10,5],[9,21,256],[24,9,15]]
m2 = [[6,3,2],[4,11,250],[12,3,8]]
res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j] = m1[i][j] - m2[i][j]

print(res)

#Multiplication
m1 = [[11,10,5],[9,21,256],[24,9,15]]
m2 = [[6,3,2],[4,11,250],[12,3,8]]
res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        res[i][j] = m1[i][j] * m2[i][j]

print(res)

#A=B*C –2*(B+C)

B = [[14,6,23],[26,7,23],[48,10,5]]
C = [[6,3,2],[4,11,250],[12,3,8]]
A = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(B)):
    for j in range(len(C[0])):
        res[i][j] = B[i][j] * C[i][j] - 2 * (B[i][j] + C[i][j])

print(res)