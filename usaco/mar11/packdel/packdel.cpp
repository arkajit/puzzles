/*
ID: arkajit.d1
PROG: packdel
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <climits>

#define MAXN 50000
#define MAXM 50000
#define MAXC 1000
#define START 1

using namespace std;

int main() {
	ofstream fout("packdel.out");
	ifstream fin("packdel.in");

	typedef pair<int, int> IntPair;
	vector<IntPair> graph[MAXN+1]; // adjacency list representation of graph
	priority_queue<IntPair> q; // first = estimated dist, second = vertex #
	IntPair edge, ip;
	vector<IntPair> nbrs;

	// scores is the smallest distance we've found to a particular vertex
	int scores[MAXN+1];
	int a, b, c, N, M, dist, vertex;

	fin >> N >> M;

	scores[0] = INT_MAX;
	for (int i = 1; i <= N; i++) {
		graph[i] = vector<IntPair>();
		scores[i] = (i == START) ? 0 : INT_MAX;
	}
	q.push(make_pair(0, START));

	for (int i = 1; i <= M; i++) {
		fin >> a >> b >> c;
		graph[a].push_back(make_pair(b, c));
		graph[b].push_back(make_pair(a, c));	
	}
	fin.close();

	// priority_queue doesn't support the DecreaseKey operation you would normally
	// use in a MinHeap implementation of Dijkstra's
	// but you can avoid this by just readding an element with smaller key and
	// keeping track of the smallest key so far. Whenever we pop off a stale value
	// that's no longer the best, we just skip it.
	while (!q.empty()) {
		ip = q.top();
		dist = -ip.first;
		vertex = ip.second;
		q.pop();

		if (vertex == N) {
			break;
		}

		if (scores[vertex] < dist) {
			continue; // we've updated this entry already, skip it
		}

		nbrs = graph[vertex];
		for (int j = 0; j < nbrs.size(); j++) {
			edge = nbrs[j];
			b = edge.first; // next vertex
			c = edge.second; // cost of the edge
			if (dist + c < scores[b]) { // Relax operation
				scores[b] = dist + c;
				q.push(make_pair(-scores[b], b));
			}
		}
	}

	fout << scores[N] << endl;
	fout.close();
}
