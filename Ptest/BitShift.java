
public class BitShift {
    public static void main(String[] args) {
        System.out.printf("2 << 3 = %d\n",(2<<3)); //세자리 왼쪽이동
        System.out.printf("16 >> 3 = %d\n",(16>>3));// 세자리 오른쪽 이동
        System.out.printf("-16 >> 3 = %d\n",(-16>>3)); // 세자리 오른쪽 이동
        System.out.printf("-16 >>> 3 = %d\n",(-16>>>3)); // 세자리 오른쪽이동+ 부호비트에 관계없이 0으로 밀어낸다.
        System.out.println("=================");
        //논리 연산자
        System.out.printf("15 & 25 = %d\n",(15&25)); // 2진수로 분리하여 자리수별로 AND 연산 실행
        System.out.printf("15 | 25 = %d\n",(15|25)); // 2진수로 분리하여 자리수별로 OR 연산 실행
        System.out.printf("15 ^ 25 = %d\n",(15^25)); // 2진수로 분리하려 자리수별로 XOR 연산 실행
        System.out.printf("~25 = %d\n", ~25); // 2진수로 분리하여 보수(각 자리가 반전된 수)를 호출
    }
}
