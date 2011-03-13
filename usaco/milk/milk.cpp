/*
ID: arkajit.d1
PROG: milk
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main() {
	ofstream fout("milk.out");
	ifstream fin("milk.in");

	int p, q, target, nFarms, cost = 0;
	multimap<int, int> farms;	

	fin >> target >> nFarms;
	
	for (int i = 0; i < nFarms; i++) {
		fin >> p >> q;
		farms.insert(make_pair(p, q));
	}
	fin.close();

	for (multimap<int, int>::iterator it = farms.begin(); 
			 it != farms.end() && target > 0; it++) {
		p = (*it).first;
		q = (*it).second;
		
		if (q < target) {
			cost += p*q;
			target -= q;
		}	else {
			cost += p*target;
			target = 0;
		}
	}

	fout << cost << endl;
	fout.close();	
	return 0;
}
