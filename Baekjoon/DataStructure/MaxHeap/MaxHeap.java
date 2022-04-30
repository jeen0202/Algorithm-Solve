import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class MaxHeap{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/MaxHeap/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        InnerMaxHeap q = new InnerMaxHeap();
        for(int i = 0 ; i < n ; i++){
            int inputNum = Integer.parseInt(br.readLine());
            if(inputNum ==0){
                    sb.append(q.pop());
                    sb.append("\n");    
            }else{
                q.push(inputNum);
            }
        }
        System.out.println(sb);
    }
    public static class InnerMaxHeap {
        private int[] heap = new int[100001];
        int size = 0;
        
        public void push(int intNum){
            heap[++size] = intNum;

            int cur = size;
            while(cur/2 != 0 && heap[cur/2] < intNum){
                int temp = heap[cur/2];
                heap[cur/2] = intNum;
                heap[cur] = temp;
                cur = cur/2;
            }
        }
        public int pop(){
            if(size <1) return 0;
            int root = heap[1];

            heap[1] = heap[size];
            size--;

            int d = heap[1];
            int cur = 1;

            while(cur*2 <= size){
                int change_i = cur*2;
                if(heap[cur*2] > d && heap[cur*2+1] > d){
                    if(heap[cur*2] < heap[cur*2+1]){
                        change_i = cur*2+1;
                    }
                }else if(heap[cur*2] > d){
                        change_i = cur*2;
                    }else if(heap[cur*2+1]> d){
                        change_i = cur*2 +1;
                    }else{
                        break;
                    }
                    int temp = heap[change_i];
                    heap[change_i] = heap[cur];
                    heap[cur] = temp;
                    cur = change_i;
                }
            return root;
        }
    }
}