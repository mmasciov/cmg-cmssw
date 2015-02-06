import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

cfg.Analyzer.nosubdir = True

import logging
logging.basicConfig(level=logging.ERROR)

##------------------------------------------
## Redefine what I need
##------------------------------------------

#Lepton
lepAna.loose_muon_dxy = 0.5
lepAna.loose_muon_dz  = 1.0
lepAna.loose_muon_relIso  = 0.15
lepAna.loose_electron_id  = "POG_Cuts_ID_2012_Veto"
lepAna.loose_electron_pt  = 5
lepAna.loose_electron_eta    = 2.4
lepAna.loose_electron_dxy    = 0.04
lepAna.loose_electron_dz     = 0.2
lepAna.loose_electron_relIso = 0.15
lepAna.loose_electron_lostHits = 999 # no cut
lepAna.inclusive_electron_lostHits = 999 # no cut
lepAna.mu_isoCorr = "deltaBeta"
lepAna.ele_isoCorr = "deltaBeta"
lepAna.ele_tightId = "Cuts_2012"
lepAna.notCleaningElectrons = True

# JET (for event variables do apply the jetID and not PUID yet)
jetAna.relaxJetId = False
jetAna.doPuId = False
jetAna.jetEta = 5.2
jetAna.jetEtaCentral = 2.5
jetAna.jetPt = 10.
jetAna.recalibrateJets = True
jetAna.jetLepDR = 0.4
jetAna.smearJets = False
jetAna.jetGammaDR = 0.4
jetAna.minGammaPt = 20
jetAna.gammaEtaCentral = 2.4
jetAna.cleanJetsFromIsoTracks = True ## added for Dominick
jetAna.doQG = True

# TAU 
tauAna.etaMax = 2.3
tauAna.dxyMax = 99999.
tauAna.dzMax = 99999.
tauAna.vetoLeptons = False
tauAna.vetoLeptonsPOG = True

# Photon
photonAna.etaCentral = 2.5
photonAna.gammaID = "PhotonCutBasedIDLoose_CSA14"

# Isolated Track
isoTrackAna.setOff=False

# recalibrate MET
metAna.recalibrate = False

##------------------------------------------ 
##  CONTROL VARIABLES
##------------------------------------------ 

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control

ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control'
            )

##------------------------------------------
##  TOLOLOGIAL VARIABLES: MT, MT2
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHTopoVarAnalyzer import ttHTopoVarAnalyzer

ttHTopoJetAna = cfg.Analyzer(
            ttHTopoVarAnalyzer, name = 'ttHTopoVarAnalyzer',
            doOnlyDefault = True
            )


##------------------------------------------
##  PRODUCER
##------------------------------------------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import triggers_HT900, triggers_MET170, triggers_HTMET, triggers_MT2_mumu, triggers_MT2_ee, triggers_MT2_mue, triggers_1mu, triggers_photon155,triggers_1mu_isolow

triggerFlagsAna.triggerBits = {
            'HT900' : triggers_HT900,
            'MET170' : triggers_MET170,
            'ht350met120' : triggers_HTMET,
            'SingleMu' : triggers_1mu_isolow,
            'DoubleMu' : triggers_MT2_mumu,
            'DoubleEl' : triggers_MT2_ee,
            'MuEG'     : triggers_MT2_mue,
            'htXprescale' : triggers_HTMET,
            'Photons'  : triggers_photon155
}

#-------- SEQUENCE

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyFullHad import *

treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyFullHad',
##     AutoFillTreeProducer, name='treeProducerSusyCore',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyFullHad_globalVariables,
     globalObjects = susyFullHad_globalObjects,
     collections = susyFullHad_collections,
     defaultFloatType = 'F',
)


susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
                        susyCounter)
sequence = cfg.Sequence(
    susyCoreSequence+[
    ttHMT2Control,
    ttHTopoJetAna,
    ttHFatJetAna,
    treeProducer,
    ])

###---- to switch off the comptrssion
#treeProducer.isCompressed = 0

