import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
public class Fibo2 {
    static long[] dp;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int T = Integer.parseInt(br.readLine());
        dp = new long[T+1];
        dp[0] = 0;
        dp[1]=  1;
        for (int i = 2; i < dp.length; i++) {
            dp[i] = dp[i-1]+dp[i-2];            
        }
        System.out.println(dp[T]);
    }
}
