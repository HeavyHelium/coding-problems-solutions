def wrapper(func): 
        def inner(self, sentence1, sentence2): 
            left = sentence1.split()
            right = sentence2.split()
            if len(left) != len(right): 
                raise ValueError("Sentences must be of equal length")
            return func(self, sentence1, sentence2)
                
        return inner


class graph: 
    def __init__(self) -> None: 
        # each word is a node and its neighbours are stored in a set
        self._adj: dict[str, set[str]] = {}
    
    def add_pair(self, word1, word2) -> None:
        lst = [word1, word2]

        for i, word in enumerate(lst):
            if word not in self._adj:
                self._adj[word] = set()
            
            self._adj[word].add(lst[1 - i])

    
    @wrapper
    def are_equivalent(self, 
                       sentence1: str, 
                       sentence2: str) -> bool:
        
        left = sentence1.split()
        right = sentence2.split()

        for word1, word2 in zip(left, right):
            if word1 == word2: 
                continue

            if word1 not in self._adj or\
               word2 not in self._adj[word1]:

                return False

        return True

    def path(self, u: str, v: str) -> bool: 
        visited = set()
        stack = [u]
        # dfs with a stack, because why not
        while stack: 
            node = stack.pop()
            if node == v: 
                return True

            if node not in visited: 
                visited.add(node)
                for neighbour in self._adj[node]: 
                    if not neighbour in visited: # not necessary, but it won't fill up the stack too much 
                        stack.append(neighbour)
        
        return False

    @wrapper
    def are_equivalent1(self, 
                        sentence1: str, 
                        sentence2: str) -> bool:

        left = sentence1.split()
        right = sentence2.split()

        for word1, word2 in zip(left, right):
            if word1 == word2: 
                continue

            if not self.path(word1, word2): 
                return False
        
        return True

if __name__ == "__main__": 
    g = graph()
    g.add_pair("big", "large")
    g.add_pair("eat", "consume")
    g.add_pair("consume", "devour")

    sentence1 = "He wants to eat food"
    sentence2 = "He wants to consume food"
    sentence3 = "He wants to devour food"

    assert(g.are_equivalent(sentence1, sentence2))
    assert(g.are_equivalent1(sentence1, sentence3))