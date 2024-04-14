#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        set_one = set(a)
        set_two = set(b)
        
        set_three = set_one.union(set_two)
        return len(set_three)
