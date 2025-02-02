import heapq

left_col, right_col = [], []
input_path = ''
with open(input_path) as data:
    for line in data:
        nums = line.split()
        heapq.heappush(left_col, int(nums[0]))
        heapq.heappush(right_col, int(nums[1]))

res = 0
while left_col:
    l = heapq.heappop(left_col)
    r = heapq.heappop(right_col)
    res += abs(l - r)
print(res)