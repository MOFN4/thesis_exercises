# -*- coding: utf-8 -*-

import os
from ROOT import *

gROOT.SetBatch(True)


f = TFile.Open ("mc.TotalPrediction_DR.nominal.observables_allChannelsOptimized.v34_2.root")


t_reco = f.Get("reco/2j2b70_0extrab85_emu")
t_particle = f.Get("particle/2j2b_emu") 

pT_reco = TH1F("pT_bjet1", "pT_bjet1", 10, 0, 10000000)
pT_reco.SetLineColor(kRed)



pT_part = TH1F("pT_bjet1_part", "pT_bjet1_part", 10, 0, 10000000)
pT_part.SetLineColor(kBlue)

for event in t_particle.particle_pT_lep1:
    pT_part.Fill(event)
                  

for event in t_reco.pT_lep1:
        pT_reco.Fill(event)
    


c1 = TCanvas("c1", "my_canvas")
c1.Divide(2,1)
c1.cd(1)
reco_histo = t_reco.pT_lep1

reco_histo.SetLineColor(kRed)

reco_histo.Draw("HIST")
 
t_particle.particle_pT_lep1.Draw("HISTO,SAME") 

c1.cd(2)
t_reco.pT_lep2.SetLineColor(kRed)
t_reco.pT_lep2.Draw("HISTO")
t_particle.particle_pT_lep2.Draw("HISTO,SAME")

pT_reco.GetXaxis().SetTitle("pT_lep1")
pT_reco.GetYaxis().SetTitle("entries")



leg = TLegend(.73,.32,.97,.53)
leg.AddEntry(pT_reco,"Reco level")
leg.AddEntry(pT_part,"Particle level")
leg.Draw()

if not os.path.exists("result"):
    os.makedirs("result")

c1.SaveAs("result/pT_lep.png")
c1.SaveAs("result/pT_lep.pdf")



