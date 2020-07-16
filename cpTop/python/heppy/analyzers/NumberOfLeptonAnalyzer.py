import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

class NumberOfLeptonAnalyzer(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(NumberOfLeptonAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
                
    def process(self, event):
	
        electrons = getattr(event, self.cfg_ana.select_electron)
        muons = getattr(event, self.cfg_ana.select_muon)

	natureLepton = 0
	numberLeptons = len(electrons) + len(muons)

	if len(electrons) == 1 and len(muons) == 0:
		natureLepton = 1
	if len(electrons) == 0 and len(muons) == 1:
		natureLepton = 2

        setattr(event, 'numberLeptons', numberLeptons)
	setattr(event, self.cfg_ana.output, numberLeptons)
	setattr(event, 'natureLepton', natureLepton)

