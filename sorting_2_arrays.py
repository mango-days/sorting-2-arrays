# If you have two sorted arrays, how can you merge them and keep the resulting array sorted?

arr1 = [ 1, 3, 5, 7, 9 ]
arr2 = [ 2, 4, 6, 8, 10 ]

ans = []
index1 = 0
index2 = 0

while ( index1!=len(arr1) or index2!=len(arr2) ) :
    if arr1 [ index1 ] > arr2 [ index2 ] :
        ans.append ( arr2 [ index2 ] )
        index2 += 1
    elif arr2 [ index2 ] > arr1 [ index1 ] :
        ans.append ( arr1 [ index1 ] )
        index1 += 1
    else :
        ans.append ( arr2 [ index2 ] )
        index2 += 1
        ans.append ( arr1 [ index1 ] )
        index1 += 1
    
    if index2 == len(arr2) :
        while index1 != len(arr1) :
            ans.append ( arr1 [ index1 ] )
            index1 += 1
        break    
    elif index1 == len(arr1) :
        while index2 != len(arr2) :
            ans.append ( arr2 [ index2 ] )
            index2 += 1
        break
    if len(ans) == len(arr1) + len(arr2) : break

print (ans)