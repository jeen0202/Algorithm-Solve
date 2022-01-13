let input = require("fs").readFileSync('./input02.txt').toString().split("\n")
let count = input[0].split(' ')
let numbers = []
const d =[[-1,0],[1,0],[0,1],[0,-1]] //좌우상하 좌표이동
const dd = [[-1,0],[1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]] // 좌우상하 대각이동
function DFS(graph){
    //let visited=Array.from(Array(graph.length),() => new Array(graph[0].length).fill(false))
    start=[0,0]
    visited = []
    //console.log(visited)
    let queue = []
    queue.push(start)
    while(queue.length >0){
        const node = queue.shift()
        dd.forEach((item)=>{
            const now = [node[0]+item[0],node[1]+item[1]]
            console.log(now)
            if(now[0]>=0 && now[1]>=0&& now[0] < graph.length && now[1] < graph[0].length&&graph[now[0]][now[1]] === 1 && !visited.includes(now)){
                visited.push(now)
                queue.push(now)
            }
        })
    }
    console.log(visited)
}


function solution(numbers){
    if(numbers.length ===1 && numbers[0].length ===1){
        console.log(numbers[0][0])        
    }else{
        DFS(numbers)
        //console.log(numbers) 
    }
}


for (let i=1; i< input.length-1;i++){
    let line = input[i].split(" ").map(Number);
    if(count === undefined){
        count = line
    }else{
        numbers.push(line)     
    }
    if(numbers.length === parseInt(count[1])){
        solution(numbers)
        numbers= []
        count = undefined
    }
}