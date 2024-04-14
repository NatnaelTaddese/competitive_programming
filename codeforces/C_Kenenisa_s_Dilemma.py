n = int(input())
a = list(map(int, input().split()))

k = 0
swapped = False
result = []

for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
                swapped = True
        if swapped:
             a[i], a[min_idx] = a[min_idx], a[i]
             result.append([i,min_idx])
             swapped = False
             k += 1
if k > n:
     print(0)
else:
     print(k)
     for i in result:
          print(i[0],i[1])
