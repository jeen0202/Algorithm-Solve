More Spicy
-----
### 개요
+ 주어진 배열과 식을 통해 스코빌 지수를 K 이상으로 만들기 위한 방법
+ ```섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)```
### 규칙
+ scoville의 길이는 2 이상 1,000,000 이하입니다.
+ K는 0 이상 1,000,000,000 이하입니다.
+ scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
+ 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
### 매개변수 및 솔루션
+ 음식의 스코빌 지수를 담은 배열 Scovile, 원하는 스코빌지수 K가 매개변수로 주어집니다.
+ 모든 음식의 스코빌 지수를 K이상으로 만들기 위해 섞어야하는 최소 횟수를 return하는 Solution 작성.