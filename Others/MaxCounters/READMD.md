MaxCounters
===
## 개요
모든 요소가 0으로 초기화된 배열 counter의 요소 개수 N과 counter의 요소를 가르키는 배열 A가 주어졌을때, 주어진 규칙에 따라 계산된 최종 counter를 반환하세요.
## 규칙
+ A배열의 각 요소는 아래의 법칙에 따라 counter를 변형시킵니다.
    - 요소가 배열의 Maxcounter(N+1)일 경우 counter의 모든 요소에 1을 더합니다.
    - 요소가 Maxcounter가 아닐경우, counter[요소+1]에 1을 더합니다.
+ counter의 길이 N은 1이상 100,000이하입니다.
+ A배열의 각 요소는 1이하 N+1의 범위에서 존재합니다.
## Solution
규칙에 따라 A배열의 계산을 모두 마친 후 counter를 list형식으로 반환하는 Solution을 작성하세요.