링크와 스타트
===
## 개요
+ N명의 사람들의 시너지를 고려해 두팀으로 나누었을때 각 팀의 능력치 총합의 차이의 최소값을 구하세요.
## 규칙
+ 각 인원은 1부터 N까지 번호가 매겨져 있습니다.
+ 능력치 $S_i$$_j$ 는 i번째 사람과 j번째 사람이 같은 팀에 속해있을때 팀에 더해지는 능력치 입니다.
+ S$_i$$_j$와 S$_j$$_i$는 다를수도 있으며, 한팀에 i와 j가 속해있을경우 더해지는 능력치는 S$_i$$_j$와 S$_j$$_i$입니다.
+ 인원의 수 N은 $4\le N \le20$을 만족하며 능력치 S는 $1\le S \le 100$입니다.
+ S$_i$$_i$는 항상 0입니다.
## 입력 및 출력
+ 첫째줄에 N이 주어지고 다음 N개의 줄에 S가 N개 주어집니다.
+ 두팀의 능력치 차이의 최솟값을 구하세요.