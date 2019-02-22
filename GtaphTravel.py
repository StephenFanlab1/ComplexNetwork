# 图的宽度遍历和深度遍历

# 1. BFS
def bfsTravel(graph, source):
    # 传入的参数为邻接表存储的图和一个开始遍历的源节点
    frontiers = [source]     # 表示前驱节点
    travel = [source]       # 表示遍历过的节点
    # 当前驱节点为空时停止遍历
    while frontiers:
        nexts = []          # 当前层的节点（相比frontier是下一层）
        for frontier in frontiers:
            for current in graph[frontier]: # 遍历当前层的节点
                if current not in travel:   # 判断是否访问过
                    travel.append(current)  # 没有访问过则入队
                    nexts.append(current)   # 当前结点作为前驱节点
        frontiers = nexts   # 更改前驱节点列表
    return travel
#2. DFS
def dfsTravel(graph, source):
    # 传入的参数为邻接表存储的图和一个开始遍历的源节点
    travel = []     # 存放访问过的节点的列表
    stack = [source]      # 构造一个堆栈
    while stack:            # 堆栈空时结束
        current = stack.pop()       # 堆顶出队
        if current not in travel:   # 判断当前结点是否被访问过
            travel.append(current)  # 如果没有访问过，则将其加入访问列表
        for next_adj in graph[current]: # 遍历当前结点的下一级
            if next_adj not in travel:  # 没有访问过的全部入栈
                stack.append(next_adj)
    return travel
#3. 广度优先遍历找图中起始点间所有路径，递归实现
def find_all_paths(graph, start, end, path=[]):
    """
    广度优先遍历找图中起始点间所有路径，递归实现
    :param graph:图拓扑 以邻接表形式表示
    :param start: 起点 'start'
    :param end: 终点 'end'
    :param path: 已经历点
    :return: 所有路径的列表
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths






if __name__ == "__main__":
    graph = {}
    graph['a'] = ['b']
    graph['b'] = ['c','d']
    graph['c'] = ['e']
    graph['d'] = []
    graph['e'] = ['a']

    # test of BFS
    print(bfsTravel(graph, 'b'))

    print(dfsTravel(graph, 'b'))