class ATM implements Runnable{
    private long depositeMoney;

    public void setDepositMoney(long money){
    this.depositeMoney=money;
    }
    public void run(){
        synchronized(this){
            for (int i = 0;i<10;i++){
                notify();
                try{
                    wait();
                    Thread.sleep(1000);
                }catch(Exception e){
                    e.printStackTrace();
                }
                if (getDepositeMoney()<=0) return;
                withDraw(1000);
            }
        }
    }
    public void withDraw(long howMuch){
        if (getDepositeMoney() >0){
            depositeMoney -= howMuch;
            System.out.print(Thread.currentThread().getName() + " , ");
            System.out.printf("잔액 : %,d 원 %n", getDepositeMoney());
        } else{
            System.out.print(Thread.currentThread().getName() + " , ");
            System.out.println("잔액이 부족합니다.");
        }
    }

    public long getDepositeMoney(){
        return depositeMoney;
    }
}

public class Thread04 {
    public static void main(String[] args) {
        ATM atm = new ATM();
        atm.setDepositMoney(10000);
        Thread father = new Thread(atm,"Father");
        Thread son = new Thread(atm,"son");
        father.start();
        son.start();
    }
}
