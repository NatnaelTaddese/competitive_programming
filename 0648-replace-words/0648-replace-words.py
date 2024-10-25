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
    def search(self, word: str) -> (bool, str):
        
        curr = self.root
        prefix = ""
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:  
                return False, word
            curr = curr.children[index]
            prefix += c
            if curr.is_end:
                return True, prefix
        return False, word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        result = []
        sentence = sentence.split(" ")

        for word in sentence:
            found, root = trie.search(word) 
            if found:
                result.append(root)
            else:
                result.append(word)
        

        return " ".join(result)


        