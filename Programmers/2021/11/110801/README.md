프린터
-----
### 개요
요청을 순차적으로 처리하는 인쇄기를 보완하여 중요도가 높은 문서를 먼저 인쇄하는 프린터 만들기
### 규칙
1. 대기목록의 가장 앞의 문서(J)를 꺼냅니다.
2. 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
+ 대기목록에는 1개이상 100개 이하의 문서가 있습니다.
+ 중요도는 1~9로 표현되며 클수록 중요합니다.
+ 대기목록 가장 앞에있으면 location은 0이고 끝에있으면 (대기목록의 작업수 -1) 입니다.
### 매개변수 및 솔루션
+ 현재 대기목록에 있는 문서의 중요도가 순서대로담긴 배열 Priorities, 인쇄를 요청한 문서가 대기열 목록의 어느 위치에 있는지를 알려주는 location이 매개변수로 주어집ㄴ디ㅏ.
+ 인쇄를 요청한 문서가 몇 번쨰로 인쇄되는지 return하는 solution 작성
