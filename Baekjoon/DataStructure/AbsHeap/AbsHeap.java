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
        InnerAbsHeap ah = new InnerAbsHeap();
        while(n>0){
            int inputNum = Integer.parseInt(br.readLine());
            if(inputNum==0){
                sb.append(ah.pop());
                sb.append("\n");
            }else{
                ah.push(inputNum);
            }
            n--;
        }
        // PriorityQueue<Integer> queue = new PriorityQueue<>(new Comparator<Integer>() {
        //     @Override
        //     public int compare(Integer a, Integer b){
        //        int ret = Math.abs(a) - Math.abs(b);
        //        if(ret==0) ret = a-b;
        //        return ret;
        //     }
        // });
        // while(n>0){
        //     int inputNum = Integer.parseInt(br.readLine());
        //     if(inputNum==0){
        //         if(queue.isEmpty()){
        //             sb.append("0\n");
        //         }else{
        //             sb.append(queue.poll());
        //             sb.append("\n");
        //         }
        //     }else{
        //         queue.offer(inputNum);
        //     }
        //     n--;
        // }

        System.out.println(sb);
    }
    public static class InnerAbsHeap {
        private int[] heap = new int[100001];
        int size = 0;

        public void push(int n){
            heap[++size] = n;
            int cur = size;
            while(cur!=1){
                if(Math.abs(heap[cur/2])>Math.abs(heap[cur]) || (Math.abs(heap[cur/2])==Math.abs(heap[cur]) && heap[cur/2]>heap[cur])) {
                    int tmp = heap[cur/2];
                    heap[cur/2] = heap[cur];
                    heap[cur] = tmp;
                    cur/=2;
                }else break;
            }
        }
        public int pop(){
            if(size<1) return 0;
            int ret = heap[1];
            heap[1] = heap[size--];            
            int cur = 1;
            while (cur*2 <=size){
                int change_l = cur*2;
                int change_r = cur*2+1;
                boolean l_check = Math.abs(heap[change_l])<Math.abs(heap[cur]) && change_l <=size || (Math.abs(heap[change_l]) == Math.abs(heap[cur]) && heap[change_l]<heap[cur]);
                boolean r_check = Math.abs(heap[change_r])<Math.abs(heap[cur]) && change_r <=size || (Math.abs(heap[change_r]) == Math.abs(heap[cur]) && heap[change_r]<heap[cur]);
                if(l_check && r_check){
                    if(Math.abs(heap[change_l])<Math.abs(heap[change_r])){
                        int temp = heap[change_l];
                        heap[change_l] = heap[cur];
                        heap[cur] = temp;
                        cur = change_l;
                    }else if(Math.abs(heap[change_l]) > Math.abs(heap[change_r])){
                        int temp = heap[change_r];
                        heap[change_r] = heap[cur];
                        heap[cur] = temp;
                        cur = change_r;
                    }else{
                        if(heap[change_l]<heap[change_r]){
                            int temp = heap[change_l];
                            heap[change_l] = heap[cur];
                            heap[cur] = temp;
                            cur = change_l;
                        }else{
                            int temp = heap[change_r];
                            heap[change_r] = heap[cur];
                            heap[cur] = temp;
                            cur = change_r;
                        }
                    }
                }else if(l_check){
                    int temp = heap[change_l];
                    heap[change_l] = heap[cur];
                    heap[cur] = temp;
                    cur = change_l;
                }else if(r_check){
                    int temp = heap[change_r];
                    heap[change_r] = heap[cur];
                    heap[cur] = temp;
                    cur = change_r;                    
                }else break; 
            }
            return ret;
        }
        
    }
}

