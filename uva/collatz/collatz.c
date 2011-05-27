#include <stdio.h>

int cycle_length(int n) {
  int i = 1;
  while (n != 1) {
    if (n % 2) {
      n = 3*n+1;
    } else {
      n = n/2;
    }
    i++;
  }
  return i;
}

int main() {
  int c, i, i0, j, j0, k, best;

  while (scanf("%d %d", &i, &j) != EOF) {
    i0 = i;
    j0 = j;

    /* swap order */
    if (i > j) {
      c = i;
      i = j;
      j = c;
    }

    best = cycle_length(j);
    for (k = i; k < j; k++) {
      c = cycle_length(k);
      best = (c > best) ? c : best; 
    }
    printf("%d %d %d\n", i0, j0, best);
  }
}
