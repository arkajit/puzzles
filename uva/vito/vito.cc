#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

// The median of a sorted list of numbers.
int median(const vector<int>& nums) {
  int mid = nums.size() / 2;
  if (nums.size() % 2 == 0) {
    return (nums[mid] + nums[mid+1]) / 2;
  } else {
    return nums[mid];
  }
}

// Manhattan distance from p to all other nums.
int cost(const vector<int>& nums, int p) {
  int num, c = 0;
  for (int i = 0; i < nums.size(); ++i) {
    num = nums[i];
    c += (num < p) ? (p - num) : (num - p);
  }
  return c;
}

int main() {
  int n, r, s;
  vector<int> outputs;

  cin >> n;
  for (int i = 0; i < n; ++i) {
    vector<int> relatives;
    cin >> r;
    for (int j = 0; j < r; ++j) {
      cin >> s;
      relatives.push_back(s);
    } 
    sort(relatives.begin(), relatives.end());
    outputs.push_back(cost(relatives, median(relatives)));
  }

  for (int i = 0; i < outputs.size(); ++i) {
    cout << outputs[i] << endl;
  }
}

