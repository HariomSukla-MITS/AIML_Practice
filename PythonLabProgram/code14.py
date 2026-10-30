A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

rows = len(A)
cols = len(A[0])

result = [
    [0 for j in range(cols)]
    for i in range(rows)
]

for i in range(rows):
    for j in range(cols):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

print("Sum of Matrices:")
for row in result:
    print(row)