class Housekim{
    static String lastname = "김"; // Housekim 클래스가 공유하는 상수로, 메모리에 1회 할당되고 모든 Houskim 클래스가 공유
};
class Counter{
    static int count = 0; // 모든 Counter 객체가 공유하는 전역변수처럼 사용가능
    Counter(){
        // this.count++; static 사용시 각 객체의 멤버변수가 아니므로 this 불필요
        count++;
        System.out.println(count);
    }
    // Static Method => 클래스 자제적으로 호출 가능
    // 유틸리티성 Method 생성에 주로 사용됨
    public static int getCount(){ 
        return count;
    }
}
// Static을 사용한 Singleton 패턴 : 클래스를 통해 단 하나의 객체만을 생성하여 사용하는 방식
class Singleton{
    private static Singleton one;
    private Singleton(){

    }
    public static Singleton getInstance() {
        if(one == null){
            one = new Singleton();
        }
        return one;
    }
}
public class Static{
    public static void main(String[] args){
        // 멤버변수 lastname을 공유합니다.
        Housekim kim1 = new Housekim();
        Housekim kim2 = new Housekim();
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        System.out.println(Counter.getCount()); // 클래스를 사용하여 Static Method 호출
        
        // Singleton : getInstance를 여러번 호출해도 객체는 1개만 존재
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();
        System.out.println(singleton1 == singleton2);
    }
}