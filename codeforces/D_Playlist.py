from heapq import heappop, heappush


n, k = map(int, input().split())
songs = []

for _ in range(n):
    songs.append(tuple(map(int, input().split())))

songs = sorted(songs, key=lambda x: x[1], reverse=True)

total_duration = 0
min_beauty = songs[0][1]
curr_value = 0

heap = []

# for song in songs:
#     if k == 0:
#         break
#     new_value = (total_duration + song[0]) * min(song[1], min_beauty)
#     if new_value > curr_value:
#         total_duration += song[0]
#         min_beauty = min(song[1],min_beauty)
#         curr_value = new_value
#         k -= 1

for length, beauty in songs:
    heappush(heap,length)
    total_duration += length

    if len(heap) > k:
        total_duration -= heappop(heap)

    curr_value = max(curr_value, (total_duration * beauty))

print(curr_value)
