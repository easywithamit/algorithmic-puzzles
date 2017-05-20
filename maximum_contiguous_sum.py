def maximum_contiguous_sum(a):
    n = len(a)
    local_sum = global_sum = a[0]
    for i in xrange(1,n):
        local_sum = max(local_sum+a[i],a[i])
        if local_sum > global_sum:
            global_sum = local_sum
    return global_sum

def maximum_contiguous_sum_non_adjacent(a,n):
    if n==0:
        return a[0]
    elif n==1:
        return max(a[n],a[n-1])
    else:
        return max(
            a[n]+maximum_contiguous_sum_non_adjacent(a,n-2),
            maximum_contiguous_sum_non_adjacent(a,n-1)
        )

def maximum_contiguous_sum_non_adjacent_dp(arr,n):
    M = list()
    M.append(arr[0])
    M.append(max(arr[0], arr[1]))
    for i in xrange(2,n):
        M.append(max(M[i-1],max(M[i-2]+arr[i],arr[i])))
    return M[n-1]
if __name__ == '__main__':
    a = [-1, 3, -4, -2, -1, 6]
    # a = [int(i) for i in raw_input().split()]
    # print(maximum_contiguous_sum(a))
    print(maximum_contiguous_sum_non_adjacent_dp(a, 6))
