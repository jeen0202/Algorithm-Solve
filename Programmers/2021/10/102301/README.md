오픈채팅 관리자페이지
-----
### 개요
+ 채팅방에 누군가 들어오면 다음 메시지가 출력된다.
    + "[닉네임]님이 들어왔습니다."
+ 채팅방에서 누군가 나가면 다음 메시지가 출력된다.
    + "[닉네임]님이 나갔습니다."
+ 채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.
    + 채팅방을 나간 후, 새로운 닉네임으로 재접속
    + 채팅방에서 닉네임을 변경
+ 중복 닉네임을 허용
### 규칙
+ 매개변수 record 는 문자열이 담긴 배열이며, 길이는 1이상 100000 이하 [유저 아이디]로 구분
    + Enter [유저 아이디] [닉네임]
    + Leave [유저 아이디]
    + Change [유저 아이디] [닉네임]
+ 각 단어는 공백으로 구분되어있으며, 알파벳 대문자, 소문자, 숫자로만 구성
+ 유저 아이디와 닉네임의 길이는 1 이상 10 이하
+ 잘못된 입력은 주어지지 않음

### 매개변수 및 솔루션
+ 매개변수 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record가 주어집니다.
+ 모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 해주세요.