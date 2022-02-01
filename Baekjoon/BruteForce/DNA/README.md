DNA
===
## 개요
+ 4개의 뉴클레오티드로 이루어져는 DNA간 Hamming Distance의 합이 가장 작은 DNA를 찾으세요.
## 규칙
+ DNA는 `T``A``G``C` 4자기 문자로 표시됩니다.
+ Hamming Distance는 크기가 같은 두 DNA에서 각 위치의 문자가 다른것은 개수입니다.
+ DNA의 수 N과 문자열의 길이 M은 다음과 같은 규칙을 따릅니다.
    - $1 \LE N \LE 1,000$
    - $1 \LE M \LE 50$
+ Hamming Distance의 합이 가장 작은 DNA가 여러개일 경우, 사전순으로 가장 앞서는 DNA를 선택하세요.
## 입력 및 출력
+ 첫째 줄에 N 과 M이 주어집니다.
+ 둘쨰 줄 부터 N+1번 째 줄까지 N개의 DNA가 주어집니다.
+ 첫째줄에 Hamming Distance의 합이 가장 작은 DNA를 출력하세요.
+ 둘째줄에는 그 DNA의 Hamming Distance의 합을 출력하세요.
