class Solution {
public:
    int count_word(string &s, int index){
        int count = 0;
        for(int i = index; i >= 0; i--){
            if(s[i] == ' '){
                break;
            }
            else{
                count++;
            }
        }
        return count;
    }

    int lengthOfLastWord(string s) {
        int length = s.length();
        int last_word_length;
        for(int i = length - 1; i >= 0; i--){
            if(s[i]!=' '){
                last_word_length = count_word(s,i);
                break;
            }
        }
        return last_word_length;
    }
};