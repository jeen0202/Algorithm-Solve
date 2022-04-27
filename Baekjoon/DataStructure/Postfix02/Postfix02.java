import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Postfix02{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Postfix02/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] op = new int[n];
        char[] expression = br.readLine().toCharArray();
        Stack<Double> st = new Stack<>();
        for(int i = 0 ; i < n ; i++) op[i] =Integer.parseInt(br.readLine());
        for(int j = 0 ; j<expression.length ;j++){
            char temp = expression[j];
            if('A'<=temp && temp <='Z'){
                double t = op[temp-'A'];
                st.add(t);
            }else{
                double a = st.pop();
                double b = st.pop();
                switch(temp){
                    case '+':
                        st.push(a+b);
                        break;
                    case '-':
                        st.push(b-a);
                        break;
                    case '/':
                        st.push(b/a);
                        break;
                    case '*':
                        st.push(a*b);
                        break;
                }
            }
        }        
        System.out.printf("%.2f\n",st.pop());
    }
}

