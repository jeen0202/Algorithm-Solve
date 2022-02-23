import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Inheritance {
    public class School{
        public String school_name = "Suksan";
        public String school_class = "High school";
        private String[][] class_student_name ={
            {"Suksan1","Suksan2"},
            {"Suksan3","Suksan4"},
            {"Suksan5","Suksan6"}
        };
        private String[] class_teacher_name ={
            "Sejing Kim",
            "Juwon Cha",
            "Mir Lee"
        };        
        public School(){
            System.out.printf("%s %s",school_name, school_class);
        }
        public String getClass(String name){
            for(int i =0;i<class_student_name.length;i++){
                for(int j=0;j<class_student_name[i].length;j++){
                    if(class_student_name[i][j].equals(name)){
                        return (i+1)+"";
                    }
                }
            }
            return null;
        }
    
        public String [] getTeacherName(String student_name){
            for(int i =0;i<class_student_name.length;i++){
                for(int j = 0;j<class_student_name[i].length;j++){
                    if(class_student_name[i][j].equals(student_name)){
                        return class_teacher_name;
                    }
                }
            }
            return null;
        }
        
        public String[] getFriends(String student_name){
            for(int i =0;i<class_student_name.length;i++){
                for(int j =0;j<class_student_name[i].length;j++){
                    if(class_student_name[i][j].equals(student_name)){
                        return class_student_name[i];
                    }
                }
            }
            return null;
        }
    }
    
    public class Teacher extends School{
        public Teacher(){
            System.out.println("반 확인 프로그램");
        }
        @Override
        public String getClass(String name){
            return super.getClass(name)+"반";
        }
    }
    public class Student extends Teacher{
    private String name;        
    public Student(){
            super(); //부모 class 인자 호출
            start();
        }
        private void start(){
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("이름을 입력하세요 >> ");
            try{
                name = in.readLine();
                if(super.getClass(name) == null){
                    System.out.println("우리학교 소속이 아닙니다!");
                    return;
                }
                System.out.println("담임교사 : "+super.getTeacherName(name));
    
                System.out.println("소속 반 : "+super.getClass(name));
    
                String[] friends = super.getFriends(name);
                System.out.println("같은반 학우들 : { ");
                for(int i = 0; i<friends.length;i++){
                    System.out.printf("%s ",friends[i]);
                }
                System.out.println(" }");
            }catch(Exception e){
                System.err.println("err!");
            }
        }
    }
    
    public static void main(String[] args) {
        //new Student();
    }
}
