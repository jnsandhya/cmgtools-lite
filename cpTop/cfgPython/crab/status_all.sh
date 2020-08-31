
cmd=$(find /gridgroup/cms/letroadec/CMSSW_9_4_11_cand1/src/CMGTools/cpTop/cfgPython/crab -type d -iname \*$1\*)

for dir in $cmd
do
    echo $dir"/*/"
    crab status $dir/*/
done
