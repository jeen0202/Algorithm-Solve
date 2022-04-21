import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class Deque01{    
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Deque01/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        List<Integer> dq = new ArrayList<Integer>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0 ; i < n ; i++){
            StringTokenizer  st = new StringTokenizer(br.readLine());
            String keyword = st.nextToken();
            if(keyword.equals("push_front")){
                dq.add(0, Integer.parseInt(st.nextToken()));
            }else if(keyword.equals("push_back")){
                dq.add(dq.size(),Integer.parseInt(st.nextToken()));
            }else if(keyword.equals("pop_front")){
                if(dq.isEmpty())
                    sb.append(("-1\n"));
                else{
                    sb.append(dq.get(0));
                    sb.append("\n");
                    dq.remove(0);
                }
            }else if(keyword.equals("pop_back")){
                if(dq.isEmpty())
                    sb.append(("-1\n"));
                else{
                    sb.append(dq.get(dq.size()-1));
                    sb.append("\n");
                    dq.remove(dq.get(dq.size()-1));
                }
            }else if(keyword.equals("size")){
                sb.append((dq.size())+"\n");
            }else if(keyword.equals("empty")){
                sb.append(((dq.isEmpty()?1:0)+"\n"));
            }
            else if(keyword.equals("front")){
                if(dq.isEmpty())
                    sb.append("-1\n");
                else{
                    sb.append(dq.get(0));
                    sb.append("\n");
                }
            }else if(keyword.equals("back")){
                if(dq.isEmpty())
                    sb.append("-1\n");
                else{
                    sb.append(dq.get(dq.size()-1));
                    sb.append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}