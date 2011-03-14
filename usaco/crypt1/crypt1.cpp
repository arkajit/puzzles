/*
ID: arkajit.d1
PROG: crypt1
LANG: C++
*/
#include <iostream>
#include <fstream>

#define MAXN 9

using namespace std;

int n, digits[10]; // 1 if we can use the digit

int is_num_valid(int num, int len) {
	for (; len > 0; len--) {
		if (num && digits[num % 10]) {
			num /= 10;
		}	else {
			return 0;
		}
	}

	return (num == 0) ? 1 : 0;
}

int main() {
	ofstream fout("crypt1.out");
	ifstream fin("crypt1.in");
	int d, total = 0;

	for (int i = 0; i < 10; i++) {
		digits[i] = 0;
	}

	fin >> n;

	for (int i = 0; i < n; i++) {
		fin >> d;
		digits[d] = 1;
	}

	fin.close();

	// a = 3-digit top number
	// b = 2-digit bottom number
	for (int a = 111; a < 1000; a++) {
		if (is_num_valid(a, 3)) {
			for (int b = 11; b < 100; b++) {
				if (is_num_valid(b, 2)) {	
					// check total product and both partial products
					if (is_num_valid(a*b, 4) &&
							is_num_valid(a*(b % 10), 3) &&
							is_num_valid(a*(b / 10), 3)) {
						total += 1;	
						//cout << "a = " << a << ", b = " << b << endl;
					}
				}
			}
		}
	}

	fout << total << endl;
	fout.close(); 	

	return 0;
}
