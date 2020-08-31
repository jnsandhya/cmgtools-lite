# 
# This is little script to get number of jobs succeeded
#

rm status/*

cmd=$(find $PWD/ -type d -iname \*$1\*)

echo ""
echo "Start to launch crab status :)"
echo ""

for dir in $cmd
do
    len_name=$(expr length $PWD)
    # +6 need to have only the sample name 
    name=${dir:len_name+6}
    crab status $dir/*/ > "status/"$name".txt"
    echo "Sample done !"
done

echo ""
echo "All samples are finished got to extract succeeded jobs"
echo ""

rm status/status.txt

for file in "status/"*
do
    echo $file >> "status/status.txt"
    while read 
    do
        if [[ "$REPLY" == "Jobs status:"*"failed"* ]]
        then 
            echo -e "$REPLY" >> "status/status.txt"
        elif [[ "$REPLY" == *"finished"* ]]
        then 
            echo -e "$REPLY" >> "status/status.txt"
        fi
    done < $file
done

echo ""
echo "Finish !! ;)"
echo ""

cat status/status.txt


