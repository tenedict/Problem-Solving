import heapq

n,m = map(int, input().split())
gige = list(map(int, input().split()))
gige.sort(reverse=True)
consent = []

for i in gige:
    if len(consent) < m:
        heapq.heappush(consent, i)
    else:
        chung = heapq.heappop(consent)
        heapq.heappush(consent, chung + i)

print(max(consent))