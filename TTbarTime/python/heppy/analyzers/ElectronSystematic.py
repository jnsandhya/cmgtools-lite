import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer


class ElectronSystematic(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(ElectronSystematic, self).__init__(cfg_ana, cfg_comp, looperName)
        self.year       = self.cfg_ana.year

        if self.year == '2016':
            rootfname_id = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/eleSF/2016LegacyReReco_ElectronTight_Fall17V2.root'])
            
            rootfname_reco = '/'.join([os.environ["CMSSW_BASE"],
                                       'src/CMGTools/TTbarTime/data/2016/eleSF/EGM2D_BtoH_GT20GeV_RecoSF_Legacy2016.root'])
                
        elif self.year == '2017':
            rootfname_id = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2017_ElectronTight.root'])
            
            rootfname_reco = '/'.join([os.environ["CMSSW_BASE"],
                                       'src/CMGTools/TTbarTime/data/egammaEffi.txt_EGM2D_runBCDEF_passingRECO.root'])


        self.mc_syst_id_file = TFile(rootfname_id)
        self.mc_syst_id_hist = self.mc_syst_id_file.Get('EGamma_SF2D')
        
        self.mc_syst_reco_file = TFile(rootfname_reco)
        self.mc_syst_reco_hist = self.mc_syst_reco_file.Get('EGamma_SF2D')
        
        
    def process(self, event):
        
        syst_id_weight = 1.        
        syst_reco_weight = 1.


        electrons = getattr(event, self.cfg_ana.electrons)    
        for elec in electrons:
            if(elec.pt()>10 and elec.pt()<500 and abs(elec.superCluster().eta()) <= 2.5):
                syst_id_weight *= self.mc_syst_id_hist.GetBinError(self.mc_syst_id_hist.FindBin(elec.superCluster().eta(),elec.pt()))
                if(elec.pt()>20):
                    syst_reco_weight *= self.mc_syst_reco_hist.GetBinError(self.mc_syst_reco_hist.FindBin(elec.superCluster().eta(),elec.pt()))
        
        if(syst_id_weight == 1.):
            syst_id_weight = 0.
        if(syst_reco_weight == 1.):
            syst_reco_weight = 0.

        setattr(event, 'systElecIdWeight', syst_id_weight)
        setattr(event, 'systElecRecoWeight', syst_reco_weight)
        event.eventSystWeight *= event.systElecIdWeight
        event.eventSystWeight *= event.systElecRecoWeight
        
        
