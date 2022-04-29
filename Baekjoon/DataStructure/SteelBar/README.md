쇠막대기(10779)
===
## 개요
+ 주어진 규칙에 따라 여러개의 쇠막대기를 절단할때 잘려진 조각의 총 개수를 출력하세요.
## 규칙
+ 쇠막대기와 레이저는 다음과 같은 조건을 만족하여 배치됩니다.
    + 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있습니다.
    + 다른 쇠막대기 위에 놓인 쇠막대기는 끝점이 겹치지 않고 완전하게 포함되어야합니다.
    + 각 쇠막대기를 자르는 레이저는 적어도 하나 이상 존재합니다.
    + 레이저는 어떤 쇠막대기의 양 끝점과도 겹ㅊ치지 않습니다.
+ 레이저는 `()`으로 표현되고 쇠막대기의 왼쪽끝은 `(`, 오른쪽 끝은 `)`로 표현됩니다.
+ 모든 `()`는 반드시 레이저를 포함합니다.
+ 괄호 표현은 공백없이 주어지며 길이는 최대 100,000입니다.
## 입력 및 출력
+ 한줄에 괄호표현이 공백없이 주어집니다.
+ 잘려진 조각의 총 개수를 나타내는 정수를 출력하세요.