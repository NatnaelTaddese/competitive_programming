class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }

        string digit = std::to_string(x);
        int left = 0;
        int right = digit.length() - 1;
        while(left < right){
            if(digit[left] != digit[right]){
                return false;
            }

            left++;
            right--;
        }
        return true;
        
    }
};