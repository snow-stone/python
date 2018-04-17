#!/usr/bin/env python

# Perform a simple check that the data is loaded, has correct dimensions and
# contains no NaNs

import numpy as np

# load the data
M1_mean_u = np.genfromtxt("./profiles/M1_mean_u")
M2_mean_u = np.genfromtxt("./profiles/M2_mean_u")
M3_mean_u = np.genfromtxt("./profiles/M3_mean_u")

M1_Reynolds_stresses = np.genfromtxt("./profiles/M1_Reynolds_stresses")
M2_Reynolds_stresses = np.genfromtxt("./profiles/M2_Reynolds_stresses")
M3_Reynolds_stresses = np.genfromtxt("./profiles/M3_Reynolds_stresses")

M1_S = np.genfromtxt("./profiles/M1_S")
M2_S = np.genfromtxt("./profiles/M2_S")
M3_S = np.genfromtxt("./profiles/M3_S")

M1_F = np.genfromtxt("./profiles/M1_F")
M2_F = np.genfromtxt("./profiles/M2_F")
M3_F = np.genfromtxt("./profiles/M3_F")

M1_vorticity_fluctuations = np.genfromtxt("./profiles/M1_vorticity_fluctuations")
M2_vorticity_fluctuations = np.genfromtxt("./profiles/M2_vorticity_fluctuations")
M3_vorticity_fluctuations = np.genfromtxt("./profiles/M3_vorticity_fluctuations")

# check array shapes 
assert M1_mean_u.shape == (50,2)
assert M2_mean_u.shape == (100,2)
assert M3_mean_u.shape == (200,2)

assert M1_Reynolds_stresses.shape == (50,5)
assert M2_Reynolds_stresses.shape == (100,5)
assert M3_Reynolds_stresses.shape == (200,5)

assert M1_vorticity_fluctuations.shape == (50,4)
assert M2_vorticity_fluctuations.shape == (100,4)
assert M3_vorticity_fluctuations.shape == (200,4)

assert M1_S.shape == (50,4)
assert M2_S.shape == (100,4)
assert M3_S.shape == (200,4)

assert M1_F.shape == (50,4)
assert M2_F.shape == (100,4)
assert M3_F.shape == (200,4)

#check for NaNs
assert np.count_nonzero(np.isnan(M1_mean_u)) == 0
assert np.count_nonzero(np.isnan(M2_mean_u)) == 0
assert np.count_nonzero(np.isnan(M3_mean_u)) == 0

assert np.count_nonzero(np.isnan(M1_Reynolds_stresses)) == 0
assert np.count_nonzero(np.isnan(M2_Reynolds_stresses)) == 0
assert np.count_nonzero(np.isnan(M3_Reynolds_stresses)) == 0

assert np.count_nonzero(np.isnan(M1_vorticity_fluctuations)) == 0
assert np.count_nonzero(np.isnan(M2_vorticity_fluctuations)) == 0
assert np.count_nonzero(np.isnan(M3_vorticity_fluctuations)) == 0

assert np.count_nonzero(np.isnan(M1_S)) == 0
assert np.count_nonzero(np.isnan(M2_S)) == 0
assert np.count_nonzero(np.isnan(M3_S)) == 0

assert np.count_nonzero(np.isnan(M1_F)) == 0
assert np.count_nonzero(np.isnan(M2_F)) == 0
assert np.count_nonzero(np.isnan(M3_F)) == 0

print "Everything seems fine!"
