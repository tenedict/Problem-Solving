import sys

# 기계의 개수와 콘센트의 수
n, m = map(int, sys.stdin.readline().split())
# 기계들 충전시간
gige = list(map(int, sys.stdin.readline().split()))
gige.sort(reverse=True)

# 콘센트 구멍
consent = [0] * m

for j in gige:
    # 충전시간(값)이 작은 인덱스
    mm = consent.index(min(consent))
    # 충전시간이 젤 작은 애에 더하기
    consent[mm] = consent[mm] + j


# 젤로 큰값 출력
print(max(consent))
