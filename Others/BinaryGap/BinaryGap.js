function solution(N){
    let cnt = 0
    let max = 0
    let flag = false
    let biN = N.toString(2).split("")
    biN.forEach(e => {
        if(e==='1' && flag === false){
            flag =true
        }else if(e==='1' && flag === true){
            max = Math.max(cnt,max)
            cnt = 0
        }else cnt +=1
    });
    return max
}
console.log(solution(1041))
console.log(solution(32))