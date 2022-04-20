import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;


public class Stack{
    static int[] stack = new int[10000];
    static int top = -1;
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Stack/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String order = br.readLine();
            String keyword = order.split(" ")[0];
            switch(keyword){
                case "push" :
                push(Integer.parseInt(order.split(" ")[1]));
                break;
                case "pop" :
                sb.append(pop()+"\n");
                break;
                case "size" :
                sb.append(size()+"\n");
                break;
                case "empty" :
                sb.append(empty()+"\n");
                break;
                case "top" :
                sb.append(top()+"\n");
                break;
            }
        }
        System.out.println(sb);
    }
    static void push(int inputNum){
        top++;
        stack[top] = inputNum;
    }
    static int pop(){
        return top<0?-1:stack[top--];
    }
    static int size(){
        return top+1;
    }
    static int empty(){
        return top<0?1:0;
    }
    static int top(){
        return top<0?-1:stack[top];
    }
}

