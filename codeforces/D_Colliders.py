import math


n, m = map(int, input().split())

# colliders = set()
colliders = [False for _ in range(n + 1)]
active_colliders = set()


for _ in range(m):
    operation, collider = input().split()
    collider = int(collider)

    if operation == '+':
        if colliders[collider]:
            print('Already on')
            continue

        # for i in range(1, collider + 1):
        # for i in range(n,1, -1):
        #     # print("Checking ", i, collider)
        #     if not math.gcd(i, collider) == 1 and colliders[i]:
        #         print('Conflict with', i)
        #         break
        for active in active_colliders:
            if not math.gcd(active, collider) == 1:
                print('Conflict with', active)
                break
        else:
            colliders[collider] = True
            active_colliders.add(collider)
            print('Success')
    else:
        if not colliders[collider]:
            print('Already off')
            continue

        else:
            colliders[collider] = False
            active_colliders.remove(collider)
            print('Success')

    