#include <limits.h>
#include <stdint.h>
// #include <vcruntime.h>
#include <algorithm>
#include <vector>
#include <string>

class BigInt{
    const uint64_t maxOneVal = 1000000000000000000;
    const uint64_t halfMaxOneVal = 500000000000000000;
    std::vector<uint64_t> values;
    bool positive = true;
public:
    BigInt(const std::string& s){
        if(s.size()>1){
            size_t pos = 0;
            if(s[pos]=='-'){
                pos++;
                positive = false;
            }

            size_t end = s.size();
            for(size_t i=pos; i<s.size(); i++){
                if(s[pos]>'9' || s[pos]<'0'){
                    end = i;
                    break;
                }
            }

            while(end>=pos+18){
                end -= 18;
                uint64_t base = 0;
                for(size_t i=0; i<18; i++){
                    base = base*10+(s[end+i]-'0');
                }
                values.push_back(base);
            }

            if(end!=pos){
                uint64_t base = 0;
                while(end!=pos){
                    base = base*10+(s[pos]-'0');
                    pos++;
                }
                values.push_back(base);
            }
        }
    }
    std::string toString(){
        std::string s;

        for(uint64_t value:values){
            std::string tmp;
            for(int i=0; i<18; i++){
                tmp.push_back(value%10+'0');
                value = value/10;
            }
            s += tmp;
        }

        if(!positive){
            s += '-';
        }
        std::reverse(s.begin(), s.end());

        return s;
    }
    BigInt& add(const BigInt& b){
        if(positive==b.positive){
            if(values.size()>0 && b.values.size()>0){
                while(values.size()<b.values.size()){
                    values.push_back(0);
                }

                size_t i = 0;
                bool next = false;
                while(i<b.values.size()){
                    values[i] += next ? 1:0;
                    if(maxOneVal-b.values[i] <= values[i]){
                        next = true;
                        uint64_t tmp = b.values[i];
                        if(values[i]>=halfMaxOneVal){
                            values[i] -= halfMaxOneVal;
                        }else{
                            tmp -= halfMaxOneVal;
                        }
                        values[i] += tmp;
                        values[i] -= halfMaxOneVal;
                    }else{
                        next = false;
                        values[i] += b.values[i];
                    }
                    i++;
                }

                while(next && i<values.size()){
                    values[i]++;
                    if(values[i]==maxOneVal){
                        next = true;
                        values[i] = 0;
                    }else{
                        next = false;
                    }
                    i++;
                }
                if(next){
                    values.push_back(1);
                }
            }
        }else{
            // to do
        }
        return *this;
    }
    // BigInt sub(BigInt& b){

    // }
};