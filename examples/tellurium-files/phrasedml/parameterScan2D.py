# -*- coding: utf-8 -*-
"""
phrasedml 2D parameter scan
"""

from __future__ import print_function
import os
from tellurium.sedml.case_template import run_case

antimonyStr = '''
// Created by libAntimony v2.9
model *parameterScan2D()

  // Compartments and Species:
  compartment compartment_;
  species MKKK in compartment_, MKKK_P in compartment_, MKK in compartment_;
  species MKK_P in compartment_, MKK_PP in compartment_, MAPK in compartment_;
  species MAPK_P in compartment_, MAPK_PP in compartment_;

  // Reactions:
  J0: MKKK => MKKK_P; (J0_V1*MKKK)/((1 + (MAPK_PP/J0_Ki)^J0_n)*(J0_K1 + MKKK));
  J1: MKKK_P => MKKK; (J1_V2*MKKK_P)/(J1_KK2 + MKKK_P);
  J2: MKK => MKK_P; (J2_k3*MKKK_P*MKK)/(J2_KK3 + MKK);
  J3: MKK_P => MKK_PP; (J3_k4*MKKK_P*MKK_P)/(J3_KK4 + MKK_P);
  J4: MKK_PP => MKK_P; (J4_V5*MKK_PP)/(J4_KK5 + MKK_PP);
  J5: MKK_P => MKK; (J5_V6*MKK_P)/(J5_KK6 + MKK_P);
  J6: MAPK => MAPK_P; (J6_k7*MKK_PP*MAPK)/(J6_KK7 + MAPK);
  J7: MAPK_P => MAPK_PP; (J7_k8*MKK_PP*MAPK_P)/(J7_KK8 + MAPK_P);
  J8: MAPK_PP => MAPK_P; (J8_V9*MAPK_PP)/(J8_KK9 + MAPK_PP);
  J9: MAPK_P => MAPK; (J9_V10*MAPK_P)/(J9_KK10 + MAPK_P);

  // Species initializations:
  MKKK = 90;
  MKKK_P = 10;
  MKK = 280;
  MKK_P = 10;
  MKK_PP = 10;
  MAPK = 280;
  MAPK_P = 10;
  MAPK_PP = 10;

  // Compartment initializations:
  compartment_ = 1;

  // Variable initializations:
  J0_V1 = 2.5;
  J0_Ki = 9;
  J0_n = 1;
  J0_K1 = 10;
  J1_V2 = 0.25;
  J1_KK2 = 8;
  J2_k3 = 0.025;
  J2_KK3 = 15;
  J3_k4 = 0.025;
  J3_KK4 = 15;
  J4_V5 = 0.75;
  J4_KK5 = 15;
  J5_V6 = 0.75;
  J5_KK6 = 15;
  J6_k7 = 0.025;
  J6_KK7 = 15;
  J7_k8 = 0.025;
  J7_KK8 = 15;
  J8_V9 = 0.5;
  J8_KK9 = 15;
  J9_V10 = 0.5;
  J9_KK10 = 15;

  // Other declarations:
  const compartment_, J0_V1, J0_Ki, J0_n, J0_K1, J1_V2, J1_KK2, J2_k3, J2_KK3;
  const J3_k4, J3_KK4, J4_V5, J4_KK5, J5_V6, J5_KK6, J6_k7, J6_KK7, J7_k8;
  const J7_KK8, J8_V9, J8_KK9, J9_V10, J9_KK10;
end
'''

phrasedmlStr = '''
  model_3 = model "parameterScan2D"
  sim_repeat = simulate uniform(0,3000,100)
  task_1 = run sim_repeat on model_3
  repeatedtask_1 = repeat task_1 for J1_KK2 in [1, 5, 10, 50, 60, 70, 80, 90, 100], reset=true
  repeatedtask_2 = repeat repeatedtask_1 for J4_KK5 in uniform(1, 40, 10), reset=true
  plot repeatedtask_2.J4_KK5 vs repeatedtask_2.J1_KK2
  plot repeatedtask_2.time vs repeatedtask_2.MKK, repeatedtask_2.MKK_P
'''

run_case(os.path.realpath(__file__), antimonyStr, phrasedmlStr)