#-------- SAMPLES AND TRIGGERS -----------
#from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import * 
from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14v2 import *
#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *

#selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsToLL_M50_PU20bx25, TTJets_PUS14 ]

#selectedComponents = [ TTJets_MSDecaysCKM_central_PU_S14_POSTLS170 ]
#selectedComponents = [ WJetsToLNu_HT100to200_PU_S14_POSTLS170, WJetsToLNu_HT200to400_PU_S14_POSTLS170, WJetsToLNu_HT400to600_PU_S14_POSTLS170, WJetsToLNu_HT600toInf_PU_S14_POSTLS170 ]

#selectedComponents = [ QCD_Pt1000to1400_PU_S14_POSTLS170, QCD_Pt10to15_PU_S14_POSTLS170, QCD_Pt15to30_PU_S14_POSTLS170, QCD_Pt120to170_PU_S14_POSTLS170, QCD_Pt170to300_PU_S14_POSTLS170, QCD_Pt1400to1800_PU_S14_POSTLS170, QCD_Pt1800_PU_S14_POSTLS170, QCD_Pt300to470_PU_S14_POSTLS170, QCD_Pt30to50_PU_S14_POSTLS170, QCD_Pt470to600_PU_S14_POSTLS170, QCD_Pt50to80_PU_S14_POSTLS170, QCD_Pt5to10_PU_S14_POSTLS170, QCD_Pt600to800_PU_S14_POSTLS170, QCD_Pt800to1000_PU_S14_POSTLS170, QCD_Pt80to120_PU_S14_POSTLS170 ]

#selectedComponents = [ DYJets_M50_HT100to200_PU_S14_POSTLS170, DYJets_M50_HT200to400_PU_S14_POSTLS170, DYJets_M50_HT400to600_PU_S14_POSTLS170, DYJets_M50_HT600toInf_PU_S14_POSTLS170 ]

#selectedComponents = [ GJets_HT100to200_PU_S14_POSTLS170, GJets_HT200to400_PU_S14_POSTLS170, GJets_HT400to600_PU_S14_POSTLS170, ZJetsToNuNu_HT200to400_PU_S14_POSTLS170, ZJetsToNuNu_HT400to600_PU_S14_POSTLS170, ZJetsToNuNu_HT600toInf_PU_S14_POSTLS170 ]

#selectedComponents = [ SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170, SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170, SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170, SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170, SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170 ]

#selectedComponents = [ DYJetsM50_HT100to200_PU_S14_POSTLS170, DYJetsM50_HT200to400_PU_S14_POSTLS170, DYJetsM50_HT400to600_PU_S14_POSTLS170, DYJetsM50_HT600toInf_PU_S14_POSTLS170, SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170, SMS_T1bbbb_2J_mGl1500_mLSP100_PU_S14_POSTLS170, SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170, SMS_T1tttt_2J_mGl1200_mLSP800_PU_S14_POSTLS170, SMS_T1tttt_2J_mGl1500_mLSP100_PU_S14_POSTLS170 ]

#selectedComponents = [ GJets_HT600toInf_PU_S14_POSTLS170 ]
#, ZJetsToNuNu_HT100to200_PU_S14_POSTLS170 ]

##selectedComponents = [ TTJets_PU20bx25 ]

#selectedComponents = [ SMS_T1qqqq_2J_mGl1000_mLSP800_PU_S14_POSTLS170 ]

selectedComponents = [
QCD_Pt1800to2400,
QCD_Pt2400to3200,
QCD_Pt3200,
QCD_HT250To500,
QCD_HT500To1000,
QCD_HT1000ToInf,
GJets_HT100to200,
GJets_HT200to400,
GJets_HT400to600,
GJets_HT600toInf,
]

