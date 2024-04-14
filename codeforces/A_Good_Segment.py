n = int(input())
s = input()

max_len = 1
left = 0

while left < n:
    right = left + 1
    while right < n and ord(s[right]) == ord(s[right - 1]) + 1:  
        right += 1
    max_len = max(max_len, right - left)
    # print(right - left)
    left = right

print(max_len)