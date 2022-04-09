import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
public class Pinary {
    static long[] dp;
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int n = Integer.parseInt(br.readLine());
        dp = new long[n];
        for (int i = 0; i < n; i++) {
            dp[i]=0;
        }
        dp[0] = 1;
        if(n>=2){
            dp[1]=1;
        }
        for (int i = 2; i < dp.length; i++) {
            dp[i] = dp[i-1]+dp[i-2];            
        }
        System.out.println(dp[n-1]);
    }
}