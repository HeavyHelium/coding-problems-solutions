#include <iostream>
#include <vector>
#include <functional>
#include <utility>
#include <cassert>

/// Implementing filter, map and reduce

namespace my {
    // for_each is supposed to modify the vector
    template<typename T>
    void for_each(std::vector<T>& items,
                  std::function<void(T&)> func) {
        for(T& item : items) {
            func(item);
        }
    }

    // map is not supposed to modify the input vector, but return a new, modified vector
    template<typename T, typename ResType>
    std::vector<ResType> map(const std::vector<T>& items,
                             std::function<ResType(const T&)> mapper) {

        std::vector<ResType> res_vec(items.size());

        for(std::size_t i = 0; i < items.size(); ++i) {
            res_vec[i] = mapper(items[i]);
        }

        return std::move(res_vec);
    }

    // filter is supposed to not modify the vector,
    // but return a new filtered vector of the same type
    template<typename T>
    std::vector<T> filter(const std::vector<T>& items,
                          std::function<bool(const T&)> predicate) {

        std::vector<T> res;

        for(const T& item : items) {
            if(predicate(item)) {
                res.push_back(item);
            }
        }
        return res;
    }

    template<typename T, typename ResType>
    ResType reduce(const std::vector<T>& items,
                   std::function<ResType(const T& left,
                                         const T& right)> func,
                   ResType initial_value) {

        for(const T& item : items) {
            initial_value = func(initial_value, item);
        }
        return initial_value; // it is rather the final value now
    }

};

template <typename T>
std::ostream& operator<<(std::ostream& os,
                         const std::vector<T>& v) {
    for(const T& elem : v) {
        os << elem << " ";
    }
    return os << '\n';
}

template <typename T>
bool operator==(const std::vector<T>& left,
                const std::vector<T>& right) {

    if(left.size() != right.size()) {
        return false;
    }
    for(std::size_t i = 0; i < left.size(); ++i) {
        if(left[i] != right[i]) {
            return false;
        }
    }

    return true;
}


int main() {

    std::vector<int> elems{ 5, 1, -5, 6, -42, 15, 42 };

    std::vector<int> filtered(my::filter<int>(elems,
                                              [](const int& elem) {
                                                    return elem > 0;
                                              }));
    std::vector<int> res_f{ 5, 1, 6, 15, 42 };
    assert(filtered == res_f);

    std::vector<int> mapped(my::map<int, int>(elems,
                                              [](const int& elem) {
                                                    return elem  * 2;
                                              }));

    std::vector<int> res_m{ 10, 2, -10, 12, -84, 30, 84 };
    assert(mapped == res_m);

    int reduced = 22;
    assert((my::reduce<int, int>(elems,
                                 [](const int& left, const int& right) {
                                        return left + right;
                                 }, 0))
                                 == reduced);

    my::for_each<int>(elems, [](int& elem) { elem *= 2; });
    assert(elems == mapped);


    return 0;
}
