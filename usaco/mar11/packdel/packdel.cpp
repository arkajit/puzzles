/*
ID: arkajit.d1
PROG: packdel
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>
#include <vector>
#include <utility>
#include <climits>
#include <algorithm>

#define MAXN 50000
#define MAXM 50000
#define MAXC 1000
#define START 1

using namespace std;

template<typename F, typename S>
struct PairComparator {
	bool operator() (const pair<F, S>& p1, const pair<F, S>& p2) {
		return p1.second > p2.second;
	}
};

int main() {
	ofstream fout("packdel.out");
	ifstream fin("packdel.in");

	typedef pair<int, int> IntPair;
	typedef struct PairComparator<int, int> IPC;
//	priority_queue<IntPair, vector<IntPair>, IDPC > q;
//	vector<IntPair> dists;
	map<int, vector<IntPair> > graph;

	IntPair edge;
	vector<IntPair> vec;
	int unvisited[MAXN+1], scores[MAXN+1];
	int a, b, c, N, M, bestScore;

	fin >> N >> M;

	scores[0] = INT_MAX;
	for (int i = 1; i <= N; i++) {
		graph[i] = vector<IntPair>();
		unvisited[i] = 1;
		scores[i] = (i == START) ? 0 : INT_MAX;
//		dists.push_back(make_pair(i, (i == START) ? 0 : INT_MAX));
		//q.push(make_pair(i, (i == START) ? 0 : INT_MAX));
	}
	bestScore = START;

	for (int i = 1; i <= M; i++) {
		fin >> a >> b >> c;
		graph[a].push_back(make_pair(b, c));
		graph[b].push_back(make_pair(a, c));	
	}
	fin.close();

	/* TEST input
	for (int i = 1; i <= N; i++) {
		cout << "Vertex " << i << " has the following neighbors: " << endl;
		vec = graph[i];
		for (int j = 0; j < vec.size(); j++) {
			ip = vec[j];
			cout << "Vertex " << ip.first << " with weight " << ip.second << endl;
		}
	}
	*/ 

	/* TEST queue order */

	for (int i = 1; i <= N; i++) {
		int v = bestScore;
		unvisited[v] = 0;
		vec = graph[v];
		for (int j = 0; j < vec.size(); j++) {
			edge = vec[j];
			if (bestScore + edge.second < scores[edge.first]) {
				scores[edge.first] = bestScore + edge.second;
			}
		}

		bestScore = 0;
		for (int i = 1; i <= N; i++) {
			if (unvisited[i] && scores[i] < scores[bestScore]) {
				bestScore = i;
			}
		}
	}

	fout << scores[N] << endl;
	fout.close();
}

