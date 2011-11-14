/*
ID: arkajit.d1
PROG: lineup
LANG: C++
*/

#include <fstream>
#include <iostream>
#include <map>
#include <set>

#define MAX_BEST 1e9

using namespace std;

int main() {
  ofstream fout("lineup.out");
  ifstream fin("lineup.in");

  // Read input into data structures
  int x, breed, N;
  map<int,int> cows, counts;
  set<int> unseen;

  fin >> N;
  for (int i = 0 ; i < N; ++i) {
    fin >> x >> breed;
    cows[x] = breed;
    counts[breed] = 0;
    unseen.insert(breed);
  }
  fin.close();

  // Find best photo
  map<int,int>::iterator start = cows.begin();
  map<int,int>::iterator end = cows.begin();
  int cost, best = MAX_BEST;

  counts[start->second]++;
  unseen.erase(start->second);
  while (end != cows.end()) {
    if (unseen.empty()) {  // feasible photo
      cost = end->first - start->first;
      if (cost < best) {
        best = cost;
      }

      // advance start edge of photo
      counts[start->second]--;
      if (counts[start->second] == 0) {
        unseen.insert(start->second);
      }
      start++;
    } else {  // not a feasible photo, expand end edge of photo
      end++;
      if (end != cows.end()) {
        counts[end->second]++;
        unseen.erase(end->second);
      }
    }   
  }

  // Output answer
  fout << best << endl;
  fout.close();
  
  return 0;
}
