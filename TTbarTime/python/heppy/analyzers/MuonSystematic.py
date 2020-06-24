import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer


class MuonSystematic(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(MuonSystematic, self).__init__(cfg_ana, cfg_comp, looperName)
        self.lumi_BCDEF = 19695.422958521
        self.lumi_GH    = 16226.452636126
        self.year       = self.cfg_ana.year

        if self.year == '2016':
            rootfname_id_1 = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/2016/muonSF/SystUnc/RunBCDEF_SF_ID.root'])
            rootfname_iso_1 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/TTbarTime/data/2016/muonSF/SystUnc/RunBCDEF_SF_ISO.root'])
            rootfname_id_2 = '/'.join([os.environ["CMSSW_BASE"],
                           'src/CMGTools/TTbarTime/data/2016/muonSF/SystUnc/RunGH_SF_ID.root'])                       
            rootfname_iso_2 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/TTbarTime/data/2016/muonSF/SystUnc/RunGH_SF_ISO.root'])
                

  
            self.mc_syst_id_file1 = TFile(rootfname_id_1)
            self.mc_syst_id_hist1 = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_eta_pt_syst')

                
            self.mc_syst_iso_file1 = TFile(rootfname_iso_1)
            self.mc_syst_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst')

            self.mc_syst_id_file2 = TFile(rootfname_id_2)
            self.mc_syst_id_hist2 = self.mc_syst_id_file2.Get('NUM_TightID_DEN_genTracks_eta_pt_syst')                              
                
            self.mc_syst_iso_file2 = TFile(rootfname_iso_2)
            self.mc_syst_iso_hist2 = self.mc_syst_iso_file2.Get('NUM_TightRelIso_DEN_TightIDandIPCut_eta_pt_syst') 

        elif self.year == '2017':
            rootfname_id_1 = '/'.join([os.environ["CMSSW_BASE"],
                                     'src/CMGTools/TTbarTime/data/RunBCDEF_SF_ID.root'])                       
            rootfname_iso_1 = '/'.join([os.environ["CMSSW_BASE"],
                              'src/CMGTools/TTbarTime/data/RunBCDEF_SF_ISO.root'])
            self.mc_syst_id_file1 = TFile(rootfname_id_1)
            self.mc_syst_id_hist1 = self.mc_syst_id_file1.Get('NUM_TightID_DEN_genTracks_pt_abseta')                              
            
            self.mc_syst_iso_file1 = TFile(rootfname_iso_1)
            self.mc_syst_iso_hist1 = self.mc_syst_iso_file1.Get('NUM_TightRelIso_DEN_TightIDandIPCut_pt_abseta')      
        
    def process(self, event):

        syst_id_weight = 0.    
        syst_iso_weight = 0.

        if self.year == '2016':
            syst_id_weight1  = 0.    
            syst_iso_weight1 = 0.
            syst_id_weight2  = 0.    
            syst_iso_weight2 = 0.

        muons = getattr(event, self.cfg_ana.muons)    

        for muon in muons:
            if(muon.pt() <= 120):
                if self.year == '2016':
                    syst_id_weight1  += self.mc_syst_id_hist1.GetBinError(self.mc_syst_id_hist1.FindBin(muon.eta(), muon.pt()))**2 /self.mc_syst_id_hist1.GetBinContent(self.mc_syst_id_hist1.FindBin(muon.eta(), muon.pt()))**2
                    syst_iso_weight1 += self.mc_syst_iso_hist1.GetBinError(self.mc_syst_iso_hist1.FindBin(muon.eta(), muon.pt()))**2/self.mc_syst_iso_hist1.GetBinContent(self.mc_syst_iso_hist1.FindBin(muon.eta(), muon.pt()))**2 
                    
                    syst_id_weight2  += self.mc_syst_id_hist2.GetBinError(self.mc_syst_id_hist2.FindBin(muon.eta(), muon.pt()))**2/self.mc_syst_id_hist2.GetBinContent(self.mc_syst_id_hist2.FindBin(muon.eta(), muon.pt()))**2
                    syst_iso_weight2 += self.mc_syst_iso_hist2.GetBinError(self.mc_syst_iso_hist2.FindBin(muon.eta(), muon.pt()))/self.mc_sys\
t_iso_hist2.GetBinContent(self.mc_syst_iso_hist2.FindBin(muon.eta(), muon.pt()))**2

                    syst_id_weight  += (syst_id_weight1*(self.lumi_BCDEF**2) + syst_id_weight2*(self.lumi_GH**2))/((self.lumi_BCDEF + self.lumi_GH)**2)
                    syst_iso_weight += (syst_iso_weight1*(self.lumi_BCDEF**2) + syst_iso_weight2*(self.lumi_GH**2))/((self.lumi_BCDEF + self.lumi_GH**2))
      
                elif self.year == '2017': 
                    syst_id_weight  += (self.mc_syst_id_hist1.GetBinError(self.mc_syst_id_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_syst_id_hist1.GetBinContent(self.mc_syst_id_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2 
                    syst_iso_weight *= (self.mc_syst_iso_hist1.GetBinError(self.mc_syst_iso_hist1.FindBin(muon.pt(),abs(muon.eta())))/self.mc_syst_iso_hist1.GetBinContent(self.mc_syst_iso_hist1.FindBin(muon.pt(),abs(muon.eta()))))**2

        
        syst_id_weight = sqrt(syst_id_weight)
        syst_iso_weight = sqrt(syst_iso_weight)

    
        setattr(event, 'systMuonIdWeight', syst_id_weight)
        setattr(event, 'systMuonIsoWeight', syst_iso_weight)
        event.eventSystWeight *= event.systMuonIdWeight
        event.eventSystWeight *= event.systMuonIsoWeight
        
       
#scale factor = (L(BCDEF)*sf(BCDEF) + L(GH)*sf(GH))/(L(BCDEF)+L(GH)) 
        
        
