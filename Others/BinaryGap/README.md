BinaryGap
===
## 개요
BinaryGap은 이진법으로 표현된 양의 정수에서 1사이의 연속된 0의 개수 입니다.
양의 정수 N이 주어지면 가장 긴 이진가격의 길이를 구하세요.
## 규칙
+ N은 [1 ... 2,147,483,637] 범위의 정수 입니다.
+ BinaryGap은 이진표현된 양의 정수에서 시작과 끝이 1이고 사이에 0이 존재할 경우 0의 개수를 나타냅니다.
## Solution
+ 양의 정수 N이 주어졌을때 BinaryGap이 존재할 경우 가장 긴 BinaryGap의 길이를, 존재하지 않는다면 0읠 return 하는 Solution을 작성하세요