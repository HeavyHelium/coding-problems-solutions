#include <iostream>
#include <vector>

struct graph { 

    graph(int node_cnt = 0): adj(node_cnt) { 
    } 

    // the graph is undirected, in this case it is a tree
    void add_edge(int u, int v) { 
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int max_removal() const { 
        int res = 0;
        std::vector<bool> visited(adj.size(), false);
        
        dfs(adj, 0, visited, res);
        
        return res;
    }

    void build_tree() { 
        std::vector<std::pair<int, int>> edges{ {0, 2}, {0, 1}, {0, 4}, 
                                                {2, 3}, {4, 5}, {5, 6}, 
                                                {5, 7} };
        int weight = edges.size() + 1; // in a tree, the number of vertices is the number of edges + 1
        adj.resize(weight);

        for(auto& e: edges) { 
            add_edge(e.first, e.second);
        }
    }    

private: 
    static int dfs(const std::vector<std::vector<int>>& g, 
                   int current, 
                   std::vector<bool>& visited, 
                   int& res) { 
    
        visited[current] = true;
        int tree_weight = 1;

        for(auto& next: g[current]) { 
            if (!visited[next]) { 
                int weight_child = dfs(g, next, visited, res);
                if(weight_child % 2 == 0) { 
                    ++res; // this child is being detached
                } else { 
                    tree_weight += weight_child;
                }
            }
        }
        return tree_weight;

    }


    std::vector<std::vector<int>> adj; 
};

int main() { 
    graph g;
    g.build_tree();
    std::cout << g.max_removal() << std::endl;

    return 0;
}