#include <stdio.h>
#include <math.h>

#define MAXNUM 1000000

int cyc[MAXNUM+1] = {0};

int main() {
  int c, i, j, k, best;

/*
  for (k = 0; k < log2(MAXNUM); k++) {
    cyc[(int) pow(2, k)] = k+1;
  } 
*/

  cyc[1] = 1; /* initialize base case */

  while (scanf("%d %d", &i, &j) != EOF) {
    best = cycle_length(j);
    for (k = i; k < j; k++) {
      c = cycle_length(k);
      best = (c > best) ? c : best; 
    }
    printf("%d %d %d\n", i, j, best);
  }
}

int cycle_length(int n) {
  if (cyc[n] == 0) {
    if (n % 2) {
      cyc[n] = 1 + cycle_length(3*n+1);
    } else {
      cyc[n] = 1 + cycle_length(n/2);
    }
  }

  return cyc[n];
}
