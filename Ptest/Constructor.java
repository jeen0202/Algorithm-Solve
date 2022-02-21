class Student{
    public int id;
    public String name;
    public String address;
    // 생성자 : 클래스를 통해 객체를 생성하고, 객체의 필드를 초기화 하기위한 반환값이 없는 Method
    // 기본 생성자 : 클래스의 생성자는 반드시 1개이상 존재해야한다.
    // 따라서 사용자가 명시적으로 생성자를 1개도 선언하지 않으면 컴파일러가 자동으로 구현부가 존재하지 않는 빈 생성자를 생성해준다.

    public Student(int id, String name){
        this.id = id;
        this.name = name;
    }
    // 생성자 오버로딩
    // 생성자의 이름은 클래스명과 동일하게 고정되지만 서로다른 매개변수로 구분되어 서로 다른 동작을 하는 여러개의 생성자를 만들 수 있다.
    public Student(int id, String name, String address){
        this.id = id;
        this.name = name;
        this.address = address;
    }
}
public class Constructor {
    public static void main(String[] args) {
        // Student 클래스 생성자 오버로딩
        Student student1 = new Student(001,"Sejing");
        Student student2 = new Student(002,"SSR","Naju");
    }
}
