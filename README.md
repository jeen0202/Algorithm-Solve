# Algorithm-Solve

쾌적한 Problem Solve를 위한 환경설정(with WSL2)
-----
1. Template 자동 생성을 위한 Shell Script 작성
> 입력받은 폴더 생성후 동명의 (cc/py)파일 생성
+ C++ 
``` shell
#!/bin/bash
    mkdir $1 # 
    echo "#include <cstdio>

    int main () {
        
    }
    " > $1/$1.cc
```
+ Python
``` shell
    #!/bin/bash
    mkdir $1
    echo "import sys
    input = sys.stdin.readline
    def solution():
            

    if __name__ == "__main__":
        solution()
    " > $1/$1.py
```
2. vs code에서의 debuggin을 위한 task 생성
``` json
{
    "label": "python",
    "type": "shell",
    "command" : "python3",
    "args": [
        "${file}",
        "<",
        "${fileDirname}/input.txt"
    ],
    "group": "build",
    "problemMatcher":[]
},
{
    "label": "C/C++ build and run active file",
    "type" : "shell",
    "command": "/usr/bin/g++",
    "args" :[
        "-g",
        "${file}",
        "-o",
        "${fileBasenameNoExtension};",
        "./${fileBasenameNoExtension}",
        "<",
        "${fileDirname}/input.txt;",
        "/bin/rm",
        "${fileBasenameNoExtension}"
    ],
    "problemMatcher":[
        "$gcc"
    ],
    "group": "build"
}
```