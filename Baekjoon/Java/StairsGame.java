import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class StairsGame {
    static int[] stairs;
    static int[] dp;
    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/java/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int n = Integer.parseInt(br.readLine());
        stairs = new int[n];
        for(int i=0;i<n;i++){
            stairs[i] = Integer.parseInt(br.readLine());
        }
        if(n<3){ 
            int sum = 0;
            for (int stair : stairs) {
                sum+= stair;
            }
            System.out.println(sum);
            System.exit(0);
        }
        dp = new int[n+1];
        dp[1] = stairs[0];
        dp[2] = stairs[0]+stairs[1];
        for(int i = 3; i<n+1; i++){
            dp[i] = dp[i-3]+stairs[i-2]+stairs[i-1] >dp[i-2]+stairs[i-1] ? dp[i-3]+stairs[i-2]+stairs[i-1]:dp[i-2]+stairs[i-1];
        }
        System.out.println(dp[n]);
    }
}
