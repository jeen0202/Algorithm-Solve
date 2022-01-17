GenomicRangeQuery
===
## 개요
DNA 서열의 특정 부분에 포함된 최소 뉴클레오티드 인자를 찾으세요
## 규칙
+ DNA시퀀스는 N개의 비어 있지 않은 문자열S로 제공되며, 문자열 S의 요소는 A,C,G,T만으로 이루어져있습니다.
+ A,C,G,T의 순서로 1,2,3,4의 영향 계수를 가집니다.
+ M쿼리는 각각 배열 P,Q의 K번째 요소를 사용하여 S의 부분 배열을 생성합니다.
+ N은 [1 ... 100,000] 범위내의 정수 입니다.
+ M은 [1 .. 50,000] 범위내의 정수 입니다.
+ P[K] <= Q[K],이고 0 <= K< M 입니다.
## Solution
+ M쿼리를 통해 생성된 부분 배열 내부의 최소 영향계수의 배열을 반환하세요.