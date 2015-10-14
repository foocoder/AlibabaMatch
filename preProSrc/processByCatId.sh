#!/bin/sh
#FileName: processByCatId.sh
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

nu=0
while read Line
do
    copyLine=$Line
    first=`echo "$Line"|awk '{print $1}'`
    k=`echo "$Line"|awk '{for(i=2;i<=NF;i++){printf("%d ",$i)};printf("\n")}'|tr -cs 0-9 '\n'|sort -nu|tr -s '\n' ' '`
    #echo $k
    for i in $k
    do
        if test $first = $i;then
            continue;
        elif test $first -gt $i;then
            startPoint=$i;
            endPoint=$first;
        else
            startPoint=$first;
            endPoint=$i;
        fi
        grep "\b$first\b" category/nopeatItemCatId | grep "\b$i\b" > /dev/null
        #grep "\b$startPoint\b.*\b$endPoint\b" category/nopeatItemCatId > /dev/null
        if test $? -eq 1;then
            for j in $Line
            do
                if test $j = $i;then
                    copyLine=`echo $copyLine|sed "s/\b$i\b/0/g"`
                fi
            done
        fi
    done
    echo $copyLine|sed "s/\b[1-9][0-9]*\b/1/g">>fm_isExist
    let nu=nu+1;
    echo $nu
    #if test $nu -eq 15;then
    #    break;
    #fi
done<fm_submissionsCatId
