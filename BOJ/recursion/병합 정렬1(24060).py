def merge_sort(arr, k, n, number):
    if len(arr) < 2:
        return arr, k, number

    mid = len(arr) // 2
    low_arr, k, number = merge_sort(arr[:mid], k, n, number)
    high_arr, k, number = merge_sort(arr[mid:], k, n, number)

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            k += 1
            if k == n:
                number = low_arr[l]
                return merged_arr, k, number
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            k += 1
            if k == n:
                number = high_arr[h]
                return merged_arr, k, number

    for i in range(l, len(low_arr)):

        merged_arr.append(low_arr[i])
        k += 1
        if k == n:
            number = low_arr[i]
            return merged_arr, k, number
    for j in range(h, len(high_arr)):

        merged_arr.append(high_arr[j])
        k += 1
        if k == n:
            number = high_arr[j]
            return merged_arr, k, number
    return merged_arr, k, number


N, K = map(int, input().split(' '))
arr1 = list(map(int, input().split(' ')))
k = 0
number = 0
sorted_arr, k, number = merge_sort(arr1, k, K, number)
print(k)
if k < K:
    print(-1)
else:
    print(number)