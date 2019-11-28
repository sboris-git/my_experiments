matrix = [
    [1,  2,   3,   4],
    [5,  6,   7,   8],
    [9, 10, 11, 12]]

#print([[row[i] for row in matrix] for i in range(len(matrix))])

#classic
transposed = []
for i in range(len(matrix[0])):
    transposed.append([row[i] for row in matrix])

for row in transposed:
    print(row)
#use zip(*)
print(list(zip(*matrix)))
matrix1 = list(zip(*matrix))
print(list(zip(*matrix1)))
