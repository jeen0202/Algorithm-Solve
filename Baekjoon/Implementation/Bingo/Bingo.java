import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.StringTokennizer;

public class Bingo{
    static int[][] t = new int[5][5];
    static int[] c = new int[26];
    static int count = 0;
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/Implementation/Bingo/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine(), );
        for(int i = 0; i <5;i++){
            String[] line = br.readLine().split(" ");
            for(int j = 0;j<5;j++){
                t[i][j] = Integer.parseInt(line[j]);
            }
        }
        for(int i = 0;i<5;i++){
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < 5; j++) {  
                c[(i*5)+j+1] = Integer.parseInt(line[j]);            
        
        }
    }
        for (int k = 1; k < 26; k++) {
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    if(t[i][j] == c[k]){
                        t[i][j] =0;
                    }
                    checkC();
                    checkR();
                    checkLC();
                    checkRC();
                    if(count >=3){
                        System.out.println(k);
                        System.exit(0);
                    }
                    count = 0;
                }
            }
        }
    }
    public static void checkR(){
        for (int i = 0; i < 5; i++) {
            int cnt = 0;
            for (int j = 0; j < 5; j++) {
                if(t[i][j] == 0) cnt++;
            }
            if(cnt==5) count++;
        }
    }
    public static void checkC(){
        for (int i = 0; i < 5; i++) {
            int cnt = 0;
            for (int j = 0; j < 5; j++) {
                if(t[j][i] == 0) cnt++;
            }
            if(cnt==5) count++;
        }
    }
    public static void checkRC(){
        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if(t[i][i] == 0) cnt++;
        }
        if(cnt==5) count++;
    }
    public static void checkLC(){
        int cnt = 0;
        for(int i =0; i<5;i++){
            if(t[i][4-i] == 0) cnt++;
        }
        if(cnt==5) count++;
    }
}

