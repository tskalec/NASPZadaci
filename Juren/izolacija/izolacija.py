class Solution:
    def minVirusSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node, nodes_in_group, articulation_nodes, malware_nodes, depth, par):
            nonlocal graph, initial, n
            
            depth[node]=depth[par]+1 if par!=-1 else 0
            nodes_in_group.add(node)
            if node in initial:
                malware_nodes.add(node)
            
            for next_node in range(n):
                if next_node!=node and depth[next_node]==-1 and next_node!=par and graph[node][next_node]==1:
                    dfs(next_node, nodes_in_group, articulation_nodes, malware_nodes, depth, node)

            initial_depth=depth[node]
            for next_node in range(n):
                if next_node!=node and next_node!=par and graph[node][next_node]==1:
                    depth[node]=min(depth[node], depth[next_node])
            
            if initial_depth<=depth[node]:
                articulation_nodes.add(node)

        def dfs_art(node, visited):
            nonlocal n, graph, initial
            
            res=1
            visited[node]=True
            valid=False if node in initial else True
            
            for i in range(n):
                if graph[node][i] and not visited[i]:
                    res_tmp,val_tmp=dfs_art(i, visited)
                    res+=res_tmp
                    valid&=val_tmp
            
            return res, valid
            
        def process_art_node(node):
            nonlocal n, graph
            
            visited=[False]*n
            visited[node]=True
            res=0
            for i in range(n):
                if i!=node and graph[node][i]==1 and not visited[i]:
                    subgraph_size,valid=dfs_art(i, visited)
                    if valid:
                        res=max(res, subgraph_size)
        
            return res
        
        def process(node):
            nonlocal n, best_save, best_ind, processed
            nodes_in_group=set()
            articulation_nodes=set()
            malware_nodes=set()
            depth=[-1]*n
            dfs(node, nodes_in_group, articulation_nodes, malware_nodes, depth, -1)
        
            for node in nodes_in_group:
                processed[node]=True
        
            if len(malware_nodes)==1:
                remove_node=malware_nodes.pop()
                saved_nodes=len(nodes_in_group)-1
                if saved_nodes>best_save:
                    best_save=saved_nodes
                    best_ind=remove_node
                elif saved_nodes==best_save and remove_node<best_ind:
                    best_ind=remove_node
            elif len(malware_nodes)>1:
                for art_node in articulation_nodes:
                    saved_nodes=process_art_node(art_node)
                    if saved_nodes>best_save:
                        best_save=saved_nodes
                        best_ind=art_node
                    elif saved_nodes==best_save and art_node<best_ind:
                        best_ind=art_node
            
        
        
        initial=set(initial)
        n=len(graph[0])
        processed=[False]*n
        best_save,best_ind=-1,99999999
        for i in range(n):
            if not processed[i]:
                process(i)
                
        return best_ind
