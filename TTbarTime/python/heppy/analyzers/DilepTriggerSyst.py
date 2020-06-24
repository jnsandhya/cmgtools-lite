import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

class DilepTriggerSyst(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(DilepTriggerSyst, self).__init__(cfg_ana, cfg_comp, looperName)
        self.year       = self.cfg_ana.year
        if self.year == '2016':
            
            rootfname_ee = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_ee2016_pt.root'])                       
            rootfname_em = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_emu2016_pt.root'])
            rootfname_mm = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/dilepSF/TriggerSF_mumu2016_pt.root'])
            
        elif self.year == '2017':
            rootfname_ee = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_ee2017_pt.root'])                       
            rootfname_em = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_emu2017_pt.root'])
            rootfname_mm = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/TriggerSF_mumu2017_pt.root'])
            
        self.mc_syst_ee_trig_file = TFile(rootfname_ee)
        self.mc_syst_em_trig_file = TFile(rootfname_em)
        self.mc_syst_mm_trig_file = TFile(rootfname_mm)
          
        self.mc_syst_ee_trig_hist = self.mc_syst_ee_trig_file.Get('h_lep1Pt_lep2Pt_Step6')                              
        self.mc_syst_em_trig_hist = self.mc_syst_em_trig_file.Get('h_lep1Pt_lep2Pt_Step3')                              
        self.mc_syst_mm_trig_hist = self.mc_syst_mm_trig_file.Get('h_lep1Pt_lep2Pt_Step9')                              

                
    def process(self, event):
    
        syst_ee_trig_weight = 0.    
        syst_em_trig_weight = 0.    
        syst_mm_trig_weight = 0.    

        dilepton = getattr(event, self.cfg_ana.dilepton)

        for dilep in dilepton:
            if(dilep.pt_lead() <= 200 and dilep.pt_sublead() <= 200): 
                syst_ee_trig_weight += ((self.mc_syst_ee_trig_hist.GetBinError(self.mc_syst_ee_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)/((self.mc_syst_ee_trig_hist.GetBinContent(self.mc_syst_ee_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)
                syst_em_trig_weight += ((self.mc_syst_em_trig_hist.GetBinError(self.mc_syst_em_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)/((self.mc_syst_em_trig_hist.GetBinContent(self.mc_syst_em_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)
                syst_mm_trig_weight += ((self.mc_syst_mm_trig_hist.GetBinError(self.mc_syst_mm_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)/((self.mc_syst_mm_trig_hist.GetBinContent(self.mc_syst_mm_trig_hist.FindBin(dilep.pt_lead(), dilep.pt_sublead())))**2)

        syst_ee_trig_weight = syst_ee_trig_weight**0.5
        syst_em_trig_weight = syst_em_trig_weight**0.5
        syst_mm_trig_weight = syst_mm_trig_weight**0.5

        setattr(event, 'systEETrigWeight', syst_ee_trig_weight)
        setattr(event, 'systEMTrigWeight', syst_em_trig_weight)
        setattr(event, 'systMMTrigWeight', syst_mm_trig_weight)
