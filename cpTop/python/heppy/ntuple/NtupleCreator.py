from tools import *
import math

default = Variable.default

event = Block(
    'event', lambda x: x,
    run = v(lambda x: x.run, int),
    lumi = v(lambda x: x.lumi, int),
    event = v(lambda x: x.eventId, int, 'l'),
    n_up = v(lambda x: getattr(x, 'NUP', default), int),
    n_pu = v(lambda x: getattr(x, 'nPU', default) if getattr(x, 'nPU', default) is not None else default, int),# to handle data and embedded samples
    n_pv = v(lambda x: len(x.vertices), int),
    rho = v(lambda x: x.rho),
    is_data = v(lambda x: x.input.eventAuxiliary().isRealData(), int),
    region = v(lambda x: x.region, int),
    natureLepton = v(lambda x: x.natureLepton, int),
    NumberOfLeptons = v(lambda x: x.numberLeptons, int),
    weight_generator = v(lambda x : getattr(x, 'generatorWeight', 1.))
    )
   
jets40 = Block(
    'jets40', lambda x: x.jets_40,
    n_jets_pt40 = v(lambda x: len(x), int),
    j1_pt = v(lambda x: x[0].pt() if len(x)>0 else default),
    j1_eta = v(lambda x: x[0].eta() if len(x)>0 else default),
    j1_phi = v(lambda x: x[0].phi() if len(x)>0 else default),
    j1_energy = v(lambda x: x[0].energy() if len(x)>0 else default),
    j1_mass = v(lambda x: x[0].mass() if len(x)>0 else default),
    # j1_bcsv = v(lambda x: x.bcsv()),
    j1_pumva = v(lambda x: x[0].puMva('pileupJetId:fullDiscriminant') if len(x)>0 else default),
#    j1_puid = v(lambda x: x[0].pileUpJetId_htt() if len(x)>0 else default),
    j1_flavour_parton = v(lambda x: x[0].partonFlavour() if len(x)>0 else default),
    j1_flavour_hadron = v(lambda x: x[0].hadronFlavour() if len(x)>0 else default),
    j1_rawf = v(lambda x: x[0].rawFactor() if len(x)>0 else default),
    j2_pt = v(lambda x: x[1].pt() if len(x)>1 else default),
    j2_eta = v(lambda x: x[1].eta() if len(x)>1 else default),
    j2_phi = v(lambda x: x[1].phi() if len(x)>1 else default),
    j2_energy = v(lambda x: x[1].energy() if len(x)>1 else default),
    j2_mass = v(lambda x: x[1].mass() if len(x)>1 else default),
    j2_pumva = v(lambda x: x[1].puMva('pileupJetId:fullDiscriminant') if len(x)>1 else default ),
#    j2_puid = v(lambda x: x[1].pileUpJetId_htt() if len(x)>1 else default ),
    j2_flavour_parton = v(lambda x: x[1].partonFlavour() if len(x)>1 else default),
    j2_flavour_hadron = v(lambda x: x[1].hadronFlavour() if len(x)>1 else default),
    j2_rawf = v(lambda x: x[1].rawFactor() if len(x)>1 else default),
    j3_pt = v(lambda x: x[2].pt() if len(x)>2 else default),
    j3_eta = v(lambda x: x[2].eta() if len(x)>2 else default),
    j3_phi = v(lambda x: x[2].phi() if len(x)>2 else default),
    j3_energy = v(lambda x: x[2].energy() if len(x)>2 else default),
    j3_mass = v(lambda x: x[2].mass() if len(x)>2 else default),
    j3_pumva = v(lambda x: x[2].puMva('pileupJetId:fullDiscriminant') if len(x)>2 else default ),
#    j3_puid = v(lambda x: x[2].pileUpJetId_htt() if len(x)>1 else default ),
    j3_flavour_parton = v(lambda x: x[2].partonFlavour() if len(x)>2 else default),
    j3_flavour_hadron = v(lambda x: x[2].hadronFlavour() if len(x)>2 else default),
    j3_rawf = v(lambda x: x[2].rawFactor() if len(x)>2 else default),
)

metvars = Block(
    'metvars', lambda x: x.pfmet,
    met = v(lambda x: x.pt()),
    metphi = v(lambda x: x.phi()),
)

