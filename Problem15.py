n = 21
Matrix = [[0 for x in range(n)] for x in range(n)]
for i in range(n): 
    Matrix[i][0] = 1
for i in range(n):
    Matrix[0][i] = 1
i = 1
j = 1
while i < n:
    j = 1
    while j < n:
        Matrix[i][j] = Matrix[i-1][j] + Matrix[i][j-1]
        j += 1
    i += 1
print(Matrix[-1][-1])
