#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

vector<int> inputHelp(string &s) {
  vector<int> res;
  size_t pos = 1;
  while (pos < s.size()) {
    int one = 0;
    while (s[pos] != '"') {
      one += (s[pos] - 'A' + 1);
      pos++;
    }
    res.push_back(one);
    pos += 3;
  }
  return res;
}

class TriangleSet {
  int maxN;
  int maxTri;
  unordered_set<int> st;
  void update() {
    maxN++;
    maxTri += maxN;
    st.insert(maxTri);
  }

public:
  TriangleSet() : maxN(1), maxTri(1), st({1}) {}
  bool find(int num) {
    while (num > maxTri) {
      update();
    }
    auto fd = st.find(num);
    return fd != st.end();
  }
};

int main() {
  string s;
  cin >> s;
  auto input = inputHelp(s);
  cout << input.size() << endl;
  int res = 0;
  TriangleSet ts;
  for (auto d : input) {
    if (ts.find(d)) {
      res++;
    }
  }
  cout << res << endl;
}