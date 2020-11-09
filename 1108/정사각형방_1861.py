def dfs(r, c):
    global cnt
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
        elif arr[nr][nc] == arr[r][c] + 1:
            cnt += 1
            dfs(nr, nc)
    return cnt


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]
    # ans: 최대 갈 수 있는 방의 수,   x,y: ans가 나오는 좌표
    ans = x = y = 0
    for i in range(N):
        for j in range(N):
            # 기본적으로 1개의 방을 갖고 dfs 탐색
            cnt = 1
            dfs(i, j)
            # 갈 수 있는 방의 수가 큰 곳을 발견하면 ans, x, y값 바꿈
            if ans < cnt:
                ans = cnt
                x, y = i, j
            # 갈 수 있는 방의 수는 동일하지만, 적힌 수가 작다면 x, y값 바꿈
            elif ans <= cnt and arr[i][j] < arr[x][y]:
                x, y = i, j

    print('#{} {} {}'.format(tc, arr[x][y], ans))