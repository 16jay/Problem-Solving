from collections import deque

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visit[r][c] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nr, nc = x + dr[k], y + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    q.append([nr, nc])


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
l = []

# 물의 높이가 0~100이 될 수 있다.
for h in range(0, 101):
    # 각 물 높이일 때 마다 기본 visit 만들어줌
    visit = [[0] * N for _ in range(N)]
    # 안전지역 개수 초기화
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 물의 높이 이하이면 방문체크
            if arr[i][j] <= h:
                visit[i][j] = 1

    for i in range(N):
        for j in range(N):
            # 물 높이 초과인곳들 bfs 탐색
            if visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    # 물의 높이가 0~100 각각 안전지역 개수 더해줌
    l.append(cnt)
print(max(l))