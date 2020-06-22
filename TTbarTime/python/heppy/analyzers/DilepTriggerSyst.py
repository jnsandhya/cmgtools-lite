import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

class DilepTriggerSyst(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(DilepTriggerSyst, self).__init__(cfg_ana, cfg_comp, looperName)
        self.year       = self.cfg_ana.year
        if self.year == 2016 :
            
            rootfname_ee = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_ee2016_pt.root'])                       
            rootfname_em = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_emu2016_pt.root'])
            rootfname_mm = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_mumu2016_pt.root'])
            
        else:
            rootfname_ee = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_ee2017_pt.root'])                       
            rootfname_em = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_emu2017_pt.root'])
            rootfname_mm = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_mumu2017_pt.root'])
            
            #rootfname_muon = '/'.join([os.environ["CMSSW_BASE"],
            #'src/CMGTools/TTbarTime/data/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root'])
            
        self.mc_syst_ee_trig_file = TFile(rootfname_ee)
        self.mc_syst_em_trig_file = TFile(rootfname_em)
        self.mc_syst_mm_trig_file = TFile(rootfname_mm)
        #self.mc_syst_muon_isomu27_file = TFile(rootfname_muon)
          
        self.mc_syst_ee_trig_hist = self.mc_syst_ee_trig_file.Get('h_lep1Pt_lep2Pt_Step6')                              
        self.mc_syst_em_trig_hist = self.mc_syst_em_trig_file.Get('h_lep1Pt_lep2Pt_Step3')                              
        self.mc_syst_mm_trig_hist = self.mc_syst_mm_trig_file.Get('h_lep1Pt_lep2Pt_Step9')                              

        #self.mc_syst_muon_isomu27_hist = self.mc_syst_muon_isomu27_file.Get('IsoMu27_PtEtaBins/pt_abseta_ratio')
        #self.mc_syst_muon_mu50_hist    = self.mc_syst_muon_isomu27_file.Get('Mu50_PtEtaBins/pt_abseta_ratio')
                
    def process(self, event):
    
        syst_ee_trig_weight = 0.    
        syst_em_trig_weight = 0.    
        syst_mm_trig_weight = 0.    
        
        #syst_muon_isomu27_weight = 1.
        #syst_muon_mu50_weight    = 1.
        dilepton = getattr(event, self.cfg_ana.dilepton)
        muon = event.dileptons[0]._l1
        #if(muon.pt() <= 1200):
        #     if(muon.pt() >= 29):
        #         syst_muon_isomu27_weight *= self.mc_syst_muon_isomu27_hist.GetBinContent(pt_binned_IsoMu27(muon.pt()), eta_binned(abs(muon.eta())))
        #     if(muon.pt() >= 52):
        #         syst_muon_mu50_weight    *= self.mc_syst_muon_mu50_hist.GetBinContent(pt_binned_Mu50(muon.pt()), eta_binned(abs(muon.eta())))

        for dilep in dilepton:
            if(dilep.pt_lead() <= 200 and dilep.pt_sublead() <= 200): 
                syst_ee_trig_weight *= self.mc_syst_ee_trig_hist.GetBinError(self.mc_syst_ee_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead()))
                syst_em_trig_weight *= self.mc_syst_em_trig_hist.GetBinError(self.mc_syst_em_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead()))
                syst_mm_trig_weight *= self.mc_syst_mm_trig_hist.GetBinError(self.mc_syst_mm_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead()))



        setattr(event, 'systEETrigWeight', syst_ee_trig_weight)
        setattr(event, 'systEMTrigWeight', syst_em_trig_weight)
        setattr(event, 'systMMTrigWeight', syst_mm_trig_weight)

        #setattr(event, 'systmTrigIsoMu27Weight', syst_muon_isomu27_weight)
        #setattr(event, 'systmTrigMu50Weight', syst_muon_mu50_weight)

