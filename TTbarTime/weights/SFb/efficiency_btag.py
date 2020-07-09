import sys,os
from optparse import OptionParser
from ROOT import TH2F, TFile, TCanvas
import argparse

usage = "usage: python efficiency_btag.py [options] \n example: python efficiency_btag.py -l CRABtest -y year"
parser = OptionParser(usage=usage)
parser.add_option("-y","--year", dest='year', default="2016", help="year on which u want to run the btag")
parser.add_option("-l", "--prod_label", dest = "prod_label",
                      default='BTag',
                      help='The prod label or part of prod labels to be selected.')
parser.add_option("-a", dest='algo',default="DeepCSV", help="btag algorithm (CSVv2 or DeepCSV)")
parser.add_option("-g", "--get_files", dest="get_files",
                      action="store_true", default=False,
                      help='whether or not to get the PU files')
options,args = parser.parse_args()


print options


#path = "$CMSSW_BASE/src/CMGTools/TTbarTime/weights/SFb/"

#print(algo)

samples=[]
samples=os.listdir("../../scripts/"+options.prod_label)

dir_input  = "files/"+options.year+"/"+options.algo+"/"
if options.get_files:
    if not os.path.exists(dir_input):
        '''
        create the input file path
         '''
        print "here am I creating input directory" 
        os.makedirs(dir_input)
    #samples=os.listdir("../../scripts/"+options.prod_label)
    os.chdir(dir_input)
    for i in samples:
        os.system("cp -r ../../../../../scripts/"+options.prod_label+"/"+i+" . ") 
    os.chdir("../../")

dir_output = options.year+"/"+options.algo+"/"
if not os.path.exists(dir_output):
    os.makedirs(dir_output)

btag_file = "btag.root"

rootfile = []
tot_b    = TH2F("h2_b","btag_eff_b",19,20,1000,4,0,2.4)
tot_c    = TH2F("h2_c","btag_eff_c",19,20,1000,4,0,2.4)
tot_oth  = TH2F("h2_oth","btag_eff_oth",19,20,1000,4,0,2.4)


eff_b    = TH2F("btag_b","btag_eff_b",19,20,1000,4,0,2.4)
eff_c    = TH2F("btag_c","btag_eff_c",19,20,1000,4,0,2.4)
eff_oth  = TH2F("btag_oth","btag_eff_oth",19,20,1000,4,0,2.4)

for i in range (len(samples)):
    rootfile.append(TFile(dir_input+"/"+samples[i]+"/"+btag_file))
    tot_b.Add(rootfile[i].Get("h2_b"))
    tot_c.Add(rootfile[i].Get("h2_c"))
    tot_oth.Add(rootfile[i].Get("h2_oth"))
    eff_b.Add(rootfile[i].Get("btag_b"))
    eff_c.Add(rootfile[i].Get("btag_c"))
    eff_oth.Add(rootfile[i].Get("btag_oth"))
    
#eff_b.Scale((1./len(rootfile)))
#eff_c.Scale((1./len(rootfile)))
#eff_oth.Scale((1./len(rootfile)))
 
eff_b.Divide(tot_b)
eff_c.Divide(tot_c)
eff_oth.Divide(tot_oth)
 
newfile = TFile(dir_output+"btag_efficiency_"+options.algo+".root", "RECREATE")
eff_b.Write()
eff_c.Write()
eff_oth.Write()
#rootfile[0].Get("btag_eff_c").Write("test")
newfile.Close()

print ("fini !")
