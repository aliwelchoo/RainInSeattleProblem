## a numerical approximation of the "Rain in Seattle" problem
import numpy as np
import matplotlib.pyplot as plt 

#input
pRain = 0.5
fT = 2/3
friends = 3
it = 100000

#calc
pNoRain = 1 - pRain
fL = 1 - fT
expected = (fT**friends)*pRain/((fT**friends)*pRain+(fL**friends)*pNoRain)

#initialise
pRain_YYY = 0
yeses = 0
rained = 0
P = [0]*it
D = [0]*it
AD = [0]*it

#calculate
while yeses < it :
    rain = np.random.random() <= pRain
    f = [not (rain ^ (rand <= fT)) for rand in np.random.random(friends)] 
    if all(f) :
        pRain_YYY_last = pRain_YYY
        yeses  += 1
        if rain :  
            rained += 1
        pRain_YYY = rained/yeses
        P[yeses-1] = pRain_YYY
        D[yeses-1] = pRain_YYY - expected
        AD[yeses-1] = abs(pRain_YYY - expected)
    
#plot iterations
plt.figure(num=None, figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')    
plt.subplot(121)        
plt.plot(P, label = "P(Rain given all say rain)")
plt.plot(AD, label = "Absolute distance to expected")
plt.ylim(0,1)
plt.legend(loc = 8)
plt.subplot(122)  
plt.plot(D, label = "Distance to expected")
plt.ylim(-0.05,0.05)
plt.legend(loc = 8)
plt.show()

#print final result
print("  Expected: " + str(round(expected,10)) + "\nCalculated: " + str(round(pRain_YYY,10)) + "\nDifference: " + str(round(abs(pRain_YYY - expected),10)))