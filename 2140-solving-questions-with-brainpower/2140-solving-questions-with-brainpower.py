class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def backtrack(index):
            if index >= len(questions):
                return 0
            
            #pick
            pick_solved = questions[index][0]
            pick_solved += backtrack(index + questions[index][1] + 1)
            #unpick
            unpick_solved = backtrack(index + 1)

            return max(pick_solved, unpick_solved)



        return backtrack(0)