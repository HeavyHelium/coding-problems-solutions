#include <iostream>
#include <climits>
#include <vector>
#include <algorithm>
#include <unordered_set>

/// NlogN solution
std::pair<int, int> sumK(std::vector<int> v, int K) { 
    std::ranges::sort(v);
    int i = 0;
    int j = v.size() - 1;

    while(i < j) { 
        if(v[i] + v[j] == K) { 
            return { v[i], v[j] };
        } else if(v[i] + v[j] < K) { 
            i++;
        } else { 
            j--;
        }
    }
    return { INT_MIN, INT_MIN };
}


std::pair<int, int> sumKLinear(std::vector<int>& v, int K) { 
    std::unordered_set<int> set;

    for(int elem : v) { 
        if(set.find(K - elem) != set.end()) { 
            return { elem, K - elem };
        } else { 
            set.insert(elem);
        }
    }
    return { INT_MIN, INT_MIN };
}

int main() { 
    std::vector<int> v = { 1, 10, 7, 4, 5, 6, 18, 7, 8, 9, 2 };
    auto [i, j] = sumK(v, 10);
    std::cout << i << " " << j << std::endl;

    auto [i1, j1] = sumKLinear(v, 10);
    std::cout << i1 << " " << j1 << std::endl;



    return 0;
}