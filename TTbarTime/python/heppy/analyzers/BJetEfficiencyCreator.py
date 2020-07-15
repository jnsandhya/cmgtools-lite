import os
import ROOT
import numpy as np

from ROOT import TRandom3, TFile, TH2F
ROOT.gSystem.Load('libCondToolsBTau')

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters

def isBJetSelected(jet_param):
    if jet_param.pt()>30 and abs(jet.eta())<2.4 and jet.jetID("PAG_ttbar_Loose"):
        return True
    else:
        return False 
      
def isBTagged(csv, csv_cut=0.5803): #CSVv2
#def isBTagged(csv, csv_cut=0.1522): #DeepCSV
    if csv>csv_cut:
        return True
    else:
        return False

class BJetEfficiencyCreator(Analyzer):
        
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(BJetEfficiencyCreator, self).__init__(cfg_ana, cfg_comp, looperName)
        
        self.h2_b = TH2F("h2_b","h2_b",19,20,1000,4,0,2.4)
        self.h2_c = TH2F("h2_c","h2_c",19,20,1000,4,0,2.4)
        self.h2_oth = TH2F("h2_oth","h2_oth",19,20,1000,4,0,2.4)

        self.btag_b = TH2F("btag_b","btag_b",19,20,1000,4,0,2.4)
        self.btag_c = TH2F("btag_c","btag_c",19,20,1000,4,0,2.4)
        self.btag_oth = TH2F("btag_oth","btag_oth",19,20,1000,4,0,2.4)
        
        #self.btag_eff_b = TH2F("btag_eff_b","btag_eff_b",19,20,1000,4,0,2.4)
        #self.btag_eff_c = TH2F("btag_eff_c","btag_eff_c",19,20,1000,4,0,2.4)
        #self.btag_eff_oth = TH2F("btag_eff_oth","btag_eff_oth",19,20,1000,4,0,2.4)

    def beginLoop(self, setup):
        super(BJetEfficiencyCreator, self).beginLoop(setup)
        self.counters.addCounter('BJetEfficiencyCreator')
        count = self.counters.counter('BJetEfficiencyCreator')
        count.register('All Events')
        #count.register('at least 2 good jets')
        count.register('total input jets')
        count.register('total b-jets')
        count.register('total b-tagged jets')

        

    def process(self, event):
      '''Adds the is_btagged attribute to the jets of the
      given jets collection.
      '''
      self.counters.counter('BJetEfficiencyCreator').inc('All Events')
      jets = getattr(event, self.cfg_ana.jets)

      for jet in jets:    
          self.counters.counter('BJetEfficiencyCreator').inc('total input jets')

          if self.cfg_ana.year == '2016': 
              if self.cfg_ana.tagger == 'DeepCSV' :
                  csv     = jet.btag("pfDeepCSVJetTags:probb") + jet.btag("pfDeepCSVJetTags:probbb")
                  csv_cut = 0.2217
              if self.cfg_ana.tagger == 'DeepJet' :
                  csv     = jet.btag("pfDeepFlavourJetTags:probb") +  jet.btag("pfDeepFlavourJetTags:probbb") +  jet.btag("pfDeepFlavourJetTags:problepb")
                  csv_cut = 0.0614
              if self.cfg_ana.tagger == 'CSVv2' :
                  csv     = jet.btag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
                  csv_cut = 0.5803 #assumption to keep it same as 2017, no SFs are actually provided for CSVv2 in 2016.
          else: 
              if self.cfg_ana.tagger == 'DeepCSV' :
                  csv     = jet.btag("pfDeepCSVJetTags:probb") + jet.btag("pfDeepCSVJetTags:probbb")
                  csv_cut = 0.1522
              if self.cfg_ana.tagger == 'DeepJet' :
                  csv     = jet.btag("pfDeepFlavourJetTags:probb") + jet.btag("pfDeepFlavourJetTags:probbb") + jet.btag("pfDeepFlavourJetTags:problepb")
                  csv_cut = 0.0521 #not sure if this will work on 2017 as the twiki says one needs to run recipe to obtain this on MiniAOD.
              if self.cfg_ana.tagger == 'CSVv2' :
                  csv     = jet.btag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
                  csv_cut = 0.5803 
              #csv_cut=0.1522) #(loose wp deepcsv)                                    
              #https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
              #https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy
              #print jet.hadronFlavour()
              #print jet.hadronFlavour()

          jet.is_btagged = isBTagged(csv, csv_cut) 
          
          if abs(jet.hadronFlavour()) == 5:
              self.counters.counter('BJetEfficiencyCreator').inc('total b-jets')
              self.h2_b.Fill(jet.pt(), abs(jet.eta()))
              if jet.is_btagged:
                  self.counters.counter('BJetEfficiencyCreator').inc('total b-tagged jets')
                  self.btag_b.Fill(jet.pt(), abs(jet.eta()))
                  #self.btag_eff_b.Fill(jet.pt(), abs(jet.eta()))
          elif abs(jet.hadronFlavour()) == 4:
              self.h2_c.Fill(jet.pt(), abs(jet.eta()))
              if jet.is_btagged:
                  self.btag_c.Fill(jet.pt(), abs(jet.eta()))
                  #self.btag_eff_c.Fill(jet.pt(), abs(jet.eta()))
          elif jet.hadronFlavour() == 0:
              self.h2_oth.Fill(jet.pt(), abs(jet.eta()))
              if jet.is_btagged:
                  self.btag_oth.Fill(jet.pt(), abs(jet.eta()))
                  #self.btag_eff_oth.Fill(jet.pt(), abs(jet.eta()))

      

    def write(self, setup):
        #self.btag_eff_b.Divide(self.h2_b)
        #self.btag_eff_c.Divide(self.h2_c)
        #self.btag_eff_oth.Divide(self.h2_oth)
        super(BJetEfficiencyCreator, self).write(setup)

        self.rootfile = TFile('/'.join([self.dirName,
                                            'btag.root']), 'recreate')

        #import pdb; pdb.set_trace()
        self.h2_b.Write()
        self.h2_c.Write()
        self.h2_oth.Write()
        self.btag_b.Write()
        self.btag_c.Write()        
        self.btag_oth.Write()
        #self.btag_eff_b.Write()
        #self.btag_eff_c.Write()        
        #self.btag_eff_oth.Write()
        self.rootfile.Write()
        self.rootfile.Close()


