#include <iostream>
typedef long long ll;
using namespace std;

int main() {
  ll sum = 1;

  for (ll i = 3; i <= 1001; i += 2) {
    ll base = i * i;
    sum += base * 4;
    sum -= (i - 1) * 6;
  }

  cout << sum << endl;
}