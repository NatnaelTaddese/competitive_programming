import sys
input = sys.stdin.readline

def merge(left, right, count):
    if sum(left) > sum(right):
        count += 1
        return right + left, count
    return left + right, count

def mergeSort(nums, n, count):
    if n == 1:
        return nums, count
    
    mid = n // 2
    left, count = mergeSort(nums[:mid], mid, count)
    right, count = mergeSort(nums[mid:], n - mid, count)

    merged, count = merge(left, right, count)
    return merged, count

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    temp = nums[:]
    count = 0

    nums, count = mergeSort(nums, n, count)
    
    if nums == sorted(temp):
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    for _ in range(int(input())):
        solve()
