# def suff_pre(query):
#     index = -1
#     for i in range(n):
#         if query[0] == words[i][0]:
#             print(query[0], words[i][0])

#             if query[1] == words[i][-1]:
#                 print(query[1], words[i][-1])
#                 if index < i:
#                     index = i
    
#     return index




# n, q = map(int, input().split())

# words = list(map(str, input()))
# queries = []
# for  _ in range(q):
#     i, j = map(str, input().split())
#     queries.append([i,j])

# print(queries[0][1], words[0][-1])


# for query in queries:
#     print(suff_pre(query))


# n, q = map(int, input().split())

# words = [input() for _ in range(n)]
# queries = [input().split() for _ in range(q)]

# def suff_pre(query):
#     index = -1

#     for i in range(n):
#         if query[0] == words[i][0] and query[1] == words[i][-1]:
#             if index < i:
#                 index = i

#     return index

# for query in queries:
#     print(suff_pre(query))







# n, q = map(int, input().split())

# words = [input() for _ in range(n)]
# queries = [input().split() for _ in range(q)]

# def suff_pre(query):
#     index = -1
    
#     for i in range(n):
#         pre = True
#         post = True
#         for j in range(len(query[0])):
#             if query[0][j]  != words[i][j]:
#                 pre = False
#                 break
#         if pre:
#             for j in range(len(query[1])):
#                 if query[1][len(query[1]) - 1 - j]  != words[i][len(words[i]) - 1 - j]:
#                     post = False
#                     break

#         if pre and post:
#             if index < i:
#                 index = i

#     return index

# for query in queries:
#     print(suff_pre(query))




n, q = map(int, input().split())

words = [input() for _ in range(n)]
queries = [input().split() for _ in range(q)]

def suff_pre(query):
    index = -1
    
    for i in range(n):
        pre = True
        post = True
        
        # Check if the prefix of query[0] matches the prefix of words[i]
        for j in range(len(query[0])):
            if query[0][j] != words[i][j]:
                pre = False
                break
        
        # Check if the suffix of query[1] matches the suffix of words[i]
        for j in range(len(query[1])):
            if query[1][j] != words[i][-len(query[1]) + j]:
                post = False
                break
 
        if pre and post:
            if index < i:
                index = i  
 
    return index

for query in queries:
    print(suff_pre(query))