n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

skippers = set()

tunnel_in = 0
tunnel_out = 0

while tunnel_out < n:
    if  a[tunnel_in] == b[tunnel_out]:
        tunnel_in += 1
        tunnel_out += 1
        continue
    else:
        if a[tunnel_in] in skippers:
            tunnel_in += 1
            continue

        if b[tunnel_out] not in skippers:
            skippers.add(b[tunnel_out])
            tunnel_out += 1
            continue
            
print(len(skippers))