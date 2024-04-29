
def linkedListToArray(node):
    arr = []
    curr = node

    while curr is not None:
        arr.append(curr.data)
        curr = curr.next

    return arr
