주유소
===
## 개요
N개의 도시가 일직선 도로위에 놓여있고, 제일 왼쪽끝 도시에서 오른쪽 끝 도시로 이동하려고할때, 각 도시의 주유소 가격이 다를때 이동비용의 최소값을 구하세요.
## 규칙
+ 처음 출발할때 자동차에는 기름이 없어 주유소에서 기름을 넣고 출발해야합니다.
+ 기름통의 크기는 무제한이라 얼마든지 많은 기름을 넣을 수 있습니다.
+ 각도시에는 한개의 주유소가 존재하고 각 주유소의 기름값은 다를 수 있습니다.
+ 도시의 개수 N은 $2 \le N \le 100,000$을 만족합니다.
+ 도시를 연결하는 도로의 개수는 N-1개의 이고, 전체 경로와 기름의 리터당 가격은 1이상 1,000,000,000 이하의 자연수 입니다.
## 입력 및 출력
+ 첫번째 줄에는 도시의 개수 N이 주어집니다.
+ 두번쨰 줄에는 인접한 두 도시를 연결하는 도로의 길이가 N-1개 주어집니다.
+ 마지막줄에는 각 도시의 주유소의 리터당 가격이 N개 주어집니다.
+ 왼쪽끝 도시에서 오른쪽 끝 도시로 이동하는 최소비용을 출력하세요.