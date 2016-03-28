#include <cstdio>
#include <cstdlib>
#include <ctime>

long long PowIterative(long long a, long long n, long long MOD) {
  long long res = 1;
  while (n) {
    // If the last bit of number is 1.
    if (n & 1) {
      res = res * a % MOD;
    }
    a = a * a % MOD;
    // Ommitting the last bit of the number.
    n >>= 1;
  }

  return res;
}

long long PowRecursive(long long a, long long n, long long MOD) {
  if(n == 0) return 1;
  if(n == 1) return a;

  // If number is odd.
  if (n & 1) {
    return PowRecursive(a, n - 1, MOD) * a % MOD;
  } else {
    // Here number is even.
    long long tmp = PowRecursive(a, n / 2, MOD);

    return tmp * tmp % MOD;
  }
}

long long PowNaive(long long a, int n, long long MOD) {
  long long res = 1;
  for (int it = 1; it <= n; ++it) {
    res = res * a % MOD;
  }

  return res;
}

int GetRandomInRange(int range_begin, int range_end) {
  return range_begin + (rand() % (int)(range_end - range_begin + 1));
}

int main(int argc, char *argv[]) {
  srand(time(NULL));
  int TEST_COUNT = 100;

  for (int test_id = 1; test_id <= TEST_COUNT; ++test_id) {
    int a = GetRandomInRange(1, 100000);
    int n = GetRandomInRange(1000000, 1000000);
    int mod = GetRandomInRange(1, 10000000);

    long long res_naive = PowNaive(a, n, mod);

    // Measure and store the running time and result of smart iterative.
    clock_t begin_iterative = clock();
    long long res_iterative = PowIterative(a, n, mod);
    clock_t end_iterative = clock();

    // Measure and store the running time and result of smart recursive.
    clock_t begin_recursive = clock();
    long long res_recursive = PowRecursive(a, n, mod);
    clock_t end_recursive = clock();

    // Here we have mismatch, something is wrong.
    if (res_naive != res_iterative || res_naive != res_recursive) {
      printf("FAILURE\nTest(#%d) failed: Naive(%lld) Recursive(%lld) Iterative(%lld)\n",
          test_id, res_naive, res_recursive, res_iterative);
    }
    else {
      printf("SUCCESS\n");
      // Here test passed, just comparing running times.
      printf("Recursive running time=%.2lf vs Iterative running time=%.2lf\n",
          (double)(end_recursive - begin_recursive) / CLOCKS_PER_SEC,
          (double)(end_iterative - begin_iterative) / CLOCKS_PER_SEC);
    }
  }

  return EXIT_SUCCESS;
}
