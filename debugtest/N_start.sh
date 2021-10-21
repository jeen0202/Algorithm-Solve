#!/bin/bash
mkdir $1
echo "
let fs = require('fs');
let stdin = fs.readFileSync('input.txt').soString().split(' ');

const input = (() => {
    let line = 0;
    return () => stdin[line++];
})
" > $1/$1.js