def merge(arr, low, mid, high):  
    start1 = low
    start2 = mid + 1
    c = []
    while start1 <= mid and start2 <= high:
        if arr[start1] < arr[start2]: 
            c.append(arr[start1])
            start1 += 1
        else:
            c.append(arr[start2])
            start2 += 1

    while start1 <= mid:
        c.append(arr[start1])
        start1 += 1

    while start2 <= high:
        c.append(arr[start2])
        start2 += 1
    k = 0
    for i in range(low, high + 1):
        arr[i] = c[k]
        k += 1

def merge_sort(arr, low, high):  
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

arr = [5, 20, 40, 8, 7, 29, 9, 15, 14]
merge_sort(arr, 0, len(arr) - 1)
print(arr) 
