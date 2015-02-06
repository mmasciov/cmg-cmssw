from CRABClient.client_utilities import getBasicConfig
config = getBasicConfig()

config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'patTuple_mini_fixPhotons.py'
#config.JobType.outputFiles = ['outfile.root']

#config.Data.inputDataset = '/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
#config.Data.inputDataset = '/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v2/MINIAODSIM'
config.Data.inputDataset = '/QCD_HT-100To250_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.publishDataName = 'miniAOD_fixPhoton_reco'
config.Data.publishDBS = 'phys03'
config.Data.outLFN = '/store/group/phys_susy/mmasciov/PHYS14_fixPhoton_reco/'
#config.Data.outLFN = '/store/user/mmasciov/PHYS14_fixPhoton/'

##config.Data.ignoreLocality = True
##config.Site.whitelist = ["T2_US*"]
config.Site.whitelist = ["T2_CH_CERN"]

config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_CH_CSCS'
