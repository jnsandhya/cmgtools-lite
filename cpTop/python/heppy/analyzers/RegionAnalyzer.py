import os
import ROOT
from ROOT import TFile, TH2F

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer

class RegionAnalyzer(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(RegionAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)
                
    def process(self, event):
	
        jets = getattr(event, self.cfg_ana.jets)
        bjets = getattr(event, self.cfg_ana.bjets_60)
	a = str(len(jets))
	b = str(len(bjets))


        if len(jets) == 2 and len(bjets) == 0 :
            region = 0

	elif len(jets) == 2 and len(bjets) == 1 :
	    region = 1

	elif len(jets) == 3 and len(bjets) == 2 :
	    region = 2

        elif len(jets) == 3 and len(bjets) == 1 :
	    region = 2

	else :
            region = -1

        setattr(event, 'region', region)
	setattr(event, self.cfg_ana.output, region)

          
