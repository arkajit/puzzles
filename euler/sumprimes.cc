#include <bitset>
#include <iostream>

using namespace std;

#define MAXNUM 2000000

int main() {
  // Bit is set if composite.
  bitset<MAXNUM> sieve;
  sieve.set(0);
  sieve.set(1);

  for (int i = 2; i < MAXNUM; i++) {
    if (!sieve.test(i)) {
      for (int j = 2*i; j < MAXNUM; j += i) {
        sieve.set(j);
      }
    }
  } 

  long sum = 0;
  for (int i = 0; i < MAXNUM; i++) {
    if (!sieve.test(i)) {
      sum += i;
    }
  }
  cout << "Sum is " << sum << endl;
}
