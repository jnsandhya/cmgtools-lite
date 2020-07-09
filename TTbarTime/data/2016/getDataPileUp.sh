pileupCalc.py -i Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 65809.2 --maxPileupBin 200 --numPileupBins 200 MyDataPileupHistogram_down.root
pileupCalc.py -i Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 72590.8 --maxPileupBin 200 --numPileupBins 200 MyDataPileupHistogram_up.root
#pileupCalc.py -i Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt --inputLumiJSON pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 200 --numPileupBins 200 MyDataPileupHistogram.root


### taking 1.049 as pu unc. up and (1-0.049) as down