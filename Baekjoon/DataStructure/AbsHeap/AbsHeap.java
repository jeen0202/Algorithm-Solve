import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Comparator;
public class AbsHeap{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/AbsHeap/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
//        InnerAbsHeap ah = new InnerAbsHeap();
        PriorityQueue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b){
               int ret = Math.abs(a) - Math.abs(b);
               if(ret==0) ret = a-b;
               return ret;
            }
        });
        while(n>0){
            int inputNum = Integer.parseInt(br.readLine());
            if(inputNum==0){
                if(queue.isEmpty()){
                    sb.append("0\n");
                }else{
                    sb.append(queue.poll());
                    sb.append("\n");
                }
            }else{
                queue.offer(inputNum);
            }
            n--;
        }

        System.out.println(sb);
    }
    // public static class InnerAbsHeap {
    //     private int[] heap = new int[100001];
    //     int size = 0;

    //     public void push(int n){
    //         heap[++size] = n;
    //         int cur = size;
    //         while(cur/2 != 0 && Math.abs(heap[cur/2]) >= Math.abs(n) && heap[cur/2] > n){
    //             int temp = heap[cur/2];
    //             heap[cur/2] = n;
    //             heap[cur] = temp;
    //             cur = cur/2;
                
    //         }
    //     }
    //     public int pop(){
    //         if(size<1) return 0;
    //         int ret = heap[1];
    //         heap[1] = heap[size];
    //         size --;
    //         int d = heap[1];
    //         int cur = 1;

    //         while (cur*2 <=size){
    //             int change_i = cur*2;
    //             if(Math.abs(heap[cur*2]) <= Math.abs(d) && heap[cur*2] < d && Math.abs(heap[cur*2+1]) <= Math.abs(d) && heap[cur*2+1] < d){
    //                 if(Math.abs(heap[cur*2]) >= Math.abs(heap[cur*2+1]) && heap[cur*2] > heap[cur*2+1]){
    //                     change_i = cur*2+1;
    //                 }
    //             }else if(Math.abs(heap[cur*2]) <= Math.abs(d) && heap[cur*2] <d){
    //                 change_i = cur*2;
    //             }else if(Math.abs(heap[cur*2+1])<=Math.abs(d) && heap[cur*2+1] < d){
    //                 change_i = cur*2+1;
    //             }else{
    //                 break;
    //             }
    //             int temp = heap[change_i];
    //             heap[change_i] = heap[cur];
    //             heap[cur] = temp;
    //             cur = change_i;
    //         }
    //         return ret;
    //     }
        
    // }
}

