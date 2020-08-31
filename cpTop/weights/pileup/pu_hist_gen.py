import sys,os
from ROOT import TFile, TH1D, TTree

dir_input  = "./MC_pileup_all/"
dir_output = "./"

file_names = os.listdir(dir_input)
file_names.sort()
print file_names

name_list = [
    "#TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3#MINIAODSIM",
    "#DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2#MINIAODSIM",
    "#QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM",
    "#QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8#RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1#MINIAODSIM"
]

rootfile = TFile(dir_output+"pileup.root", "RECREATE")
pu_file = []
pu_tree = []
pu_hist = []

for i in range(len(file_names)):
    pu_file.append(TFile(dir_input+file_names[i]+"/tree.root"))
    pu_tree.append(pu_file[i].Get('events'))

rootfile = TFile(dir_output+"pileup.root", "RECREATE")
for i in range(len(file_names)):
    pu_hist.append(TH1D(name_list[i], "",200,0.,200.))
    pu_tree[i].Project(name_list[i], "pu")
    pu_hist[i].Write()



