# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:40:22 2017

@author: pjcigan

"""

import numpy as np

# life with NaN can be tricky

a = 5
print a == 5
# --> True
 
a = np.nan
print a == np.nan # --> False
print np.isnan(a) # --> True


#Generate some x-vals, as well as some y-vals with scatter.
xvals = np.arange(-3,5,.2)
yvals = xvals**2 - 7
for i in range( len(yvals) ): yvals[i] += 2*np.random.randn()
    
print yvals.min(), np.min(yvals)

# let's add some NaNs

yvals_with_nans = yvals.copy()
yvals_with_nans[3:10] = np.nan

print np.min(yvals_with_nans) # --> nan
print np.max(yvals_with_nans) # --> nan
print np.sum(yvals_with_nans) # --> nan

print 'In contrast : \n'
print np.nanmin(yvals_with_nans) # --> -10.287...

# Keep the original array while only using the non-NaN elements in calculation?
# use numpy masked arrays

a = np.ma.masked_array([1,2,3,4,5],mask=0)
print a
# --> [1 2 3 4 5], mask = [False False False False False]

np.sum(a) # --> 15

a.mask[2] = True; a.mask[4] = True
print a
# --> [1 2 -- 4 --], mask = [False False True False True]

# a.data just keep the whole array
print a.mask # --> [False False True False True]
print a.data # --> [1 2 3 4 5]

# A trick : Nb of the masked/un-masked elements
# by summing up booleans !!

# In fact Booleans are 1/0. Adding up True/1 will give Nb of masked elements
# Inverse the Booleans by using '-' (though deprecationWarning), we get un-masked elements
# '~' is better
print 'Nb of Masked elements :', np.sum(a.mask) # --> 2
print 'Nb of un-Masked elements :', np.sum(-a.mask) # --> 3
print 'Nb of un-Masked elements :', np.sum(~a.mask) # --> 3  


# take an array and  mask NaN and inf
y_masked = np.ma.masked_invalid( yvals_with_nans )
 
print y_masked #Note how the nans have been replaced by -- marks
 
print np.sum(y_masked) # --> 3.34306...

# compress the array adn get all-unmasked array
y_compressed = y_masked.compressed() #If you print, you will notice that the NaNs are now gone.


#==============================================================================
# Get a scatter plot while making x and y of the same length?
# Use mask !!
#==============================================================================
x_masked = np.ma.masked_array(xvals, mask=y_masked.mask)
x_compressed = x_masked.compressed()
print len(xvals), len(yvals_with_nans), len(x_compressed), len(y_compressed)
# --> 40 40 33 33
 
#Or you can even just do it on-the-fly with
x_compressed = np.ma.masked_array(xvals, mask=y_masked.mask).compressed()