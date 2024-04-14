class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        string word = "";
        bool divisible = false;
        
        for(int i = 1; i <= n; i++){
            if(i % 3 == 0){
                divisible = true;
                word += "Fizz";
            }
            if(i % 5 == 0){
                divisible = true;
                word += "Buzz";
            }

            if(divisible){
                answer.push_back(word);
                word = "";
                divisible = false;
            }
            else{
                answer.push_back(std::to_string(i));
            }
        }
        return answer;
        
    }
};