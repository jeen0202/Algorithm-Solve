#!/bin/zsh
mkdir $1/$2
echo "import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.StringTokennizer;

public class $2{
    public static void main(String[] agrs) throws IOException{
        System.setIn(new FileInputStream(\"Baekjoon/$1/$2/input.txt\"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st = new StringTokenizer(br.readLine()," ");
    }
}
" > $1/$2/$2.java

echo "제목
===
## 개요
## 규칙
## 입력 및 출력" > $1/$2/README.md

echo > $1/$2/input.txt