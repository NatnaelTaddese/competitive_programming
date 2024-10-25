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

    def search_from(self, s: str, start: int) -> List[int]:
        curr = self.root
        ends = []
        for i in range(start, len(s)):
            index = ord(s[i]) - ord('a')
            if not curr.children[index]:
                break
            curr = curr.children[index]
            if curr.is_end:
                ends.append(i + 1)
        return ends
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(n):
            if dp[i]:
                ends = trie.search_from(s,i)
                for end in ends:
                    dp[end] = True
        
        return dp[n]
        