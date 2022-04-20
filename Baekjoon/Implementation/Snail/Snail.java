import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Snail{
    public static int[][] graph;
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/Implementation/Snail/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //Buffer에 저장하여 한번에 출력(시간 절약)
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        //(1,1)에서 시작 => 최대값 출력
        int max  = n*n;
        // 반시계방향으로 전환하며 출력
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        // N x N 배열로 초기화
        int ax = 0;
        int ay = 0;
        graph = new int[n][n];
        for (int i = 0;i<(n/2)+1;i++){
            //
            int idx =0;
            int x = i;
            int y = i;
            graph[i][i] = max--;
            while(idx<4){
                int x2 = x + dx[idx];
                int y2 = y + dy[idx];
                if(x2<0 || x2>= n ||y2<0 || y2 >=n){
                    idx++;
                }else if(graph[x2][y2]!=0){
                    idx++;
                }else{
                    graph[x2][y2] = max--;
                    x = x2;
                    y = y2;
                }                
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(graph[i][j]==m){
                    ax = i+1;
                    ay = j+1;
                }
                sb.append(graph[i][j] + " ");      
            }
            sb.append("\n");
        }
        sb.append(ax+" "+ay);
        System.out.println(sb);
        br.close();
    }
}