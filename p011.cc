#include<iostream>
#include<vector>
using namespace std;
const int row = 20;
const int col = 20;

int rowMax(vector<vector<int>>& nums, int maxOne){
    for(int i=0; i<row; i++){
        for(int j=0; j<col-3; j++){
            int one = nums[i][j]*nums[i][j+1]*nums[i][j+2]*nums[i][j+3];
            maxOne = max(maxOne, one);
        }
    }
    return maxOne;
}

int colMax(vector<vector<int>>& nums, int maxOne){
    for(int j=0; j<col; j++){
        for(int i=0; i<row-3; i++){
            int one = nums[i][j]*nums[i+1][j]*nums[i+1][j]*nums[i+3][j];
            maxOne = max(maxOne, one);
        }
    }
    return maxOne;
}

int diag1Max(vector<vector<int>>& nums, int maxOne){
    for(int i=0; i<row-3; i++){
        for(int j=0; j<col-3; j++){
            int one = nums[i][j]*nums[i+1][j+1]*nums[i+2][j+2]*nums[i+3][j+3];
            maxOne = max(maxOne, one);
        }
    }
    return maxOne;
}

int diag2Max(vector<vector<int>>& nums, int maxOne){
    for(int i=0; i<row-3; i++){
        for(int j=3; j<col; j++){
            int one = nums[i][j]*nums[i+1][j-1]*nums[i+2][j-2]*nums[i+3][j-3];
            maxOne = max(maxOne, one);
        }
    }
    return maxOne;
}

int main(){
    vector<vector<int>> nums(row, vector<int>(col));
    for(auto& vt:nums){
        for(auto& num:vt){
            cin >> num;
        }
    }

    int maxOne = 0;
    maxOne = rowMax(nums, maxOne);
    maxOne = colMax(nums, maxOne);
    maxOne = diag1Max(nums, maxOne);
    maxOne = diag2Max(nums, maxOne);

    cout << maxOne << endl;
}