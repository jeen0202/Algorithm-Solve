import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class StringSet{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/StringSet/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int n = Integer.parseInt(line.split(" ")[0]);
        int m = Integer.parseInt(line.split(" ")[1]);
        int ans = 0;
        String[] s = new String[n];
        for(int i = 0 ; i < n ; i++) s[i] = br.readLine();
        for(int j = 0 ; j < m ; j++){
            String temp = br.readLine();
            for(String item : s){
                if(item.equals(temp)){
                    ans +=1;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}

