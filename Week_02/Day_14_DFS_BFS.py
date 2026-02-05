from collections import deque

# DFS 템플릿(재귀함수)
# visited: 방문 처리 배열
def dfs(node, visited, graph):
    visited[node] = True
    print(node, end=' ') # 방문 도장 쾅!

    # 인접한 노드들을 방문
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited, graph)


# BFS 템플릿(큐)
def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True # 시작점 방문 처리

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐에서 하나 꺼냄
        print(v, end=' ')

        # 인접한 노드들을 큐에 넣음
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True