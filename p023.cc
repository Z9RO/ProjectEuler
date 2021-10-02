#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

bool isAbundant(int num){
    int divSum = 1;
    int sqrtNum = ceil(sqrt(num));
    int sqrts = sqrtNum*sqrtNum;
    if(sqrts==num){
        divSum += sqrtNum;
    }
    for(int i=2; i<sqrtNum; i++){
        if(num%i==0){
            divSum += i;
            divSum += num/i;
        }
    }
    return divSum>num;
}

int main(){
    // 28123 
    const int all = 28124;
    vector<bool> nums(all, true);

    vector<int> abundants;

    for(int i=12; i<all; i++){
        if(isAbundant(i)){
            abundants.push_back(i);
            for(auto one:abundants){
                if(one+i<all){
                    nums[one+i] = false;
                }else{
                    break;
                }
            }
        }
    }

    int sum = 0;
    for(int i=1; i<all; i++){
        sum += nums[i] ? i:0;
    }
    cout << sum << endl;
}