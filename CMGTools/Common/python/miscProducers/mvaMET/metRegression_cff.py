import FWCore.ParameterSet.Config as cms

from CMGTools.External.puJetIDAlgo_cff import *
from CMGTools.Common.Tools.cmsswRelease import cmsswIs44X, isNewerThan


if isNewerThan('CMSSW_5_3_0'):
    jetPtMin = 0.
    puJetIdAlgo = met_53x.clone()
    wpId = 3
else:
    jetPtMin = 1.
    puJetIdAlgo = PhilV1.clone()
    wpId = 2 # see MetUtilies.cc
pfMetForRegression   = cms.EDProducer(
    "MetFlavorProducer",
    CorrJetName     = cms.InputTag("slimmedJets"),
    PFCandidateName = cms.InputTag("packedPFCandidates"),
    VertexName      = cms.InputTag("offlineSlimmedPrimaryVertices"),
    RhoName         = cms.InputTag('fixedGridRhoFastjetAll'),
    JetPtMin        = cms.double(jetPtMin), # should be 0 for 5X and 1 for 4X
    dZMin           = cms.double(0.1),
    MetFlavor       = cms.int32(0),  # 0 PF  1 TK  2 No PU 3 PU  4 PUC
    WorkingPointId  = cms.uint32(wpId),
    PUJetId         = puJetIdAlgo,
    PUJetIdLowPt    = puJetIdAlgo,
    )
   
tkMet     =  pfMetForRegression.clone(MetFlavor = cms.int32(1))
nopuMet   =  pfMetForRegression.clone(MetFlavor = cms.int32(2))
puMet     =  pfMetForRegression.clone(MetFlavor = cms.int32(3),
                                      dZMin = 0.2)
pcMet     =  pfMetForRegression.clone(MetFlavor = cms.int32(4))

                          
MetRegressionSequence  = cms.Sequence (
    pfMetForRegression + 
    nopuMet +
    puMet + 
    pcMet +
    tkMet
    )
