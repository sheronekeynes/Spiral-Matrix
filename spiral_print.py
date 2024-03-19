
def spiral_print(matrix):
    res=[]
    left,right=0,len(matrix[0])
    top,bottom=0,len(matrix)

    while left < right and top < bottom:

        #get every i in the row
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1

        #get every i in the right column

        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):
            break

        #get every i in the bottom row
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom-=1

        #get every i in the left col
        for i in range(bottom-1,top-1,-1):
            res.append(matrix[i][left])
        left+=1
    return res




m,n=map(int,input().split())
matrix=[]

for _ in range(m):
    row=[int(val) for val in input().split()]
    matrix.append(row)

result=spiral_print(matrix)
print(len(matrix))

for element in result:
    print(element,end=" ")



