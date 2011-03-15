/*
ID: arkajit.d1
PROG: packdel
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <utility>
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
	map<int, vector<IntPair> > graph;
	IntPair edge;
	vector<IntPair> vec;

	int unvisited[MAXN+1], scores[MAXN+1];
	// bit-vector of which nodes we haven't visited
	// scores is the smallest distance we've found to a particular vertex

	int a, b, c, N, M;
	int nextVertex; // the vertex with the next best score

	fin >> N >> M;

	scores[0] = INT_MAX;
	for (int i = 1; i <= N; i++) {
		graph[i] = vector<IntPair>();
		unvisited[i] = 1;
		scores[i] = (i == START) ? 0 : INT_MAX;
	}

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
			edge = vec[j];
			cout << "Vertex " << edge.first << " with weight " << edge.second << endl;
		}
	}
	*/ 

	// We'll visit exactly N vertices
	// Vist in order of current nextVertex
	// Find Min currently takes O(N). Can speed up with a min-heap, but didn't
	// have time to implement.
	nextVertex = START;
	for (int i = 1; i <= N; i++) {
		unvisited[nextVertex] = 0;
		vec = graph[nextVertex];
		for (int j = 0; j < vec.size(); j++) {
			edge = vec[j];
			// Relax operation
			if (scores[nextVertex] + edge.second < scores[edge.first]) {
				scores[edge.first] = scores[nextVertex] + edge.second;
			}
		}

		// find the next unvisited vertex with the lowest score
		nextVertex = 0;
		for (int i = 1; i <= N; i++) {
			if (unvisited[i] && scores[i] < scores[nextVertex]) {
				nextVertex = i;
			}
		}
	}

	fout << scores[N] << endl;
	fout.close();
}

