/*
ID: arkajit.d1
PROG: ride
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("ride.out");
    ifstream fin ("ride.in");
		string comet, group;
    int c = 1;
		int g = 1;

		getline(fin, comet);
		getline(fin, group);
		fin.close();
    
		for (int i = 0; i < comet.length(); i++) {
			c = (c * (int(comet[i]) - 64)) % 47;
		}

		for (int i = 0; i < group.length(); i++) {
			g = (g * (int(group[i]) - 64)) % 47;
		}

		if (c == g) {
			fout << "GO" << endl;
		} else {
			fout << "STAY" << endl;	
		}
		fout.close();

    return 0;
}
