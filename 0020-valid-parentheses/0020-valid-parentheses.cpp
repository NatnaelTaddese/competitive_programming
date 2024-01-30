class Solution {
public:
    bool isValid(string s) {

        vector<char> answer;

        int length = s.length();


        for(int i = 0; i < length; i++){
            switch(s[i]){
                case '(':
                    answer.push_back(s[i]);
                    break;
                case ')':
                    if(answer.size() == 0){
                        return false;
                    }
                    if(answer.back() == '('){
                        answer.pop_back();
                    }
                    else{
                        return false;
                    }
                    break;
                case '{':
                    answer.push_back(s[i]);
                    break;
                case '}':
                    if(answer.size() == 0){
                        return false;
                    }
                    if(answer.back() == '{'){
                        answer.pop_back();
                    }
                    else{
                        return false;
                    }
                    break;
                case '[':
                    answer.push_back(s[i]);
                    break;
                case ']':
                    if(answer.size() == 0){
                        return false;
                    }
                    if(answer.back() == '['){
                        answer.pop_back();
                    }
                    else{
                        return false;
                    }
                    break;
                default:
                    break;
            }
        }
        if(answer.size() == 0){
            return true;
        }
        return false;
        
    }
};