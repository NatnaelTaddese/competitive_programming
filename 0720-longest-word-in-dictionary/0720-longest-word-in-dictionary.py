class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # your code goes here
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_end = True
    def search(self, word: str) -> bool:
        # your code goes here
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        result = ""


        for word in words:
            if (len(word) < len(result)) or (len(word) == len(result) and word > result):
                continue
            
            valid = True
            for i in range(1,len(word)):
                if not trie.search(word[:i]):
                    valid = False
                    break
            if valid:
                result = word
        
        return result

            



        