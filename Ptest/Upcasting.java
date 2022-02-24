class Person{
    String name;

    public Person(String name){
        this.name = name;
    }
}

class Student extends Person{
    String dept;

    public Student(String name){
        super(name); // 부모 클래스의 생성자 호출
    }
}
public class Upcasting {
    public static void main(String[] args) {
        Student student = new Student("Sejing");
        //Student 객체를 Person 객체로 Upcasting : 명시적 지정 불필요
        Person person = student;
        person.name = "Juwon";
        // Upcasting되었으므로 부모의 멤버만 사용가능.
        // person.dept = "Economics";
        // Person 객체를 Student 객체로 다운 캐스팅 : 명시적 지정필요
        Student dstudent = (Student)person;
        dstudent.name = "Sejing";
        dstudent.dept = "Development";

    }
}
