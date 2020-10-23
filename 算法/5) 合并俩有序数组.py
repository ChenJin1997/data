def Merger(list1,m,list2,n):
    i = m-1
    j = n-1
    k = m+n-1
    while i>=0 and j>=0:
        if list1[i]>=list2[j]:
            list1[k] = list2[i]
            k -= 1
            i -= 1
        elif list1[i]<list2[j]:
            list1[k] = list2[j]
            k -= 1
            j -= 1
    while  i >= 0:
        list1[k] = list1[i]
        k -= 1
        i -= 1
    while j >= 0:
        list1[k] = list1[j]
        k -= 1
        j -= 1

