n, m = map(int, input().split())

servers = dict()
for _ in range(n):
    name, ip = map(str, input().split())
    servers[ip] = name

for _ in range(m):
    command, ip = map(str, input().split())
    print(command + " " +  ip + " #" + servers [ip[:-1]])

