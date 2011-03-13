/*
ID: arkajit.d1
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

#define MAXS 20000
#define MAXP 2000

char s[MAXS+1];
int n;

// index of the previous letter in string
int prev_letter(int i) {
	do {
		i--;
	} while (i >= 0 && !isalpha(s[i]));
	return i;
}

// index of the next letter in string
int next_letter(int j) {
	do {
		j++;
	} while (j < n && !isalpha(s[j]));
	return j;
}

int expand(int i, int j, int len, int *iBest, int *jBest) {
	while (i >= 0 && j < n && (j-i) < MAXP
				 && isalpha(s[i]) && isalpha(s[j]) 
				 && toupper(s[i]) == toupper(s[j])) {
		len += 2;

		if (iBest) {
			*iBest = i;
		}

		if (jBest) {
			*jBest = j;
		}

		i = prev_letter(i);
		j = next_letter(j);
	}

	return (len < 0) ? 0 : len;
}

int longest_palindrome(int center, int *iBest, int *jBest) {
	int c = center / 2;
	
	if (center % 2 == 0) {  
		return expand(c, c, -1, iBest, jBest);
	} else { 
		// important to use next_letter instead of +1 to skip over nonletters	
		return expand(c, next_letter(c), 0, iBest, jBest);
	}	
}

int main() {
	ofstream fout("calfflac.out");
	ifstream fin("calfflac.in");

	fin.get(s, MAXS, EOF);
	fin.close();
	n = strlen(s);

	int left = 0;
	int right = 0;

	int leftBest = 0;
	int rightBest = 0;
	int longest = 0;

	// loop over all possible centers
	// center for an odd-length palindrome is on a letter
	// center for an even-length palindrome is on a space between letters
	for (int len, i = 0; i < 2*n-1; i++) {
		len = longest_palindrome(i, &left, &right);
		if (len > longest) {
			longest = len;
			leftBest = left;
			rightBest = right;
		}
	}

	fout << longest << endl;
	fout.write(&s[leftBest], rightBest-leftBest+1);
	fout << endl;
	fout.close();
	
	return 0;	
}
