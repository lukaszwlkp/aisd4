#!/bin/bash
blue=$(tput setaf 4)
gray=$(tput setaf 7)
green=$(tput setaf 2)
teal=$(tput setaf 6)
normal=$(tput sgr0)

for routine in "routines/"*; do
    for benchmark in "benchmark_non-hamilton/generate."*; do #Using file extensions to denote instance size, since extracting extension is trivial in Linux
        instance_size=${benchmark##*.}
        #Initial log - before program completion
        tmpLogFile=$(mktemp) #tmpfile to allow for pretty colors using printf
        cat > $tmpLogFile <<EOF
$normal============================[INSTANCE SIZE $instance_size]============================$green
Running the $routine benchmark for --non-hamilton. 
$normal============================[Input]============================$gray
$(cat $benchmark $routine <(echo exit))
$normal============================[Program Output]===================$teal 

EOF
            printf "$(more $tmpLogFile)" #printf allows for pretty colors
            tmpFile=$(mktemp) #saving to tmp file so it can be logged in follow up log
            run_project="python3 ../main.py --non-hamilton"
            #Please note that <(echo $instance_size) is unnecesarry for routines kahn_sort and tarjan_sort, but the program should ignore invalid `actions`.
            result=$(/usr/bin/time -f "%S|%M" $run_project < <(cat $benchmark $routine <(echo exit)) 2>&1 >$tmpFile)
            mem=${result##*|}
            time=${result%|*}

            #Save to .csv
            echo "$(basename $routine),$instance_size,$time" >> $(basename $routine)_50nh_benchmark_time.csv
            echo "$(basename $routine),$instance_size,$mem" >> $(basename $routine)_50nh_benchmark_memory.csv
            
            #Follow up log - after program completion
            cat > $tmpLogFile <<EOF

$(cat $tmpFile)
$normal============================[usr/bin/time]=====================$green
time = $(echo $time) seconds | memory used = $(echo $mem) KBi
Saved to $(basename $routine)_50nh_benchmark_time.csv $(basename $routine)_50nh_benchmark_memory.csv

$normal
EOF
        printf "$(more $tmpLogFile)" #printf allows for pretty colors

    done
done
