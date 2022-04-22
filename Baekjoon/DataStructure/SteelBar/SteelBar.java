import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
public class SteelBar{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/SteelBar/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack = new Stack<>();
        char[] line = br.readLine().toCharArray();
        int ans = 0, cnt = 0;
        boolean flag = false;
        for (char c : line) {
            if(c =='('){
                stack.add((cnt+1));
                flag = true;                
                cnt+=1;
            }
            else{
                cnt -=1;
                if(flag == true){
                    ans += cnt;
                    flag = false;
                }else if(!stack.isEmpty())
                ans+=1;
                stack.pop();
                
            }
        }
        System.out.println(ans);

    }
}

