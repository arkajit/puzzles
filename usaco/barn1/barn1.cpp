/*
ID: arkajit.d1
PROG: barn1
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <queue>

using namespace std;

#define MAXM 50
#define MAXS 200

int stalls[MAXS+1];
int boards[MAXM+1];

int main() {
	ofstream fout("barn1.out");
	ifstream fin("barn1.in");

	int c, nBoards, nStalls, nCows;
	int first, last;

	for (int i = 0; i <= MAXS; i++) {
		stalls[i] = 0;
	}
	
	fin >> nBoards >> nStalls >> nCows;
	assert(nBoards >= 1 && nBoards <= MAXM);
	assert(nStalls >= 1 && nStalls <= MAXS);
	assert(nCows >= 1 && nCows <= nStalls);

	// Don't assume that the input is sorted
	for (int i = 0; i < nCows; i++) {
		fin >> c;	
		stalls[c] = 1;
	}
	fin.close();

	int totClear = 0; 	// number of stalls clear

	for (int i = 1; i <= nStalls; i++) {
		if (stalls[i]) {
			first = i;
			break;
		} else {
			totClear++;	
		}
	}

	for (int i = nStalls; i > 0; i--) {
		if (stalls[i]) {
			last = i;
			break;
		} else {
			totClear++;
		}
	}
	//cout << "First is " << first << " and last is " << last << endl;
	//cout << "total is " << totClear << endl;

	priority_queue<int> gaps;
	int run = 0;

	for (int i = first; i <= last; i++) {
		if (stalls[i] == 0) {
			run++;
		}	else if (run) {
			gaps.push(run);
			run = 0;
		}
	}


	for (int i = 1; i < nBoards && !gaps.empty(); i++) {
		totClear += gaps.top();
		gaps.pop();
	}

	fout << nStalls - totClear << endl;
	fout.close();

/* TEST input
	for (int i = 1; i <= nStalls; i++) {
		cout << "stalls[" << i << "] = " << stalls[i] << endl;
	}
*/

	return 0;
}
