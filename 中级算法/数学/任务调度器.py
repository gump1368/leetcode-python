#！ -*- coding: utf-8 -*-
"""
@Author: Gump
@Create Time: 20230112
@Info:
"""

def leastInterval(tasks, n: int):
    if n == 0:
        return len(tasks)
    res = -1
    # 统计每个任务次数
    count = {}
    for task in tasks:
        if task in count:
            count[task] += 1
        else:
            count[task] = 1

    max_count = max(count.values())
    res += len([task for task, value in count.items() if value == max_count])
    res += (max_count-1) * (n+1) + 1
    return res if res > len(tasks) else len(tasks)


if __name__ == '__main__':
    print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))


