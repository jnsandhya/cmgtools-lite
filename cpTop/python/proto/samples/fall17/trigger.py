from CMGTools.H2TauTau.proto.analyzers.TriggerAnalyzer import TriggerFilterMatch

############################################################################
# 2017
############################################################################

mc_triggers = [
    #'HLT_Ele32 WPTight Gsf_v*',
    #'HLT_Ele35 WPTight Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    #'HLT_IsoMu24_v*',
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]


data_triggers = {}

data_triggers['A'] = [
    # electron
    #'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*',
    #'HLT_Ele35_WPTight_Gsf_v*',
    #'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    # muon
    #'HLT_IsoTkMu24_v*',
    #'HLT_IsoMu24_v*',
    #'HLT_IsoMu24_eta2p1_v*',
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]
data_triggers['B'] = data_triggers['A']

data_triggers['C'] = [
    # electron
    #'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*',
    #'HLT_Ele35_WPTight_Gsf_v*',
    #'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    # muon
    #'HLT_IsoMu24_eta2p1_v*',
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]

data_triggers['D'] = [
    # electron
    #'HLT_Ele32_WPTight_Gsf_v*',
    #'HLT_Ele35_WPTight_Gsf_v*',
   # 'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    # muon
    #'HLT_IsoMu24_eta2p1_v*',
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]

data_triggers['E'] = [
    # electron
    #'HLT_Ele32_WPTight_Gsf_v*',
    #'HLT_Ele35_WPTight_Gsf_v*',
    #'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    # muon
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]

data_triggers['F'] = [
    # electron
    #'HLT_Ele32_WPTight_Gsf_v*',
    #'HLT_Ele35_WPTight_Gsf_v*',
    #'HLT_Ele38_WPTight_Gsf_v*',
    #'HLT_Ele40_WPTight_Gsf_v*',
    'HLT_Ele23_CaloIdM_TrackIdM_PFJet30_v*',
    # muon
    #'HLT_IsoMu27_v*',
    'HLT_Mu20_v*',
]

















