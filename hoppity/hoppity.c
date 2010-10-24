/*
puzzle: hoppity
lang: C
author: arkajit (arkajit.dey@gmail.com)
*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  FILE *fp;
  int i, n;

  if (argc != 2) {
    printf("Usage: hop <filename>\n");
    return 1;
  }

  fp = fopen(argv[1], "r");
  if (fp == NULL) {
    printf("Error: Could not open file\n");
    return 1;
  }

  fscanf(fp, "%d", &n);
  fclose(fp);
  for (i = 1; i <= n; i++) {
    if (i % 3 == 0 && i % 5 == 0)
      printf("Hop\n");
    else if (i % 3 == 0)
      printf("Hoppity\n");
    else if (i % 5 == 0)
      printf("Hophop\n");
  }
       
  return 0; 
}
