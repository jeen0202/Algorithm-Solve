class testThread extends Thread{
    int seq;

    testThread(int seq){
        this.seq = seq;
    }
    public void run(){
        System.out.println(this.seq + " Thread start");
        try{
            Thread.sleep(1000);
        }catch(Exception e){

        }
        System.out.println(this.seq + " Thread end.");
    }
}
public class Thread01 {
    public static void main(String[] args) { // main 함수는 thread의 종료를 기다리지 않는다.
        for (int i = 0; i<10;i++){
        testThread thread = new testThread(i); // Thread는 동시 실행
        thread.start();
        }    
    System.out.println("main end.");
    }
}
