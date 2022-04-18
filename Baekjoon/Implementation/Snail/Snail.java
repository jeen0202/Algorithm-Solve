import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.StringTokennizer;

public class Snail{
    public static int[][] graph;
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/Implementation/Snail/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine(), );
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int max  = n*n;
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};
        int ax = 0,ay = 0;
        graph = new int[n][n];
        for (int i = 0; i < n/2+1; i++) {
            int r = i;
            int c = i;
            int idx = 0;

            graph[i][i] = max--;

            while(idx <4){
                int rr = r + dx[idx];
                int cc = c + dy[idx];

                if(rr< 0 || rr >=n|| cc >= n || cc <0){
                    idx++;
                }else if(graph[rr][cc] != 0){
                    idx++;
                }else{
                    graph[rr][cc] = max--;
                    r = rr;
                    c = cc;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if(graph[i][j]==m){
                    ax = i+1;
                    ay = j+1;
                }
                System.out.print(graph[i][j]+" ");        
            }
            System.out.println();
        }
        System.out.println(ax+" "+ay);
    }
}

