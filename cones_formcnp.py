# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:48:48 2020

@author: ychen
"""

import math

for i in range(1,89) :
    t2 = ( math.tan( i * math.pi / 180 ) )**2
    print( "{0:4d} KX 0.0 {1:6e} 1".format(1000 + i, t2) )

print( "1090 PX 0.0" )

for i in range(91,180) :
    t2 = ( math.tan( i * math.pi / 180 ) )**2
    print( "{0:4d} KX 0.0 {1:6e} -1".format(1000 + i, t2) )

for i in range(1,89) :
    print( "{0:4d} 1 -0.001225 2 -3 -{1:d} {2:d} imp:p,e=1".format(1000 + i, 1000+i, 1000+i+1 ) )

for i in range(90,180) :
    print( "{0:4d} 1 -0.001225 2 -3 {1:d} -{2:d} imp:p,e=1".format(1000 + i, 1000+i, 1000+i+1 ) )
    
text_string = ""
for i in range(0,600):
    text_string += " "
    text_string += str(round(180-0.1*i,1))
    if (i>1 and i%15==0):
        text_string += "\n"
        text_string += "       "
print(text_string)