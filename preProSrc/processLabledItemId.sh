#!/bin/zsh
#FileName: processLabledItemId.sh
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

nu=0
while read Line
do
    k=`echo "$Line"|tr -s ' ' '\n'|sort -nu|tr -s '\n' ' '`
    printf "%s\n" $k>>nopeatItemCatId
    let nu=$nu+1;
    echo "$nu"
done<labledItemCatId
