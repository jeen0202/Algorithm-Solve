class SingleThread implements Runnable{ // Runnable Interface 상속 : 다중상속 가능
    private int[] temp;
    SingleThread(){
        temp = new int[10];
        for (int start = 0;start<temp.length;start++){
            temp[start]=start;
        }
    }
    @Override
    public void run(){
        for(int start:temp){
            try{
                Thread.sleep(1000);
            }catch(Exception e){
                e.printStackTrace();
            }

            System.out.println("Thread : " + Thread.currentThread().getName());
            System.out.println("temp value : "+start) ;
        }
    }
}

public class Thread02 {        
    public static void main(String[] args) {
        SingleThread ct = new SingleThread();
        Thread t = new Thread(ct,"첫번째");
        //Thread t2 = new Thread(ct,"두번째");

        t.start();
        //t2.start();
    }
}
