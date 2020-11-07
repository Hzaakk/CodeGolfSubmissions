print(*[int("".join(i),2)for i in zip(*(f'{int(j):08b}'for j in input().split()))])
