#include <iostream>
#include <initializer_list>
#include <algorithm>

struct LinkedList {
    struct Node {
        int data = 42;
        Node* next = nullptr;
    };

    LinkedList(std::initializer_list<int> list) {
        
        for(int elem : list) {
            push_front(elem);
        }   
    }

    void push_front(int data) {
        Node* new_node = new Node{data, head};
        head = new_node;
        ++length;
    }

    void remove_kth(int k) {
        Node* current = head;
        int pos = 0; 

        while(pos < k - 1) {
            if(current == nullptr) {
                return;
            }
            current = current->next;
            ++pos;
        }
        Node* to_delete = current->next;
        current->next = to_delete->next;
        
        delete to_delete;
        --length;

    }

    void clear() {
        Node* current = head;
        while(current) {
            Node* next = current->next;
            delete current;
            current = next;
        
        }
        head = nullptr;
        length = 0;
    }

    void remove_kth_last(int k) {
        remove_kth(length - k);
        
    } 

    ~LinkedList() {
        clear();
    }


    friend std::ostream& operator<<(std::ostream& os, const LinkedList& list) {
        Node* current = list.head;
        while(current) {
            os << current->data << ' ';
            current = current->next;
        }
        return os;
    }

private: 
    Node* head = nullptr;
    int length = 0;


};


int main() {
    LinkedList list{5, 4, 3, 2, 1};
    
    // list is 1 2 3 4 5

    std::cout << list << '\n';
    list.remove_kth(3);
    std::cout << list << '\n';
    list.remove_kth_last(2);
    std::cout << list << '\n';
    list.remove_kth_last(1);
    std::cout << list << '\n';
    list.remove_kth_last(1);
    std::cout << list << '\n';
    return 0;

}

/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

kth last -> n - k th element from the start 

*/