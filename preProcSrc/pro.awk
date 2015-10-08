#!/bin/awk -f
#FileName: pro.awk
#Author:   Fuchen Duan
#Email:    slow295185031@gmail.com

{
    cmd="grep \'\\b"$1"\\b\' ../originalData/test_items.txt > /dev/null"
    if(system(cmd) == 0)
    {
        print $0
    }
}
