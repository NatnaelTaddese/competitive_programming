
n = int(input())
boxes = list(map(int, input().split()))

# arrangement = dict()

# for box in boxes:
#     if  box not in arrangement.keys():
#         arrangement[box] = 0
#         continue
#     for bigger_box in arrangement.keys():
#         if box < bigger_box and arrangement[bigger_box] == 0:
#             arrangement[bigger_box] += 1
#             break

boxes = sorted(boxes, reverse=True)

# biggest = boxes[0]
# stack = 0
# x = 0
# second = biggest
# second_stack = 0

# for i, box in enumerate(boxes):
#     if box == biggest:
#         stack += 1
#     else:
#         second = box
#         x = i
#         break

# for box in boxes[x:]:
#     if box == second:
#         second_stack += 1
#     elif box < second:
#         second = box
#     elif box > second:
#         stack += 1

# print(stack)

biggest = boxes[0]
freq = 0
current_freq = 0

for box in boxes:
    if box < biggest:
        biggest = box
        current_freq = 1
    else:
        current_freq += 1
      
    if current_freq > freq:
        freq = current_freq

print(freq)