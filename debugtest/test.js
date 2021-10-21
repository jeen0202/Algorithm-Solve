let fs = require('fs');
let stdin = fs.readFileSync('input.txt').soString().split(' ');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})

