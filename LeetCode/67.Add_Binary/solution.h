class Solution {
public:
    string addBinary(string a, string b) {
        unsigned long long int a_dec = binary2decimal(a);
        unsigned long long int b_dec = binary2decimal(b);
        unsigned long long int c_dec = a_dec + b_dec;
        string c_bin = decimal2binary(c_dec);
        if (c_bin=="") { return "0"; }
        return c_bin;
    }
    
    unsigned long long int binary2decimal(string a){
        vector<char> res;
        for (auto el:a){
            res.push_back(el);
        }
        int i = 0;
        unsigned long long int result = 0;
        for (auto it=res.rbegin() ; it!=res.rend(); it++){
            if ((*it)=='1') { result += pow(2,i); }
            i += 1;
        }
        return result;
    }
    
    string decimal2binary(unsigned long long int a){
        vector<unsigned long long int> res;
        while(a>=1){
            res.push_back(a%2);
            a = (int)a/2;
        }
        string result = "";
        for (auto it=res.rbegin(); it!=res.rend(); it++){
            result += to_string(*it);
        }
        return result;
    }
};