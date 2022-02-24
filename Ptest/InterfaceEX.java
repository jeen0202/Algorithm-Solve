//추상 메서드만 존재하는 인터페이스
interface WashingMachine{
    public void startButtonPressed();
    public void pauseButtonPressed();
    public void stopButtonPressed();
    public int changeSpeed(int speed);
}

interface dryCouse{
    public void dry();
}
//인터페이스를 활용한 다중 상속
class LGWashingMachine implements WashingMachine,dryCouse{
    @Override
    public void startButtonPressed(){
        System.out.println("빨래를 시작했습니다.");
    }
    @Override
    public void pauseButtonPressed(){
        System.out.println("빨래를 일시정지했습니다.");
    }
    @Override
    public void stopButtonPressed(){
        System.out.println("빨래를 중지했습니다.");
    }
    @Override
    public int changeSpeed(int speed){
        int rtnSpeed = 0;
        switch(speed){
            case 1:
                rtnSpeed = 20;
                break;
            case 2:
                rtnSpeed = 50;
                break;
            case 3:
                rtnSpeed = 100;
                break;
        }
        return rtnSpeed;
    }
    @Override
    public void dry(){
        System.out.println("세탁이 완료되어 건조를 시작합니다.");
    }
}
public class InterfaceEX {

    public static void main(String[] args) {
        LGWashingMachine washingMachine = new LGWashingMachine();
        washingMachine.startButtonPressed();;
        System.out.printf("세탁기의 속도는 %d 입니다.\n",washingMachine.changeSpeed(3));
        washingMachine.dry();
    }
}
