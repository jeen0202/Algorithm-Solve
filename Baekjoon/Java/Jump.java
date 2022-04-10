import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Jump {
    static int points[][];
    static int dp[][];
    public static void main(String args[]) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int n = Integer.parseInt(br.readLine());
        long [][] dp = new long[n+1][n+1];
        points = new int[n+1][n+1];
        for (int i = 0; i < n; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                points[i][j] = Integer.parseInt(row[j]);
            }
        }
        dp[0][0] = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(i ==n-1 && j == n-1){
                    continue;
                }
                if(j+points[i][j] <n){
                    dp[i][j+points[i][j]] += dp[i][j];
                }
                if(i+points[i][j] < n){
                    dp[i+points[i][j]][j] += dp[i][j];
                }
            }
        }
        System.out.println(dp[n-1][n-1]);
    }
}
