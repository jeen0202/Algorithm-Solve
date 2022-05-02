import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
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
        System.out.println(sb);
    }
    //절대값을 기준으로 정렬하는 Heap
    public static class InnerAbsHeap {
        //기본적인 heap구조를 위한 배열 과 size
        private int[] heap = new int[100001]; //heap[0]은 고려하지 않습니다.
        int size = 0;

        //push Method
        public void push(int n){
            heap[++size] = n; // size1 늘리면서 heap에 입력된 데이터 추가
            int cur = size; // 정렬을 시작 위치 지정(마지막 삽입된 원소)
            while(cur!=1){
                // 기준위치보다 낮은 위치의 절대값이 크거나, 절대값은 같은데 실제 값이 큰 경우 순서를 변경
                if(Math.abs(heap[cur/2])>Math.abs(heap[cur]) || (Math.abs(heap[cur/2])==Math.abs(heap[cur]) && heap[cur/2]>heap[cur])) {
                    int tmp = heap[cur/2];
                    heap[cur/2] = heap[cur];
                    heap[cur] = tmp;
                    cur/=2;
                }else break; // 조건에 부합하지않으면 정렬 종료
            }
        }
        public int pop(){
            // heap이 비어있으면 0을 반환합니다.
            if(size<1) return 0;
            int ret = heap[1]; // 기준에 의해 정렬된 가장 우선순위가 높은 값의 위치 = heap[1]
            heap[1] = heap[size--]; // 재정렬을 위해 heap의 최우선 위치에 가장 우선순위가 낮은 값 대입
            int cur = 1;
            while (cur*2 <=size){ // cur이 size 이상이 될때까지 증가해가면 비교
                int change_l = cur*2;  
                int change_r = cur*2+1;
                // 기준위치 상위의 값이 기준위치보다 우선순위가 높을 경우 위치를 변경해주는 조건식
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
                }else break; //어느 조건에도 부합하지 않으면 정렬 종료
            }
            return ret; // 우선수위 최상위값 반환
        }
        
    }
}

