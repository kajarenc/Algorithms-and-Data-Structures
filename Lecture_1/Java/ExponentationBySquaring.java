import java.io.IOException;
import java.util.Random;


public class ExponentationBySquaring {
	
	public static int GetRandomInRange(int begin, int end) {
		Random rand = new Random();
		
		return begin + rand.nextInt(end - begin + 1);
	}
	
	public static long NaiveExponentation(long a, int n, long mod) {
		long res = 1;
		for (int i = 1; i <= n; ++i) {
			res = res * a % mod;
		}
		
		return res;
	}
	
	public static long IterativeExponentation(long a, long n, long mod) {
		long res = 1;
		while (n > 0) {
			if(n % 2 == 1) {
				res = res * a % mod;
			}
			a = a * a % mod;
			n >>= 1;
		}
		
		return res;
	}
	
	public static long RecursiveExponentation(long a, long n, long mod) {
		if (n == 0L) {
			return 1;
		}
		if (n == 1L) {
			return a % mod;
		}
		if (n % 2 == 1) {
			return a * RecursiveExponentation(a, n - 1, mod) % mod;
		}
		else {
			long temp = RecursiveExponentation(a, n / 2, mod);
			
			return temp * temp % mod;
		}
	}
	
	public static void main(String args[]) throws IOException {
		int testCount = 100;
		
		for (int test_id = 1; test_id <= testCount; ++test_id) {
			int a = GetRandomInRange(1, 10000);
			int n = GetRandomInRange(1, 10000000);
			int mod = GetRandomInRange(1, 1000000);
			
			long naiveRes = NaiveExponentation(a, n, mod);
			
			long recursiveExpoBegin = System.currentTimeMillis();
			long resRecursive = RecursiveExponentation(a, n, mod);
			long recursiveExpoEnd = System.currentTimeMillis();
			
			long iterativeExpoBegin = System.currentTimeMillis();
			long resIterative = IterativeExponentation(a, n, mod);
			long iterativeExpoEnd = System.currentTimeMillis();
			
			if (naiveRes != resIterative || naiveRes != resRecursive) {
				System.out.println("FAILURE: naiveRes=" + naiveRes +
						" iterativeRes=" + resIterative + " recursiveRes=" +
						resRecursive);
			}
			else {
				System.out.println("Iterative running time=" + 
					(double)(iterativeExpoEnd - iterativeExpoBegin) / 1000.0 + " vs " +
				"Recursive running time=" + (double)(recursiveExpoEnd - recursiveExpoBegin) / 1000.0);
			}
		}
	}
}

