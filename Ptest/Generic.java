import java.util.List;
import java.util.Map;

//Generic Class 예시
class ExClassGeneric<T>{
    private T t;

    public void setT(T t){
        this.t =t;
    }

    public T getT() {
        return t;
    }
}
//Generic Interface 예시
interface ExInterfaceGeneric<T>{
    T example();
}
class ExGeneric implements ExInterfaceGeneric<String>{
    @Override
    public String example(){ 
        return null;
    }
}
//Generic Method 예시
class People<T,M>{
    private T name;
    private M age;

    People(T name, M age){
        this.name = name;
        this.age = age;
    }

    public T getName(){
        return name;
    }

    public void setName(T name){
        this.name = name;
    }
    public M getAge(){
        return age;
    }
    public void setAge(M age){
        this.age = age;
    }
    //Generic Method : 일반 클래스 제너릭 클래스 구분없이 정의 가능
    public static<T,V> boolean compare(People<T,V>p1, People<T,V>p2){
        boolean nameCompare = p1.getName().equals(p2.getName());
        boolean ageCompare = p1.getAge().equals(p2.getAge());
        return nameCompare && ageCompare;
    }
}
//Multi type Parameter 사용
class ExMultiTypeGeneric<K,V> implements Map.Entry<K,V>{
    private K key;
    private V value;

    @Override
    public K getKey(){
        return this.key;
    }
    @Override
    public V getValue(){
        return this.value;
    }
    @Override
    public V setValue(V value){
        this.value = value;
        return value;
    }
}

public class Generic {
    // Generic Wildcard :  제너릭 클래스의 객체를 메소드의 매개변수로 받을때 ?를 사용해 그 객체의 타입 변수를 제한하는 방식
    // Type Parameter를 대치하기 위해 사용, 모든 클래스, 인터페이스타입 가능
    public void printList(List<?> list){
        for (Object obj : list){
            System.out.println(obj + " ");
        }
    }
    // <? extends 상위Object> : 와일드카드의 범위를 특정 객체의 하위클래스로 지정
    public int sum(List<? extends Number>list){
        int sum=0;
        for (Number i : list){
            sum += i.doubleValue();
        }
        return sum;
    }
    // <? super 하위Object> : 와일드카드의 범위를 특정 객체의 상위 클래스로 지정
    public List<? super Integer> addList(List<? super Integer> list){
        for(int i = 1; i<5;i++){
            list.add(i);
        }
        return list;
    }
    public static void main(String[] args) {
        People<String,Integer> p1 = new People<String,Integer>("Jin", 29);
        People<String,Integer> p2 = new People<String,Integer>("cha", 27);

        boolean result  = p1.compare(p1, p2);
        System.out.println(result);
    }
}
