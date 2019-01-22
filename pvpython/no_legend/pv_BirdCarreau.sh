#!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau

pvpython pv_k_mean.py $BirdCarreau/inlet_0p5 &&
pvpython pv_k_mean.py $BirdCarreau/inlet0p5_impinging &&
pvpython pv_k_mean.py $BirdCarreau/inlet_0p3 &&
pvpython pv_k_mean.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 &&
pvpython pv_k_mean.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_5
