@FunctionalInterface
interface Say{
    int something(int a,int b);
}
class Person{
    public void hi(Say line){
        int number = line.something(3,4);
        System.out.println("Number is "+number);
    }
}

public class Lamda01 {
    public static void main(String[] args) {
        Person kim = new Person();
        kim.hi(new Say(){
            public int something(int a, int b){
                System.out.println("My name is janjan-Coding");
                System.out.println("Nice to meet you");
                System.out.println("parameter number is"+a+","+b);
                return 7;
            }
        });
        //람다식 사용
        kim.hi((a,b)->{
            System.out.println("My name is janjan-Coding");
            System.out.println("Nice to meet you");
            System.out.println("parameter number is"+a+","+b);
            return 7;            
        });
    }
}
