class ThreadEX implements Runnable{
    int TestNum =0;
    @Override
    public void run(){ // Syncronized 하게 실행된다.
        for(int i =0;i<5;i++){
            if(Thread.currentThread().getName().equals("A")){
                System.out.println("=============");
                TestNum++;
            }
            System.out.println("ThreadName : "+Thread.currentThread().getName()+" TestNum : " +TestNum);

            try{
                Thread.sleep(500);
            }catch ( Exception e){
                e.printStackTrace();
            }
        }
    }
}
public class Thread03 {
    public static void main(String[] args) {
        ThreadEX threadex = new ThreadEX();
        ThreadEX threadex2 = new ThreadEX();
        Thread thread1 = new Thread(threadex,"A");
        Thread thread2 = new Thread(threadex2,"B");

        thread1.start();
        thread2.start();

        Thread.currentThread().getName();

    }
}
