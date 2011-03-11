/*
ID: arkajit.d1
LANG: C
TASK: ride
*/

#include <stdio.h>

int main() {
	FILE *fin = fopen("ride.in", "r");
	FILE *fout = fopen("ride.out", "w");
	char comet[6], group[6];
	int i;
	int c = 1;
	int g = 1;
	
	fscanf(fin, "%s", comet);
	fscanf(fin, "%s", group);
	fclose(fin);

	for (i = 0; i < 6; i++) {
		c = (comet[i]) ? (c * (comet[i]-64)) % 47 : c;
		g = (group[i]) ? (g * (group[i]-64)) % 47 : g;
	}

	if (c == g) {
		fprintf(fout, "GO\n");
	} else {
		fprintf(fout, "STAY\n");
	}
	fclose(fout);

	return 0;
}
