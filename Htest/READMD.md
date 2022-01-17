1. ## 모노레일 최대 수송인원 산출

제한시간 : C/C++/Java/Python(2초)| 메모리 제한 : 256MB



소프트웨어개발팀에서 근무 중인 당신은 이번에 미국 실리콘밸리로 출장을 가게 되었다. 비행기를 타기 위해 인천공항에 도착해서 수속을 마친 당신은 모노레일을 타고 수속장에서 비행기 탑승동으로 이동해야 했다. 공항에는 승객을 수송하기 위한 N개의 모노레일 라인이 설치되어 있다.

모노레일을 이용하기 위한 승강장은 N+1개 있어서, i번째 라인은 i번째 승강장과 i+1번째 승강장의 승객을 태울 수 있다. 현재 i번째 승강장에는 Pi명의 승객이 있고, i번째 라인의 열차는 한 번에 Ci명의 승객을 태울 수 있다. 평소 호기심 많은 개발자였던 당신은 한번에 몇명이나 모노레일로 이동할 수 있는지 궁금했고 이를 알아보고자 간단하게 프로그래밍을 해보기로 했다. 각 라인의 열차를 한 번씩만 운행하여 수송할 수 있는 승객의 최대 명수를 구해보자.

예를 들어 N=2 (모노레일 2개)인 경우를 도식화해보면 다음과 같다.

![img](https://www.softeer.ai/upload/2021/08/20210805_143253983_81356.png)

승강장은 N+1이므로 총 3개이며, 각 승강장에는 P1=2명, P2=4명, P3=1명의 승객이 있다고 가정해 보자. 각 모노레일의 탑승 정원이 C1=3명, C2=2명 이라고 할때, 한번에 최대 수송가능한 인원은 5명임을 알 수 있다.



입력형식

첫 번째 줄에 정수 N이 주어진다.
두 번째 줄에 N+1개의 정수 P1,P2,...,PN+1이 주어진다.
세 번째 줄에 N개의 정수 C1,C2,...,CN이 주어진다.
입력은 다음과 같은 조건을 만족한다.
  1≤N≤105
  1≤Pi≤109
  1≤Ci≤109



출력형식

첫 번째 줄에 각 라인의 열차를 한번씩만 운행하여 수송할 수 있는 최대 승객수를 출력하라.



입력예제1

2
2 4 1
3 2

출력예제1

5

2
10 2 1
1 9

출력예제2

4

입력예제3

2
5 1 5
1 10

출력예제3

7





2. ## H-모빌리티클래스

제한시간 : C/C++(1초), Java/Python(2초) | 메모리 제한 : 256MB



현대자동차그룹의 기술경쟁력을 강화하기 위해 국내외 산업계 및 학계와의 협력을 확대하고, 인재 육성체계를 수립해 연구개발 인력 역량 향상에 기여하고 있다. 그 중 4차 산업혁명에 대비하여 H-모빌리티클래스로 미래기술 관련 교육을 실시하고 있다.

![img](https://softeer.ai/upload/2022/01/20220107_132144358_70794.jpeg)

H-모빌리티클래스는 기초 과정과 심화 과정으로 구분이 되어있다. 기초 과정에서 우수한 성적을 거둔 교육생들 대상으로 심화 과정이 이뤄진다.

여기 기초 과정에 참여한 수강생을 1부터 N까지 정수로 표현하자. 기본 교육 이해도 평가를 한 뒤, 모든 수강생은 본인의 등수를 알고 싶어한다. 그러나 운영자는 수강생에게 개별적으로 등수를 알려주지는 않고, 두 사람 A, B에 대해서 “A가 B보다 시험을 잘 보았나요?”라는 질문에만 답을 해준다. 총 N(N-1)/2번 서로 다른 질문을 했고 그 답을 받았다. 이 결과로부터, 전체 N명의 등수를 알아내서 정렬한 결과를 출력하는 프로그램을 작성하라.



입력형식

시험을 본 사람 수 N 이 첫 줄에 주어진다.(2 ≤ N ≤ 1,000)

다음 N(N-1)/2개의 줄에 빈칸으로 구분된 X Y S가 한 줄에 주어진다.(1 ≤ X < Y ≤ N)

이는, 수강생 X가 수강생 Y보다 평가를 잘 보았는지 물어보는 것으로, X의 점수가 Y보다 높다면 S가 1, Y의 점수가 X보다 높다면 S가 0으로 주어진다. 단, 동점인 사람은 없다고 가정한다.



출력형식

1부터 N까지 정수의 순열을 숫자 사이에 공백을 하나 두고 출력하는데, 이는 평가 점수가 높은 사람부터 차례로 등수에 따라 사람들을 출력한다.

입력예제1

4
1 2 1
2 3 0
3 4 1
1 3 1
2 4 1
1 4 1

출력예제1

1 3 2 4

입력예제2

3
3 1 0
2 1 0
2 3 1

1 2 3





3. ## 드론 삼각 편대

제한시간 : C/C++(1초), Java/Python(2초) | 메모리 제한 : 256MB



드론들 사이의 통신 연결은 정점과 간선을 가진 단순 그래프(간선의 방향이 없으며, 동일한 쌍의 정점을 연결하는 간선이 최대 1개인 그래프)로 생각할 수 있다. 드론은 정점을 나타내고 간선은 두 드론이 직접 통신이 가능함을 나타낸다. 드론이 원활한 편대비행을 하기 위해서는 편대를 구성하는 드론끼리 모두 직접 통신이 가능해야 한다.

당신은 3개의 드론으로 구성된 편대를 고려하고 있다. 구체적으로, 이 그래프의 3개의 서로 다른 정점 a, b, c에 대해 a와 b를 잇는 간선, b와 c를 잇는 간선, c와 a를 잇는 간선이 모두 존재할 때, {a, b, c}를 삼각형이라고 부르고, 삼각형을 구성하는 드론들은 편대 구성이 가능하다.

주어진 그래프에 2개 이상의 삼각형이 있는지 판단하는 프로그램을 작성하라.



입력형식

입력으로는 자연수 N, M이 첫 줄에 주어진다.
N은 정점의 수, M은 간선의 수이다. N은 1 이상 3,000이하이고, M은 0이상 10,000이하이다.
정점은 1부터 N까지 번호가 붙어 있다. 다음 M개의 줄 각각에 서로 다른 정점의 번호 두 개가 주어진다. 주어진 두 정점이 간선으로 이어져 있다는 뜻이다.



출력형식

2개 이상의 서로 다른 삼각형이 있는 경우 YES를, 아닌 경우 NO를 출력한다.
서로 다른 삼각형이 정점의 일부를 공유하는 것도 가능한 것으로 본다.

입력예제1

3 3
1 2
1 3
3 2

출력예제1

NO

입력예제2

4 6
1 2
2 3
3 4
4 2
1 3
4 1

출력예제2

YES


