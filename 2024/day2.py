input_path = ''
res = 0
with open(input_path) as f:
    for line in f:
        data = line.split()
        increasing = []
        decreasing = []
        for n in data:
            n = int(n)
            if not increasing or (increasing[-1] < n and 1 <= n - increasing[-1] <= 3):
                increasing.append(n)
            if not decreasing or (decreasing[-1] > n and 1 <= decreasing[-1] - n <= 3):
                decreasing.append(n)
        if len(increasing) == len(data) or len(decreasing) == len(data):
            res += 1
print(res)