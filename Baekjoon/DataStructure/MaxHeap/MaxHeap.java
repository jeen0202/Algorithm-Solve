import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class MaxHeap{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/MaxHeap/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        long n = Long.parseLong(br.readLine());
        PriorityQueue<Long> q = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0 ; i < n ; i++){
            long inputNum = Long.parseLong(br.readLine());
            if(inputNum ==0){
                if(q.isEmpty()){
                    sb.append(0);
                    sb.append("\n");
                }else{
                    sb.append(q.peek());
                    sb.append("\n");    
                    q.remove(q.peek());
                }
            }else{
                q.add(inputNum);
            }
        }
        System.out.println(sb);
    }
}

