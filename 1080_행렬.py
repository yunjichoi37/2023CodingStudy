from sys import stdin

def change(mat,k,l):
    for i in range(k,k+3):
        for j in range(l,l+3):
            mat[i][j] = 1 - mat[i][j]
    return mat
            

            

            


n, m = map(int, input().split())
matrix_first =[list(map(int, stdin.readline().rstrip()))for j in range(n)]
matrix_second = [list(map(int, stdin.readline().rstrip()))for j in range(n)]


count =0
for i in range(n-2):
    for j in range(m-2):
        if matrix_first[i][j] != matrix_second[i][j]:
            count+=1
            change(matrix_first,i,j)
if matrix_first == matrix_second:
    print(count)
else:
    print(-1)
            