from numpy import *

#the meat and bones calculator to create scattering coefficients. Code is adapted from in "Absorbtion and Scattering" by Bohren, Huffman, which will be referred to as A&S or the book from now on. All page numbers listed are the PDF page numbers not book page numbers. The discussion of the why and how for the recurrence code begins at page 140. The original Fortran code begins on page 491.
#attempting to borrow as many var/function names from book as possible
#Primary goal is to calculate scattering coefficients a_n and b_n with funcitons pi_n and tau_n then sum
#################################################################


#function MeiParams
#calculates the size parameter x and relative refraction index for sphere and medium
#INPUTS
#sphereRef - spheres refraction index
#mediumRef - medium refraction index
#r - radius of sphere
#lamdaFS - free space wavelength
#numAng - number of angles between 0 and 90 deg
#        Matrix elements calculated at 2*numAng - 1 angles including 0,90, and 180
#OUTPUTS
#x is the size parameter, require about x terms in series for convergence(p. 491)
#refRel is the refraction index of the medium
#################################################################
refMed = 1.0

refRe = 1.55
refIm = 0.0

#refRel = Cmplx(refRemrefIm)/refMed

#x = 2 * pi * r * refMed/lamdaFS






#function MeiCoeffs
#calculates the amplitude scattering matrix elements, and efficiencies for extinction, total scattering and backscattering for a given size parameter and relative refractive index(p494)
#INPUTS
#x is the size parameter, x = k*r = 2*pi/lambdaFS * r
#refRel is the refraction index of the medium
#################################################################

#NSTOP is the real number of terms used for convergence in calculations,
#int NSTOP = x + 4*x^(1/3) +2

#NMX is taken as Max(NSTOP,abs(mx))+15 and D_NMX = 0.0 +i0.0 (pg492)




