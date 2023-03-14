#include <iostream>
#include <cassert>
#include <unordered_map>
#include <string>
#include <queue>
#include <cstddef>
#include <stdexcept>

struct Node {
    // the inner nodes have data '$'(just a fixed value)
    char data = '$'; 
    std::size_t value = 0;
    Node* left = nullptr;
    Node* right = nullptr;

    bool operator>(const Node& other) const {
        // this is used make the heap a min heap
        return value > other.value;
    }
};

class comparator {
public:
    bool operator()(const Node* lhs, const Node* rhs) {
        return *lhs > *rhs;
    }
};

using FreqMap = std::unordered_map<char, std::size_t>;



struct huffman_tree { 

    using Coder = std::unordered_map<char, 
                                     std::string>;
    
    using MinQueue = std::priority_queue<Node*, 
                                         std::vector<Node*>, 
                                         comparator>;

    huffman_tree() = default;

    huffman_tree(const huffman_tree& other) = delete;
    huffman_tree& operator=(const huffman_tree& other) = delete;

    huffman_tree(const FreqMap& freqs) {
        freq = freqs;
        build();
    }

    huffman_tree(const std::string& text) {
        freq = text_to_freq(text);
        build();
    }

    std::string encode(const std::string& text) const {
        std::string res;
        for(char ch: text) {
            auto it = code_table.find(ch);
            if(it == code_table.end()) {
                throw std::runtime_error("Invalid code!");
            } else {
                res += it->second;
            }
        }
        return res;
    }

    std::string decode(const std::string& text) {
        const char* suffix = text.c_str();
        std::string res;

        decode_helper(root, suffix, res);
        return res;
    }

    friend std::ostream& operator<<(std::ostream& os,
                                    const huffman_tree& T) {
        for(const std::pair<char, 
                            std::string>& elem: T.code_table) {
        
            os << elem.first << ": " << elem.second << '\n';
        }
        return os;
    }


    ~huffman_tree() { 
        free_tree(root);    
    }


private:

    void decode_helper(const Node* root,
                       const char*& suffix,
                       std::string& res) {
        
        if(root->data != '$') {
        
            res += root->data;
            if(*suffix) {
                decode_helper(this->root, 
                              suffix, 
                              res);
            }
            return;
        }
        if(!*suffix) {
            return;
        }

        if(*suffix == '0') {
            decode_helper(root->left,
                          ++suffix,
                          res);
        } else {
            decode_helper(root->right,
                          ++suffix,
                          res);
        }

    }

    void fill_code(const Node* root, std::string& code) {
        if(!root) {
            return;
        }
        if(root->data != '$') {
            // a leaf reached
            code_table[root->data] = code;
        } else {
            code.push_back('0'); // left edges are labeled with 0
            fill_code(root->left, code);
            code.pop_back();

            code.push_back('1'); // right edges are labeled with 1
            fill_code(root->right, code);
            code.pop_back();
        }
    }

    static FreqMap text_to_freq(const std::string& text) { 
        FreqMap freq;
        for(char c : text) {
            if(freq.find(c) == freq.end()) {
                freq[c] = 0;
            } 
            freq[c]++;
        }
        return freq;
    }

    MinQueue build_queue() const { 
        MinQueue q;
        
        for(const std::pair<char, std::size_t>& p : freq) { 
            q.push(new Node{p.first,
                              p.second,
                               nullptr,
                                    nullptr });
        }
        
        return q;
    }

    void build() {
        assert(root == nullptr);

        std::size_t n = freq.size();
        if(n == 0) {
            return;
        }

        if(n < 2) { 
            code_table[freq.begin()->first] = freq.begin()->second;
        }

        MinQueue q = build_queue();

        while(q.size() > 1) { 
            Node* left = q.top();
            q.pop();
            Node* right = q.top();
            q.pop();
            
            q.push(new Node{ '$',
                              left->value + right->value,
                              left,
                              right });
        }

        root = q.top();
        std::string temp;
        fill_code(root, temp);
    }

    static void free_tree(Node*& root) { 
        if(root == nullptr) return;
        
        free_tree(root->left);
        free_tree(root->right);

        delete root;
        root = nullptr;
    } 

    Node* root = nullptr;
    FreqMap freq;
    Coder code_table;
};


int main() { 
    huffman_tree tr("mssssiiiipp");
    std::cout << tr << std::endl;

    FreqMap f{{'a', 5}, {'b', 9}, {'c', 12},
              {'d', 13}, {'e', 16}, {'f', 45}};

    huffman_tree t2(f);

    std::cout << t2.decode(t2.encode("cdef")) << std::endl;

    std::cout << "Inval: " << t2.decode("111") << std::endl;


    std::cout << t2 << std::endl;

    return 0;
} 