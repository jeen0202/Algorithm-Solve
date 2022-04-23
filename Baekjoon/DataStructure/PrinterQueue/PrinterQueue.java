import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PrinterQueue{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/PrinterQueue/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        //테스트 케이스 t만큼 반복
        for(int i = 0; i < t ; i++ ){
            //중요도를 저장하기 위한 Queue 
            StringTokenizer st = new StringTokenizer(br.readLine());
            // n,m,중요도 list 저장
            int n,m,max = 0,cnt = 0;
            int[] list = new int[100];;            
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            //list에 data 입력          
            for(int j = 0 ; j < n ; j++){
                int temp = Integer.parseInt(st.nextToken());
                list[j] = temp;
            }
            //while문을 순회하며 위치정보를 확인할 변수 now
            int now = 0;
            //m위치의 문서가 출력될때 까지 반복
            while(list[m]!=0){
                // list내의 중요도의 max값 검색
                for(int j = 0 ; j < n ; j++) max = max>=list[j]?max:list[j];
                // 조건에 부합하는 문서 출력
                if(list[now] != 0 && list[now]>=max){
                    list[now] = 0;
                    cnt++;
                }
                //list순회를 위해 now 증가
                now = (now+1)%n;
            max = 0;
            //최대값 초기화
        }
            System.out.println(cnt);                        
        }
    }
}

