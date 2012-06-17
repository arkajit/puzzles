/*
ID: arkajit.d1
PROG: tilechng
LANG: C++
*/

#include <fstream>
#include <iostream>
#include <math>
#include <vector>

using namespace std;

typedef vector<int>::iterator vit;

bool IsPerfectSquare(int n) {
  double m = sqrt(static_cast<double>(n));
  return floor(m) == m;
}

int MinCost(vit start, vit end, int target) {
  if (end - start > 1) {
    int first = *start;
  } else if (end - start == 1 && IsPerfectSquare(target)) {
    int diff = *start - static_cast<int>(sqrt(target));
    return diff*diff;
  } else {
    return -1;
  }
}

int main() {
  ofstream fout("tilechng.out");
  ifstream fin("tilechng.in");

  int N, M;
  fin >> N >> M;
  cout << N << " " << M << endl;
  vector<int> sides(N);

  for (int i = 0; i < N; ++i) {
    fin >> sides[i];
    cout << sides[i] << endl;
  }

  
}
