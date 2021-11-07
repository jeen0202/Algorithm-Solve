Hash Table
-----
### 개요
+ Key-Value 쌍으로 데이터를 저장하는 자료구조
+ Python의 Dictionary 변수가 HashTable로 구현되어 있다.
+ Key를 사용해 검색하기 때문에 순차적 검색보다 검색속도가 빠르다.
+ Key에 대한 Data의 중복 확인이 쉽다.
+ 여러 Key에 해당하는 주소가 동일할 경우 이를 해결하기위한 Chaning이 필요하다.
### HashTable 구조
1. Hash Function
    : 임의의 길이를 가지는 임의의 데이터를 고정된 데이터로 매핑하는 함수
2.  Hash값 
    : Hash Function을 통해 도출되는 고정된 길이의 data
3.  Slot 
    : 한개의 데이터를 저장할 수 있는 공간


