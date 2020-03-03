## a numerical approximation of the "Rain in Seattle" problem
import numpy as np
import matplotlib.pyplot as plt 

#input
pRain = 0.5
fT = 2/3
friends = 3
it = 10000

#calc
pNoRain = 1 - pRain
fL = 1 - fT
expected = (fT**friends)*pRain/((fT**friends)*pRain+(fL**friends)*pNoRain)

#initialise
pRain_YYY = 0
yeses = 0
rained = 0
P = []
D = []
AD = []
PG = []
DG = []
ADG = []
x = []

fig = plt.figure(num="LIVE", figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')           
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
        P.append(pRain_YYY)
        D.append(pRain_YYY - expected)
        AD.append(abs(pRain_YYY - expected))
        PG.append(pRain_YYY)
        DG.append(pRain_YYY - expected)
        ADG.append(abs(pRain_YYY - expected))
        x.append(yeses)
        
        
        if yeses/50 == round(yeses/50) :
            #plot most recent results live
            plt.clf()
            plt.subplot(121)  
            plt.plot(x,PG, label = "P(Rain given all say rain)")
            plt.plot(x,ADG, label = "Absolute distance to expected")
            plt.ylim(0,1)
            plt.legend(loc = 8)
            plt.subplot(122)  
            plt.plot(x,DG, label = "Distance to expected")
            plt.ylim(-0.05,0.05)
            plt.legend(loc = 8)
            fig.canvas.draw()
            fig.canvas.flush_events()
        
        if yeses>5000:
            PG.pop(0)
            DG.pop(0)
            ADG.pop(0)
            x.pop(0)
         
#plot iterations
plt.close()
fig = plt.figure(num="Complete", figsize=(14, 6), dpi=80, facecolor='w', edgecolor='k')
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