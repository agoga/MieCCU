#Author: Adam Goga

from numpy import *
from SingleSphereMiePy import bhmie

#physical setup should be as follows
#emitter is at x=0 and the middle of the lattice should be at x=0. Not implementing emitter distance
#from lattice as we should follow functional form for the intensity fall off to determine initial
#field strength
#all units in meters
pii = 4.*arctan(1.)#done in the miepy code so we will use it but I dont like it.
radius = .005#sphere radius
lamda = .03
k = 2*pii / lamda
x = 2*3.14159265*radius*1/lamda

Efield = 0
Etot = 0
z=0#assuming the level plane


refrel = 2.75681

#The following code will create an array of field data for each sphere for the specified number of
#a from center of lattice and angles to measure around the lattice this code
#will convert each distance and angle into distances and angles relative to the position of each given sphere
#sphere. That is, for every radius and angle given each sphere will have their own angle and radius
a = radius #spheres radius, all spheres should be same radius though it is not a hard fix


#TODO is this correct
#place emitter at 1 unit away down y axis
r_e = [0,-1]


def FieldAtR(spheres, rMag, ri, r_sp, detectAng):
    
    
    numAng = len(detectAng)
    numSpheres = len(r_sp)
    
    global Etot
    global Efield
    Etot = zeros(numAng,dtype=complex)
#for every sphere we will find r_s_d and theta_s_d
    for s in range(numSpheres):   
        #should not change based on detector movement
        r_s = r_sp[s]
        r_e_s = subtract(r_s,r_e)
        
        #Ei = EmitterIntensity
        Ei = 1#specific incoming field for this sphere
        
        #print('Sphere at position: ' + str(r_s))
        #print('Detector radius: ' + str(r))

        #this sphere will have a specific R and Theta for every R and Theta we are taking measurements for
        sRList = []
        sThetaList = []
        for j in range(numAng):
            theta_d = detectAng[j]
            #this is r_d relative to origin
            r_d = [rMag * sin(theta_d), rMag * cos(theta_d)]
            #calculate detector vectors.... inspector
            r_s_d = subtract(r_d,r_s)
            
            #update list of this radius's from this sphere for final field caluclation
            sRList.append(r_s_d)
                  
            #print("r_d - r_sp: " + str(rdTmp) + ' - ' + str(r_sp[s]) + ' = ' + str(r_s_d))
            
            #calculate the numerator dot product and denomenators scalar val
            #dot emitter to sphere and sphere to detector
            numDot = dot(r_e_s,r_s_d)
            #print('r_e dot r_s_d = ' + str(numDot))
            
            demVal = linalg.norm(r_s_d)*linalg.norm(r_e_s)
            #print("|r_s_d||r_e| = " + str(demVal))
            
            #list of cos(theta) specific to this sphere
            sThetaList.append(numDot/demVal)
           # print('cos ( theta_sp ) = ' + str(numDot/demVal))
            #end angle loop
        
        #sanity check, all of these should be the same
        #for r in r_D:
        #   print(linalg.norm(r_D))
        #end specific sphere loop
       # print('------------------------')
    
        #we have out list of angles and radius for this sphere

        #get the solutions
                                                #MUST CAST ARRAY AND NMPY ARRAY
        S1,S2 = bhmie(x,refrel,array(sThetaList))
       # print('SUM 1')
        #print(len(sum1))
        #print(len(sThetaList))
        #print(len(curThetaList))
        #print(len(curRList))
        #print(2*numAng-1)
        #tmpAng = concatenate((detectAng,pii/2+detectAng[1:]))
        
        #print(tmpAng)



        #this is the final calculation loop
        #we have radius and angle from this specific sphere
        #use those values to calculate field from this sphere for each angle which
        #is an in order calculate adding to the final Efield
        for oi in range(numAng):
            #distance from sphere for this specific angle
            #print()
            r_s_d = linalg.norm(sRList[oi])

            #we want to use the current radius wrt sphere for the calculation
            #E = exp(1.j*k*(r_s_d-z)) / (-1.j*k*r_s_d) * S1[oi]
            E = exp(1.j*k*(r_s_d-z)) / (-1.j) * S1[oi]
            #but the final cummulative field is wrt the radius' and angles from origin
            #E = E**2
            #REMOVE abs(E)**2 for multiple spheres
            Efield[ri][oi] = add(Efield[ri][oi], E)
            #print('Field at r: ' + str(r) + ' and angle: ' + str(t) + ' = ' + str(real(E)))

            #print(E)
            Etot[oi] = add(Etot[oi], E)#current sphere only for debugging
            
        #end sphere loop
    #end radius loop
    return Etot, Efield