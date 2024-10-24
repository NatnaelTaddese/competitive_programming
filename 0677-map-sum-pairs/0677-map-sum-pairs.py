class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = [ None for _ in range(26) ]

class MapSum:

    def __init__(self):
        self.seen = dict()
        self.root = TrieNode(0)

    def insert(self, word: str, val: int) -> None:

        temp = val
        if word in self.seen:
            val -= self.seen[word]

        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode(0)
            curr = curr.children[index]
            curr.val += val
        
        self.seen[word] = temp
        
    def search(self, word: str) -> bool:
        # your code goes here
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def sum(self, prefix: str) -> int:
        curr = self.root
        total = 0
        if not self.search(prefix):
            return 0
        
        for c in prefix:
            index = ord(c) - ord('a')
            curr = curr.children[index]

        return curr.val

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)