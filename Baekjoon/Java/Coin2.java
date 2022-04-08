import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Coin2 {
    static int coins[];
    static long dp[];
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        coins = new int[n];
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        dp = new long[100001];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = 10001;
        }
        dp[0] = -1;
        for (int item : coins) {
            dp[item] = 1;
        }
        for (int i = 1; i < k+1; i++) {
            for (int coin : coins) {
                if(i-coin>0){
                    dp[i] = Math.min(dp[i],dp[i-coin]+1);
                }
            }
        }
        if(dp[k]==10001){
            System.out.println(-1);
        }else{
            System.out.println(dp[k]);
        }
    }    
}
