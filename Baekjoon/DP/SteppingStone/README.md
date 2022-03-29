징검다리 건너기(21317)
===
## 개요
+ 행동과 소모에너지가 주어졌을 때 일렬로 나열되어있는 N개의 돌의 마지막 돌 틈의 산삼을 캐기 위한 소모 에너지의 최솟값을 구하세요.
## 규칙
+ 3종류의 점프를 할 수 있습니다.
    - 작은 점프 : 현재 위치에서 다음돌로 이동합니다.
    - 큰 점프 : 1개의 돌을 건너 뛰어 이동합니다.
    - 매우 큰 점프 : 2개의 돌을 건너뛰어 이동합니다. 전체 시도중 1번만 가능하며 k의 에너지를 소비합니다.
+ 작은 점프과 큰 점프시 소모되는 에너지는 점프를 하는 돌의 번호마다 다릅니다.
+ 첫번째 돌부터 시작합니다.
+ $1 \le N \le 20$을 만족합니다.
+ 각 점프시 필요한 에너지와 매우 큰 점프의 소모 에너지 K를 5,000을 넘지않는 자연수 입니다.
## 입력 및 출력
+ 첫번째 줄에 N이 주어집니다.
+ 두번 쨰 줄부터 N번째 줄까지 작은 점프, 큰점프를 하기위해 필요한 에너지가 주어집니다.
+ N+1번째 줄에 K가 주어집니다.
+ 산삼을 얻기 위한 최소 소모에너지를 출력하세요.