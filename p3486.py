from collections import defaultdict
from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        ans = [0, 1]
        graph = defaultdict(list)
        for a,b,c in edges:
            graph[a].append((b, c))
            graph[b].append((a, c))

        costs = []
        last = defaultdict(lambda: -1)
        
        def dfs(node, curr_cost, prev, left):
            nonlocal ans
            node_color_index_prev = last.get(nums[node], -1)
            last[nums[node]] = len(costs)
            costs.append(curr_cost)
            
            ans2=[curr_cost - costs[left[0]], len(costs) - left[0]]
            ans=max(ans,ans2,key=lambda x:[x[0],-x[1]])
            
            for next_node, next_cost in graph[node]:
                if next_node == prev:
                    continue
                
                next_left = left
                if last[nums[next_node]] != -1:
                    next_left = left + [last[nums[next_node]] + 1]
                dfs(next_node, curr_cost + next_cost, node, sorted(next_left)[-2:])
            
            last[nums[node]] = node_color_index_prev
            costs.pop()
        
        dfs(0, 0, -1, [0,0])
        return ans
