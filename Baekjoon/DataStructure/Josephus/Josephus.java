import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
public class Josephus{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Josephus/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        ArrayList<Integer> dq = new ArrayList<>();
        int point = 0;
        for(int i = 1;i<=n;i++) dq.add(i);
        while(!dq.isEmpty()){
            point = (point+k-1)%dq.size();
            sb.append(dq.remove(point));
            if(!dq.isEmpty()) sb.append(", ");
        }
        sb.append(">");
        System.out.println(sb);
    }
}

