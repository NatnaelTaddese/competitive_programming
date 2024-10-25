class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True

    def recursive_search(self, word: str, node: TrieNode, index: int) -> bool:
        if index == len(word):
            return node.is_end
        
        c = word[index]
        if c == '.':
            for child in node.children:
                if child and self.recursive_search(word, child, index + 1):
                    return True
            return False
        else:
            child_index = ord(c) - ord('a')
            curr = node.children[child_index]
            if not curr:
                return False
            return self.recursive_search(word, curr, index + 1)

        

    def search(self, word: str) -> bool:
        return self.recursive_search(word, self.root, 0)

        # for i, c in enumerate(word):
        #     if c = ".":
                

        #     index = ord(c) - ord('a')
        #     if not curr.children[index]:
        #         return False
        #     curr = curr.children[index]
        # return curr.is_end


class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        self.trie.insert(word)
        

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)