후보키
-----
### 개요
주어진 관계형데이터베이스를 분석하여 후보키의 최대개수를 구하세요
### 규칙
+ 후보키는 유일성, 최소성을 모두 만족해야합니다.
+ RDB의 Column 길이는 1이상 8이하입니다.
+ RDB의 row 길이는 1이상 20이하입니다.
+ RDB의 모든 요소의 길이는 1이상 8이하이여, 알파벳 소문자/숫자로만 이루어져있습니다.
+ RDB의 모든 튜플은 서로 중복되지 않습니다. 
### 매개변수 및 솔루션
+ 관계형데이터베이스 Relation이 2차원 문자열배열로 주어집니다.
+ 주어진 relation의 후보키 개수의 최대치를 구하는 solution 작성
