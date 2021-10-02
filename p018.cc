#include <vector>
#include <iostream>
using namespace std;
int main(){
    vector<vector<int>> vts(1);
    int num;
    int size = 1;
    while (cin>>num) {
        if(vts.back().size()==size){
            vector<int> vt;
            vts.push_back(vt);
            size++;
        }
        vts.back().push_back(num);
    }

    int end = vts.size()-1;
    if(vts[end].size()>vts[end-1].size()){
        for(int i=end-1; i>=0; i--){
            for(int j=0; j<vts[i].size(); j++){
                vts[i][j] += max(vts[i+1][j], vts[i+1][j+1]);
            }
        }
    }
    cout << vts[0][0] << endl;
}