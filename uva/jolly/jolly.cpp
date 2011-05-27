#include <iostream>
#include <cmath>
#include <set>

#define MAXNUM 3000

using namespace std;

int main() {
  int d, n; 
  int nums[MAXNUM];
  set<int> rem;   /* differences that remain to be seen */
  set<int>::iterator it;

  while (cin >> n) {
    for (int i = 0; i < n; i++) {
      cin >> nums[i]; 
    }

    rem.clear();
    for (int i = 1; i < n; i++) {
      rem.insert(i);
    }

    for (int i = 0; i < n-1; i++) {
      d = fabs(nums[i+1] - nums[i]);
      it = rem.find(d); 
      if (it == rem.end()) {
        break;  /* trying to use a difference twice */
      } else {
        rem.erase(it);
      } 
    }

    if (rem.empty()){
      cout << "Jolly" << endl;
    } else {
      cout << "Not jolly" << endl;
    } 
  } 
}
