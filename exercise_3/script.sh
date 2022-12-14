#!/bin/bash

observable="minimaxmbl m_b1b2 pT_b1b2 pT_ttbar pT_bjet1 pT_bjet2 pT_lep1 pT_lep2 mT_ttbar m_bbll minimaxmbl_old minimaxmbl_coarse1 minimaxmbl_coarse2 minimaxmbl_coarse3 particle_minimaxmbl_vs_minimaxmbl particle_m_b1b2_vs_m_b1b2 particle_pT_b1b2_bs_pT_b1b2 particle_pT_ttbar_vs_pT_ttbar particle_pT_bjet1_vs_pT_bjet1 particle_pT_bjet2_vs_pT_bjet2 particle_pT_lep1_vs_pT_lep1 particle_pT_lep2_vs_pT_lep2 particle_mT_ttbar_vs_mT_ttbar particle_m_bbll_vs_m_bbll particle_minimaxmbl_old_vs_minimaxmbl_old particle_minimaxmbl_coarse1_vs_minimaxmbl_coarse_1 particle_minimaxmbl_coarse2_vs_minimaxmbl_coarse_2 particle_minimaxmbl_coarse3_vs_minimaxmbl_coarse_3"

for word in $observable 
do

    echo $word
    python3.6 exercise_3

done