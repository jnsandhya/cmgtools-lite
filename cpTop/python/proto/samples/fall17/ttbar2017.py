import os 
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator

creator = ComponentCreator()

json = os.path.expandvars('$CMSSW_BASE/src/CMGTools/TTbarTime/data/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt')
lumi = 41529.

############################################################################
# MC
############################################################################

signal_MC_dilep = creator.makeMCComponent("MC_a_dilep","/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 88.2);
signal_MC_semilep = creator.makeMCComponent("MC_b_semilep","/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root", 365.3);

background_MC_TTW = creator.makeMCComponent("MC_c_TTW","/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.2043);
background_MC_TTZ = creator.makeMCComponent("MC_d_TTZ","/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",0.2529);

background_MC_ST_s = creator.makeMCComponent("MC_e_ST_s","/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",3.36);
background_MC_ST_t_top = creator.makeMCComponent("MC_f_ST_t_top","/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root",136.02);
background_MC_ST_t_antitop = creator.makeMCComponent("MC_g_ST_t_antitop","/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM","CMS",".*root",80.95);
background_MC_tW_top = creator.makeMCComponent("MC_h_ST_tW_top","/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root",35.9);
background_MC_tW_antitop = creator.makeMCComponent("MC_i_ST_tW_antitop","/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root",35.9);

background_MC_WW = creator.makeMCComponent("MC_j_WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 118.7)
background_MC_WZ = creator.makeMCComponent("MC_k_WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 47.13)
background_MC_ZZ = creator.makeMCComponent("MC_l_ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 16.523)
background_MC_WJets = creator.makeMCComponent("MC_m_WJets", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM", "CMS", ".*root", 61526.7)

background_MC_DY_50 = creator.makeMCComponent("MC_n_DY_50", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 6025.2)
background_MC_DY_1050 = creator.makeMCComponent("MC_o_DY_1050", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 22635.1)

#############################################################################
#MC QCD
#############################################################################

background_MC_QCD_pt_15to20_MuEnriched = creator.makeMCComponent("MC_p_QCD_Mu_15to20","/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 3336011);
background_MC_QCD_pt_20to30_MuEnriched = creator.makeMCComponent("MC_q_QCD_Mu_20to30", "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root",3987854.9);
background_MC_QCD_pt_30to50_MuEnriched = creator.makeMCComponent("MC_r_QCD_Mu_30to50", "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM","CMS",".*root", 1705381);
background_MC_QCD_pt_50to80_MuEnriched = creator.makeMCComponent("MC_s_QCD_Mu_50to80", "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 395178);
background_MC_QCD_pt_80to120_MuEnriched = creator.makeMCComponent("MC_t_QCD_Mu_80to120", "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 106889.4);
background_MC_QCD_pt_120to170_MuEnriched = creator.makeMCComponent("MC_u_QCD_Mu_120to170", "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 23773.61);
background_MC_QCD_pt_170to300_MuEnriched = creator.makeMCComponent("MC_v_QCD_Mu_170to300", "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 8292.982);
background_MC_QCD_pt_300to470_MuEnriched = creator.makeMCComponent("MC_w_QCD_Mu_300to470", "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 797.35269);
background_MC_QCD_pt470to600_MuEnriched = creator.makeMCComponent("MC_x_QCD_Mu_470to600", "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 56.588336);
background_MC_QCD_pt600to800_MuEnriched = creator.makeMCComponent("MC_y_QCD_Mu_600to800", "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 25.09505908);
background_MC_QCD_pt800to1000_MuEnriched = creator.makeMCComponent("MC_z_QCD_Mu_800to1000", "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 4.707368272);
background_MC_QCD_pt1000toInf_MuEnriched = creator.makeMCComponent("MC_aa_QCD_Mu_1000toInf", "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1.62131692);

background_MC_QCD_pt20to30_EMEnriched = creator.makeMCComponent("MC_ab_QCD_EM_20to30", "/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 4948840);
background_MC_QCD_pt30to50_EMEnriched = creator.makeMCComponent("MC_ac_QCD_EM_30to50", "/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 6324800);
background_MC_QCD_pt50to80_EMEnriched = creator.makeMCComponent("MC_ad_QCD_EM_50to80", "/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1806336);
background_MC_QCD_pt80to120_EMEnriched = creator.makeMCComponent("MC_ae_QCD_EM_80to120", "/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 380538);
background_MC_QCD_pt120to170_EMEnriched = creator.makeMCComponent("MC_af_QCD_EM_120to170", "/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM", "CMS", ".*root", 66634.28);
background_MC_QCD_pt170to300_EMEnriched = creator.makeMCComponent("MC_ag_QCD_EM_170to300", "/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 20859);
background_MC_QCD_pt300toInf_EMEnriched = creator.makeMCComponent("MC_ah_QCD_EM_300toInf", "/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM", "CMS", ".*root", 1350);


mc_ttbar = [
    signal_MC_dilep,
    signal_MC_semilep,
    background_MC_TTW,
    background_MC_TTZ,
    background_MC_ST_s,
    background_MC_ST_t_top,
    background_MC_ST_t_antitop,
    background_MC_tW_top,
    background_MC_tW_antitop,
    background_MC_WW, 
    background_MC_WZ,
    background_MC_ZZ,
    background_MC_WJets,
    background_MC_DY_50,
    background_MC_DY_1050
]

mc_singletop = [
    signal_MC_dilep,
    signal_MC_semilep,
    background_MC_ST_t_top,
    background_MC_ST_t_antitop, 
    background_MC_DY_50, 
    background_MC_DY_1050, 
    background_MC_WJets, 
    background_MC_tW_top, 
    background_MC_tW_antitop,
    background_MC_QCD_pt_15to20_MuEnriched,
    background_MC_QCD_pt_20to30_MuEnriched,
    background_MC_QCD_pt_30to50_MuEnriched,
    background_MC_QCD_pt_50to80_MuEnriched,
    background_MC_QCD_pt_80to120_MuEnriched,
    background_MC_QCD_pt_120to170_MuEnriched,
    background_MC_QCD_pt_170to300_MuEnriched,
    background_MC_QCD_pt_300to470_MuEnriched,
    background_MC_QCD_pt470to600_MuEnriched,
    background_MC_QCD_pt600to800_MuEnriched,
    background_MC_QCD_pt800to1000_MuEnriched,
    background_MC_QCD_pt1000toInf_MuEnriched,
    background_MC_QCD_pt20to30_EMEnriched,
    background_MC_QCD_pt30to50_EMEnriched,
    background_MC_QCD_pt50to80_EMEnriched,
    background_MC_QCD_pt80to120_EMEnriched,
    background_MC_QCD_pt120to170_EMEnriched,
    background_MC_QCD_pt170to300_EMEnriched,
    background_MC_QCD_pt300toInf_EMEnriched
]

mc_total = [
    #signal_MC_dilep,
    signal_MC_semilep,
    #background_MC_ST_t_top,
    #background_MC_ST_t_antitop, 
    #background_MC_DY_50, 
    #background_MC_DY_1050, 
    #background_MC_WJets, 
    #background_MC_tW_top, 
    #background_MC_tW_antitop,
    #background_MC_QCD_pt_15to20_MuEnriched,
    #background_MC_QCD_pt_20to30_MuEnriched,
    #background_MC_QCD_pt_30to50_MuEnriched,
    #background_MC_QCD_pt_50to80_MuEnriched,
    background_MC_QCD_pt_80to120_MuEnriched,
    #background_MC_QCD_pt_120to170_MuEnriched,
    #background_MC_QCD_pt_170to300_MuEnriched,
    #background_MC_QCD_pt_300to470_MuEnriched,
    #background_MC_QCD_pt470to600_MuEnriched,
    #background_MC_QCD_pt600to800_MuEnriched,
    #background_MC_QCD_pt800to1000_MuEnriched,
    #background_MC_QCD_pt1000toInf_MuEnriched,
    #background_MC_QCD_pt20to30_EMEnriched,
    #background_MC_QCD_pt30to50_EMEnriched,
    #background_MC_QCD_pt50to80_EMEnriched,
    #background_MC_QCD_pt80to120_EMEnriched,
    #background_MC_QCD_pt120to170_EMEnriched,
    #background_MC_QCD_pt170to300_EMEnriched,
    #background_MC_QCD_pt300toInf_EMEnriched
]

############################################################################
# MC
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

data_singletop = data_single_electron + data_single_muon

reversed_electron = data_single_electron
reversed_muon = data_single_muon

