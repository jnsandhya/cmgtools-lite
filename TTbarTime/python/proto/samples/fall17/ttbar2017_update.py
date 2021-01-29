import os 
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

json = os.path.expandvars('$CMSSW_BASE/src/CMGTools/TTbarTime/data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt')
lumi = 41529.

############################################################################
# MC
############################################################################

signal_MC_dilep = creator.makeMCComponent("MC_signal_dilep","/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 89.05);

signal_MC_semilep = creator.makeMCComponent("MC_signal_semilep","/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 364.31);

signal_MC_hadronic = creator.makeMCComponent("MC_signal_hadronic","/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 380.11);

##############

background_MC_TTW = creator.makeMCComponent("MC_ttx_TTW","/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.2043);

background_MC_TTW2 = creator.makeMCComponent("MC_ttx_TTW2","/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",0.2043);

background_MC_TTW3 = creator.makeMCComponent("MC_ttx_TTW3","/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.4062);

background_MC_TTZ = creator.makeMCComponent("MC_ttx_TTZ","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.2529);

background_MC_TTZ2 = creator.makeMCComponent("MC_ttx_TTZ2","/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",0.2529);

background_MC_TTZ3 = creator.makeMCComponent("MC_ttx_TTZ3","/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.5297);

#background_MC_TTG = creator.makeMCComponent("MC_ttx_TTG","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",3.697);

#background_MC_TTG2 = creator.makeMCComponent("MC_ttx_TTG2","/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", "CMS", ".*root",3.697);

##############

background_MC_ST_s = creator.makeMCComponent("MC_singletop_ST_s","/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",10.32);

background_MC_ST_s2 = creator.makeMCComponent("MC_singletop_ST_s2","/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",10.32);

background_MC_ST_t_top = creator.makeMCComponent("MC_singletop_ST_t_top","/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root",136.02);

background_MC_ST_t_antitop = creator.makeMCComponent("MC_singletop_ST_t_antitop","/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root",80.95);

background_MC_tW_top = creator.makeMCComponent("MC_singletop_ST_tW_top","/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",35.5);

background_MC_tW_top2 = creator.makeMCComponent("MC_singletop_ST_tW_top2","/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",35.5);

background_MC_tW_antitop = creator.makeMCComponent("MC_singletop_ST_tW_antitop","/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",35.5);

background_MC_tW_antitop2 = creator.makeMCComponent("MC_singletop_ST_tW_antitop2","/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",35.5);

##############

background_MC_WW = creator.makeMCComponent("MC_dibosons_WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 118.7)
background_MC_WZ = creator.makeMCComponent("MC_dibosons_WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 47.13)
background_MC_ZZ = creator.makeMCComponent("MC_dibosons_ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 16.52)

##############

background_MC_WJets = creator.makeMCComponent("MC_wjets_WJets", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 0.4062)

background_MC_WJets2 = creator.makeMCComponent("MC_wjets_WJets2", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", "CMS", ".*root",0.4062)

##############

background_MC_DY = creator.makeMCComponent("MC_zjets_DY_50", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 6225.4)

background_MC_DY2 = creator.makeMCComponent("MC_zjets_DY_502", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM", "CMS", ".*root", 6225.4)

background_MC_DY3 = creator.makeMCComponent("MC_zjets_DY_1050", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM", "CMS", ".*root", 22635.1)


mc_ttbar = [
    signal_MC_dilep,
    signal_MC_semilep,
    signal_MC_hadronic,
    background_MC_TTW,
    background_MC_TTW2,
    background_MC_TTW3,
    background_MC_TTZ,
    background_MC_TTZ2,
    background_MC_TTZ3,
    #background_MC_TTG,
    #background_MC_TTG2,
    background_MC_ST_s,
    background_MC_ST_s2,
    background_MC_ST_t_top,
    background_MC_ST_t_antitop,
    background_MC_tW_top,
    background_MC_tW_top2,
    background_MC_tW_antitop,
    background_MC_tW_antitop2,
    background_MC_WW, 
    background_MC_WZ,
    background_MC_ZZ,
    background_MC_WJets,
    background_MC_WJets2,
    background_MC_DY,
    background_MC_DY2,
    background_MC_DY3
]

############################################################################
# DATA
############################################################################

# Run2017B 31Mar2018

SingleElectron_Run2017B_31Mar2018 = creator.makeDataComponent("SingleElectron_Run2017B_31Mar2018", "/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017B_31Mar2018 = creator.makeDataComponent("SingleMuon_Run2017B_31Mar2018", "/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

DoubleEG_Run2017B_31Mar2018 = creator.makeDataComponent("DoubleEG_Run2017B_31Mar2018", "/DoubleEG/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MuonEG_Run2017B_31Mar2018 = creator.makeDataComponent("MuonEG_Run2017B_31Mar2018", "/MuonEG/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuon_Run2017B_31Mar2018 = creator.makeDataComponent("DoubleMuon_Run2017B_31Mar2018", "/DoubleMuon/Run2017B-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

# Run2017C 31Mar2018

SingleElectron_Run2017C_31Mar2018 = creator.makeDataComponent("SingleElectron_Run2017C_31Mar2018", "/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017C_31Mar2018 = creator.makeDataComponent("SingleMuon_Run2017C_31Mar2018", "/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

DoubleEG_Run2017C_31Mar2018 = creator.makeDataComponent("DoubleEG_Run2017C_31Mar2018", "/DoubleEG/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MuonEG_Run2017C_31Mar2018 = creator.makeDataComponent("MuonEG_Run2017C_31Mar2018", "/MuonEG/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuon_Run2017C_31Mar2018 = creator.makeDataComponent("DoubleMuon_Run2017C_31Mar2018", "/DoubleMuon/Run2017C-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

# Run2017D 31Mar2018

SingleElectron_Run2017D_31Mar2018 = creator.makeDataComponent("SingleElectron_Run2017D_31Mar2018", "/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017D_31Mar2018 = creator.makeDataComponent("SingleMuon_Run2017D_31Mar2018", "/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

DoubleEG_Run2017D_31Mar2018 = creator.makeDataComponent("DoubleEG_Run2017D_31Mar2018", "/DoubleEG/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MuonEG_Run2017D_31Mar2018 = creator.makeDataComponent("MuonEG_Run2017D_31Mar2018", "/MuonEG/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuon_Run2017D_31Mar2018 = creator.makeDataComponent("DoubleMuon_Run2017D_31Mar2018", "/DoubleMuon/Run2017D-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

# Run2017E 31Mar2018

SingleElectron_Run2017E_31Mar2018 = creator.makeDataComponent("SingleElectron_Run2017E_31Mar2018", "/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017E_31Mar2018 = creator.makeDataComponent("SingleMuon_Run2017E_31Mar2018", "/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

DoubleEG_Run2017E_31Mar2018 = creator.makeDataComponent("DoubleEG_Run2017E_31Mar2018", "/DoubleEG/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MuonEG_Run2017E_31Mar2018 = creator.makeDataComponent("MuonEG_Run2017E_31Mar2018", "/MuonEG/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuon_Run2017E_31Mar2018 = creator.makeDataComponent("DoubleMuon_Run2017E_31Mar2018", "/DoubleMuon/Run2017E-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

# Run2017F 31Mar2018

SingleElectron_Run2017F_31Mar2018 = creator.makeDataComponent("SingleElectron_Run2017F_31Mar2018", "/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
SingleMuon_Run2017F_31Mar2018 = creator.makeDataComponent("SingleMuon_Run2017F_31Mar2018", "/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)

DoubleEG_Run2017F_31Mar2018 = creator.makeDataComponent("DoubleEG_Run2017F_31Mar2018", "/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
MuonEG_Run2017F_31Mar2018 = creator.makeDataComponent("MuonEG_Run2017F_31Mar2018", "/MuonEG/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)
DoubleMuon_Run2017F_31Mar2018 = creator.makeDataComponent("DoubleMuon_Run2017F_31Mar2018", "/DoubleMuon/Run2017F-31Mar2018-v1/MINIAOD", "CMS", ".*root", json)


# les lists 

data_single_electron = [SingleElectron_Run2017B_31Mar2018, SingleElectron_Run2017C_31Mar2018, SingleElectron_Run2017D_31Mar2018, SingleElectron_Run2017E_31Mar2018, SingleElectron_Run2017F_31Mar2018]

data_single_muon = [SingleMuon_Run2017B_31Mar2018, SingleMuon_Run2017C_31Mar2018, SingleMuon_Run2017D_31Mar2018, SingleMuon_Run2017E_31Mar2018, SingleMuon_Run2017F_31Mar2018]

data_muon_electron = [MuonEG_Run2017B_31Mar2018, MuonEG_Run2017C_31Mar2018, MuonEG_Run2017D_31Mar2018, MuonEG_Run2017E_31Mar2018, MuonEG_Run2017F_31Mar2018]

data_dimuon = [DoubleMuon_Run2017B_31Mar2018, DoubleMuon_Run2017C_31Mar2018, DoubleMuon_Run2017D_31Mar2018, DoubleMuon_Run2017E_31Mar2018, DoubleMuon_Run2017F_31Mar2018]

data_dielectron = [DoubleEG_Run2017B_31Mar2018, DoubleEG_Run2017C_31Mar2018, DoubleEG_Run2017D_31Mar2018, DoubleEG_Run2017E_31Mar2018, DoubleEG_Run2017F_31Mar2018]

data_elecmuon = data_single_electron + data_single_muon + data_muon_electron
data_ttbar = data_elecmuon + data_dimuon + data_dielectron


