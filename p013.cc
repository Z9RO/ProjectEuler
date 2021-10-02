#include <vector>
#include <iostream>
#include <string>
#include "bigInt.h"
using namespace std;

int main(){
    vector<BigInt> nums;
    string s;
    while (cin >> s) {
        nums.emplace_back(BigInt(s));
        // cout << nums.back().toString() << endl;
    }

    for(int i=1; i<nums.size(); i++){
        nums[0].add(nums[i]);
        // cout << nums[0].toString() << endl;
    }

    cout << nums[0].toString() << endl;

}
