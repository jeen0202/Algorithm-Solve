import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;


public class Deque01{    
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Deque01/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Deque<Integer> dq = new ArrayDeque<Integer>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < n ; i++){
            String line = br.readLine();
            String keyword = line.split(" ")[0];
            if(keyword.equals("push_front")){
                dq.addFirst(Integer.parseInt(line.split(" ")[1]));
            }else if(keyword.equals("push_back")){
                dq.addLast(Integer.parseInt(line.split(" ")[1]));
            }else if(keyword.equals("pop_front")){
                if(dq.isEmpty())
                    sb.append((-1+"\n"));
                else{
                    sb.append((dq.removeFirst())+"\n");
                }
            }else if(keyword.equals("pop_back")){
                if(dq.isEmpty())
                    sb.append((-1+"\n"));
                else{
                    sb.append((dq.removeLast())+"\n");
                }
            }else if(keyword.equals("size")){
                sb.append((dq.size())+"\n");
            }else if(keyword.equals("empty")){
                sb.append(((dq.isEmpty()?1:0)+"\n"));
            }
            else if(keyword.equals("front")){
                if(dq.isEmpty())
                    sb.append((-1+"\n"));
                else{
                    sb.append((dq.getFirst())+"\n");
                }
            }else if(keyword.equals("back")){
                if(dq.isEmpty())
                    sb.append((-1+"\n"));
                else{
                    sb.append((dq.getLast())+"\n");
                }
            }
        }
        System.out.println(sb);
    }
}