weights = Block(
    'weights', lambda x: x, 
    weight = v(lambda x : x.eventWeight),
    weight_pu = v(lambda x : getattr(x, 'puWeight', 1.)),
    weight_sfb = v(lambda x : getattr(x, 'sfbWeight', 1.)),
    weight_sfe_id = v(lambda x : getattr(x, 'sfeIdWeight', 1.)),
    weight_sfe_reco = v(lambda x : getattr(x, 'sfeRecoWeight', 1.)),
    weight_sfm_id = v(lambda x : getattr(x, 'sfmIdWeight', 1.)),
    weight_sfm_iso = v(lambda x : getattr(x, 'sfmIsoWeight', 1.)),
    weight_sfm_trig_isomu27 = v(lambda x : getattr(x, 'sfmTrigIsoMu27Weight', 1.)),
    weight_sfm_trig_mu50 = v(lambda x : getattr(x, 'sfmTrigMu50Weight', 1.)),
#    weight_sf_ee_trig = v(lambda x : getattr(x, 'sfEETrigWeight', 1.)),
    weight_sf_em_trig = v(lambda x : getattr(x, 'sfEMTrigWeight', 1.)),
#    weight_sf_mm_trig = v(lambda x : getattr(x, 'sfMMTrigWeight', 1.)),
) 

triggers_fired = Block(
    'triggers_fired', lambda x: getattr(x, 'trigger_infos', []),
    # electron
    trg_electron_ele32doubleEG_fired       = v(lambda x : any('Ele32_WPTight_Gsf_L1DoubleEG_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele32_fired               = v(lambda x : any('Ele32_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele35_fired               = v(lambda x : any('Ele35_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    trg_electron_ele38_fired               = v(lambda x : any('Ele38_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)), 
    trg_electron_ele40_fired               = v(lambda x : any('Ele40_WPTight_Gsf_v' in trg.name for trg in x if trg.fired)),
    # muon 
    trg_muon_mu24_fired                    = v(lambda x : any('IsoMu24_v' in trg.name for trg in x if trg.fired)),
    trg_muon_mu24tk_fired                  = v(lambda x : any('IsoTkMu24_v' in trg.name for trg in x if trg.fired)),
    trg_muon_mu24eta21_fired               = v(lambda x : any('IsoMu24_eta2p1_v' in trg.name for trg in x if trg.fired)), 
    trg_muon_mu27_fired                    = v(lambda x : any('IsoMu27_v' in trg.name for trg in x if trg.fired)),    
)

bjets = Block(
    'bjets', lambda x: x.bjets_60,
    n_bjets = v(lambda x: len(x), int),
)
for vname, variable in jets40.iteritems():
    if not vname.startswith('j'):
        continue
    newname = vname.replace('j1','b1',1)
    newname = newname.replace('j2','b2',1)
    newname = newname.replace('j3','b3',1)
    bjets[newname] = variable

electron = Block(
    'electron', lambda x: x.select_electron,
    pt_elec    = v(lambda x: x[0].pt() if len(x)>0 else default),
    eta_elec   = v(lambda x: x[0].eta() if len(x)>0 else default),
    phi_elec   = v(lambda x: x[0].phi() if len(x)>0 else default),
    m_elec     = v(lambda x: x[0].mass() if len(x)>0 else default),
    q_elec     = v(lambda x: x[0].charge() if len(x)>0 else default),
    iso_elec   = v(lambda x: x[0].iso_htt() if len(x)>0 else default),
    energy_elec = v(lambda x: x[0].energy() if len(x)>0 else default),
)

muon = Block(
    'muon', lambda x: x.select_muon,
    pt_muon    = v(lambda x: x[0].pt() if len(x)>0 else default),
    eta_muon   = v(lambda x: x[0].eta() if len(x)>0 else default),
    phi_muon   = v(lambda x: x[0].phi() if len(x)>0 else default),
    m_muon     = v(lambda x: x[0].mass() if len(x)>0 else default),
    q_muon     = v(lambda x: x[0].charge() if len(x)>0 else default),
    iso_muon   = v(lambda x: x[0].iso_htt() if len(x)>0 else default),
    energy_muon = v(lambda x: x[0].energy() if len(x)>0 else default),
)

common = EventContent(
    [event, weights, jets40, bjets, electron, muon, metvars, triggers_fired]
)

################################################################################
#Weight Generator
################################################################################

nPU = Block(
    'pu', lambda x: x,
    pu = v(lambda x: x.nPU)
)

pileup = EventContent(
    [nPU]
)

