#!/bin/zsh
#FileName: match.sh
#Author: Yeoman

matchNo=0
sumNo=0
for i in `cat test_items.txt`
do
    grep "\b$i\b" user_bought_1_day
    if test $? -eq 0 ;then
        let matchNo=matchNo+1
    else
        let sumNo=sumNo+1
    fi
done
echo "Matched no :$matchNo, Not Matched No: $sumNo"
