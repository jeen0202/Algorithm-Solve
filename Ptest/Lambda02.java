import java.util.*;

public class Lambda02 {
    @FunctionalInterface
    public interface Mynumber{
        int getMax(int num1, int num2);
    }
    public static void main(String[] args) {
        Mynumber max = (x,y)->(x>=y)? x:y; // 삼항연산자 사용 return 생략
        //Mynumber max = (x,y)->{return x>=y ? x:y;}
        System.out.println(max.getMax(10,30));

        //Lambda를 사용한 Runnable 구현
        Thread thread = new Thread(()->{
            System.out.println("Start Thread");
            try {
                Thread.sleep(1000);
            } catch (Exception e) {
                e.printStackTrace();
            }
            System.out.println("End Thread");
        });

        //Lambda를 사용한 컬렉션 순회
        List<String> list = new ArrayList<String>();
        list.add("E1");
        list.add("E2");
        list.add("E3");

        list.forEach(x-> System.out.println(x));
    }
}
