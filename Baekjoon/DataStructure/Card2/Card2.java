import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Card2{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream("Baekjoon/DataStructure/Card2/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> cards = new ArrayDeque<>();
        for(int i = 1; i<=n;i++){
            cards.add(i);
        }
        for(int j = 0;j<n-1;j++){
            cards.removeFirst();
            cards.addLast(cards.removeFirst());
        }
        System.out.println(cards.getFirst());
    }
}

 
