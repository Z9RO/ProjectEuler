#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int getRecurringCycle(int n) {
  int level = 0;
  unordered_map<int, int> mp;
  int base = 1;
  while (base > 0) {
    while (base < n) {
      base *= 10;
      level++;
    }
    auto fd = mp.find(base);
    if (fd != mp.end()) {
      return level - fd->second;
    }
    mp[base] = level;
    level++;
    base = base % n;
  }
  return 0;
}

int main() {
  int maxRC = 0;
  int maxRCN = 0;
  for (int i = 1; i < 1000; i++) {
    int rc = getRecurringCycle(i);
    cout << i << ' ' << rc << endl;
    if (rc > maxRC) {
      maxRC = rc;
      maxRCN = i;
    }
  }
  cout << maxRCN << endl;
}