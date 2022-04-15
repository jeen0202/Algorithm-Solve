import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Resignation {
    static int[][] list;
    static int[] dp;
    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        list = new int[n+2][2];
        dp = new int[n+2];
        String[] in;
        for(int i = 1;i<n+1;i++){
            in = br.readLine().split(" ");
            list[i][0] = Integer.parseInt(in[0]);
            list[i][1] = Integer.parseInt(in[1]);
        }
        for(int i = n; i>0; i--){
           if (i+list[i][0]>n+1) dp[i] = dp[i+1];
           else dp[i] = Math.max(dp[i+1], list[i][1]+dp[i+list[i][0]]);
        }
        System.out.println(dp[1]);

    }
}
