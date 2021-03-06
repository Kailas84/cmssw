import FWCore.ParameterSet.Config as cms

pythia8CP4SettingsBlock = cms.PSet(
    pythia8CP4Settings = cms.vstring(
    'Tune:pp 14',
    'Tune:ee 7',
    'MultipartonInteractions:ecmPow=0.02012',
    'PDF:pSet=20',
    'MultipartonInteractions:bProfile=2',
    'MultipartonInteractions:pT0Ref=1.483',
    'MultipartonInteractions:coreRadius=0.5971',
    'MultipartonInteractions:coreFraction=0.3053',
    'ColourReconnection:range=5.613',
    'SigmaTotal:zeroAXB=off', 
    'SpaceShower:alphaSorder=2',
    'SpaceShower:alphaSvalue=0.118',
    'SigmaProcess:alphaSvalue=0.118',
    'SigmaProcess:alphaSorder=2',
    'MultipartonInteractions:alphaSvalue=0.118',
    'MultipartonInteractions:alphaSorder=2',
    'TimeShower:alphaSorder=2',
    'TimeShower:alphaSvalue=0.118',
    'SpaceShower:rapidityOrder=off', 
   )
)