#selectedComponents = [
##QCD_HT_250To500,
##QCD_HT_500To1000,
##QCD_HT_1000ToInf,
##QCD_HT_250To500_ext1,
##QCD_HT_500To1000_ext1,
##QCD_HT_1000ToInf_ext1,
#WJetsToLNu_HT100to200,
#WJetsToLNu_HT200to400,
#WJetsToLNu_HT400to600,
#WJetsToLNu_HT600toInf,
#DYJetsToLL_M50_HT100to200,
#DYJetsToLL_M50_HT200to400,
#DYJetsToLL_M50_HT400to600,
#DYJetsToLL_M50_HT600toInf,
##GJets_HT100to200,
##GJets_HT200to400,
##GJets_HT400to600,
##GJets_HT600toInf,
#ZJetsToNuNu_HT100to200,
#ZJetsToNuNu_HT200to400,
#ZJetsToNuNu_HT400to600,
#ZJetsToNuNu_HT600toInf,
#TTJets,
#SMS_T2tt_2J_mStop850_mLSP100,
#SMS_T2tt_2J_mStop650_mLSP325,
#SMS_T2tt_2J_mStop500_mLSP325,
#SMS_T2tt_2J_mStop425_mLSP325,
#SMS_T2qq_2J_mStop600_mLSP550,
#SMS_T2qq_2J_mStop1200_mLSP100,
#SMS_T2bb_2J_mStop900_mLSP100,
#SMS_T2bb_2J_mStop600_mLSP580,
#SMS_T1tttt_2J_mGl1500_mLSP100,
#SMS_T1tttt_2J_mGl1200_mLSP800,
#SMS_T1qqqq_2J_mGl1400_mLSP100,
#SMS_T1qqqq_2J_mGl1000_mLSP800,
#SMS_T1bbbb_2J_mGl1500_mLSP100,
#SMS_T1bbbb_2J_mGl1000_mLSP900
#]

#-------- HOW TO RUN
test = 1
if test==2:
    # test a single component, using a single thread.
    #comp=TTJets_PU20bx25 #TTJets_forSynch
    #comp=SMS_T1qqqq_2J_mGl1400_mLSP100_PU_S14_POSTLS170 # small files for testing
    #comp=SMS_T1bbbb_2J_mGl1000_mLSP900_PU_S14_POSTLS170
    #comp=GJets_HT100to200_PU_S14_POSTLS170
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']
    #comp.files = ['/afs/cern.ch/user/p/pandolf/public/file_gammaJet.root']
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/file_gammaJet.root']
    #comp.files = ['/afs/cern.ch/user//m/mmasciov/public/TTJets_forSynch_1.root']
    ## 50 ns ttbar CSAv1
    #    comp=TTJets_MSDecaysCKM_central_PU_S14_POSTLS170
    ## 50 ns ttbar CSAv2
    #    comp=TTJets
    ## 25 ns ttbar PHYS14
    #comp = TTJets
    #comp.files = comp.files[:1]
    comp = GJets_HT600toInf
    comp.files = ['/afs/cern.ch/user/m/mmasciov/CMSSW_7_2_3_PhysicsTools/src/CMGTools/TTHAnalysis/cfg/miniAOD-prod_PAT.root']

#    comp=TTJets
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/ttjets_miniaodsim_00C90EFC-3074-E411-A845-002590DB9262.root']
#    comp=GJets_HT200to400
#    comp.files = ['/afs/cern.ch/work/d/dalfonso/public/gjets_ht200to400_miniaodsim_060B8ED3-8571-E411-A2CD-002590D0AFEA.root']
    selectedComponents = [comp]
#    comp.splitFactor = 10
elif test==2:
    #selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsToLL_M50_PU20bx25, TTJets_PUS14 ]
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 251
        comp.files = comp.files[:]
        #comp.files = comp.files[:1]

from PhysicsTools.HeppyCore.framework.services.tfile import TFileService 
output_service = cfg.Service(
      TFileService,
      'outputfile',
      name="outputfile",
      fname='mt2.root',
      option='recreate'
    )

# the following is declared in case this cfg is used in input to the heppy.py script                                                                                                                   
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [output_service],
                     events_class = Events)

#printComps(config.components, True)
        
