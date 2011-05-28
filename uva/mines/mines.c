/*
	problem: minesweeper (110102/10189)
	author: arkajit.dey@gmail.com (Arkajit Dey)
*/

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

#define MAXNUM 100

int main() {
/* Symbol might not be defined by judge. Comment out during submission.
	#ifndef ONLINE_JUDGE
		close (0); open ("110102.in", O_RDONLY);
		close (1); open ("110102.out", O_WRONLY | O_CREAT | O_TRUNC, 0600);
	#endif
*/

	int i, j, n, m;
	int f = 1; 	/* field number */

	while (scanf("%d %d", &n, &m) != EOF && n && m) {
		/* Read input: */

		getchar(); /* skip newline */

		/* padding to prevent out-of-bounds, extra space for \0,\n */
		char mine[MAXNUM+10][MAXNUM+10]; 

		for (i = 1; i <= n; i++) {
			fgets(mine[i]+1, m+2, stdin);
		}

		/* Build mine counts array */
		int cnts[MAXNUM+10][MAXNUM+10] = {0};
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				if (mine[i][j] == '*') {
					cnts[i-1][j-1]++;
					cnts[i-1][j]++;
					cnts[i-1][j+1]++;

					cnts[i][j-1]++;
					cnts[i][j+1]++;

					cnts[i+1][j-1]++;
					cnts[i+1][j]++;
					cnts[i+1][j+1]++;
				}	
			}
		}
		/* Write output */
		printf("Field #%d:\n", f);
		for (i = 1; i <= n; i++) {
			for (j = 1; j <= m; j++) {
				if (mine[i][j] == '*') {
					printf("*");
				} else {
					printf("%d", cnts[i][j]);
				}
			}
			printf("\n");
		}
		printf("\n");
		f++;
	}

	return 0;
}
