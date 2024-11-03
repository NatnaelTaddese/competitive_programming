n = int(input())
words = [input() for _ in range(n)]



def collabse(word1, word2):
    n = len(word1)
    m = len(word2)

    i = n - 1
    j = 0
    final_length = n + m

    while i >= 0 and j < m:
        if word1[i] == word2[j]:
            i -= 1
            j += 1
            final_length -= 2
        else:
            break
    
    return final_length
total = 0

for i in range(n):
    for j in range(n):
        total += collabse(words[i], words[j])



print(total)