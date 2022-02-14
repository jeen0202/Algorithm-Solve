package Baekjoon.BruteForce.PDG;
import java.io.*;

public class PDG {
    static int a, t, k;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        a = Integer.parseInt(br.readLine());
        t = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        int ans = solution();
        System.out.println(ans);
    }

    static int solution(){
        int p = 0, d = 0, cnt = 2;
        while(true){
            for (int i = 0;i<4;i++){
                if (i%2 == 0){
                    p++;
                }else{
                    d++;
                }
                if (p==t && k == 0){
                    return (p+d-1) %a;
                }
                if(d==t && k ==1){
                    return (p+d-1) %a;
                }
            }
            for(int i = 0;i<cnt;i++){
                p++;
                if(p==t && k == 0){
                    return (p+d-1) %a;
                }
            }
            for(int i =0;i<cnt;i++){
                d++;
                if(d==t && k == 1){
                    return (p+d-1)%a;
                }
            }
            cnt++;
        }
    }
}
