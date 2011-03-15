/*
ID: arkajit.d1
PROG: meetplace
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <set>

#define ROOT 1
#define MAXN 1000
#define MAXM 1000

using namespace std;

int main() {
	ofstream fout("meetplace.out");
	ifstream fin("meetplace.in");

	int parents[MAXN+1];
	int bessie[MAXM+1];
	int jonell[MAXM+1];
	int meet[MAXM+1];
	set<int> ancestors;
	int b, j, N, M;

	fin >> N >> M;
	parents[ROOT] = 0;
	for (int i = 2; i <= N; i++) {
		fin >> parents[i];
	}

	for (int i = 1; i <= M; i++) {
		fin >> bessie[i] >> jonell[i];
		meet[i] = 0;
	}
<<<<<<< HEAD
	fin.close();
=======
>>>>>>> 01ec7da... mar11 problem 1 first draft solution

	/* TEST Input
	for (int i = 1; i <= N; i++) {
		cout << "parents[" << i << "] = " << parents[i] << endl;
	}

	for (int i = 1; i <= M; i++) {
		cout << "bessie[" << i << "] = " << bessie[i] << endl;
		cout << "jonell[" << i << "] = " << jonell[i] << endl;
	}
	*/

	// Traverse from Bessie back to to ROOT, storing the path of nodes
	// Traverse from Jonell back, intersecting path with Bessie's path
	// Stop as soon as match is found or we hit ROOT
	for (int i = 1; i <= M; i++) {
		ancestors.clear();
		b = bessie[i];
		while (b != ROOT) {
			ancestors.insert(b);
			b = parents[b];	
		}

		j = jonell[i];
		while (j != ROOT && ancestors.count(j) == 0) {
			j = parents[j];
		}
		meet[i] = j;
	}

	// OUTPUT answer
	for (int i = 1; i <=M; i++) {
		fout << meet[i] << endl;
	}
<<<<<<< HEAD
	fout.close();
=======
>>>>>>> 01ec7da... mar11 problem 1 first draft solution

	return 0;
}
