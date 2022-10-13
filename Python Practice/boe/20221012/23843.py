import heapq

n, m = map(int, input().split())
gige = list(map(int, input().split()))
su = 5 // 2

print(gige)
print(su)

h = heapq.heappop(gige)
print(h)
