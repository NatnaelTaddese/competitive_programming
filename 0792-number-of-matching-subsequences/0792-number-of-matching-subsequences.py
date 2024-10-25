class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
        res = 0
        for word in words:
            valid = True
            last_idx = -1
            for c in word:
                if c not in indices:
                    valid = False
                    break
                idx = bisect_right(indices[c], last_idx)
                boundary = len(indices[c])
                if idx == boundary:
                    valid = False
                    break
                last_idx = indices[c][idx]
            if not valid:
                continue
            res += 1

        return res