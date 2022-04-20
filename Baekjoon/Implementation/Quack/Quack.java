import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Quack{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/Implementation/Quack/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String v = br.readLine();
        int[] check ={0,0,0,0,0};
        int duck = 0;
        int ret = 0;
        for (int i = 0; i < v.length(); i++) {
            char temp = v.charAt(i);
            if(temp== 'q'){
                check[0]++;
                duck++;
                ret = Math.max(ret,duck);
            }else if(temp == 'u'){
                check[1]++;
                if(check[1]>check[0]){
                    System.out.println(-1);
                    System.exit(0);
                }
            }else if(temp == 'a'){
                check[2]++;
                if(check[2]>check[1]){
                    System.out.println(-1);
                    System.exit(0);
                }
            }else if(temp == 'c'){
                check[3]++;
                if(check[3]>check[2]){
                    System.out.println(-1);
                    System.exit(0);
                }
            }else if(temp == 'k'){
                check[4]++;
                if(check[4]>check[3]){
                    System.out.println(-1);
                    System.exit(0);
                }
                duck--;
            }else{
                System.out.println(-1);
                System.exit(0);
            }
        }
        if(check[1]==check[0]&& check[2]==check[1]&&check[3]==check[2]&&check[4]==check[3])
            System.out.println(ret);
        else System.out.println(-1);
        }
}

